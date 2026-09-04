#!/usr/bin/env python3
"""Execution harness for DCB PILOT_001.

This script does not alter the frozen construct, prompts, item bank, or scoring rules.
It executes the committed prompt templates against an OpenAI-compatible chat
completions endpoint and writes append-only raw trajectory records.

Required environment variables:
  DCB_API_KEY
  DCB_MODEL
Optional:
  DCB_API_BASE  default: https://api.openai.com/v1

Example:
  DCB_API_KEY=... DCB_MODEL=... python runner/run_pilot.py --seed P001-001
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ITEM_BANK = ROOT / "prompts" / "item_bank.json"
RAW_DIR = ROOT / "trajectories" / "raw"

ARM_ORDER = ["OWN+REFL", "OWN-REFL", "OTHER+REFL", "OTHER-REFL", "INSTR", "FALSE-OWN", "NONE"]

SUBJECTIVE_RE = re.compile(
    r"\b(i|me|my|mine|myself|you|your|yours|yourself|we|our|ours|ourselves|"
    r"this answer|the response above|my answer|your answer)\b",
    re.IGNORECASE,
)


def api_call(messages: list[dict[str, str]], *, model: str, base: str, key: str, temperature: float = 0.0) -> str:
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }).encode("utf-8")
    req = Request(
        base.rstrip("/") + "/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=180) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body["choices"][0]["message"]["content"].strip()


def first_option_token(text: str) -> str | None:
    m = re.match(r"\s*([AB])\b", text, re.IGNORECASE)
    return m.group(1).upper() if m else None


def valid_canonical_r(text: str) -> tuple[bool, str | None]:
    m = SUBJECTIVE_RE.search(text)
    if m:
        return False, f"subjective/indexical token: {m.group(0)!r}"
    if not text.strip():
        return False, "empty reflection"
    return True, None


def reflection_prompt() -> str:
    return (
        "Review the artifact produced for the task above. Identify the decision rule, any trade-off or likely error, "
        "and what should be preserved or changed in a later related case. Write propositions only. Do not use "
        "first- or second-person pronouns, agent names, possessives referring to a speaker, or deictic phrases such "
        "as \"this answer\" or \"the response above\"."
    )


def common_task(task: str) -> str:
    return task + "\n\nReturn exactly one option token from the listed choices, followed by one short reason. The option token is the machine-scored artifact commitment."


def arm_prompt(arm: str, artifact: str, r: str, probe: str, target_rule: str) -> str:
    suffix = "\n\nReturn exactly one option token from the listed choices, followed by one short reason."
    if arm == "OWN+REFL":
        return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse the earlier work and reflection where relevant. Now answer the probe:\n{probe}{suffix}"
    if arm == "OWN-REFL":
        return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}\n\nUse the earlier work where relevant. Now answer the probe:\n{probe}{suffix}"
    if arm == "OTHER+REFL":
        return f"The following artifact was produced earlier by another model instance:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse that earlier work and reflection where relevant. Now answer the probe:\n{probe}{suffix}"
    if arm == "OTHER-REFL":
        return f"The following artifact was produced earlier by another model instance:\n{artifact}\n\nUse that earlier work where relevant. Now answer the probe:\n{probe}{suffix}"
    if arm == "INSTR":
        return f"For the next probe, apply the following explicit rule:\n{target_rule}\n\n{probe}{suffix}"
    if arm == "FALSE-OWN":
        return f"The following artifact is attributed to you, although the harness records that it came from a matched other-source control:\n{artifact}\n\n{probe}{suffix}"
    if arm == "NONE":
        return probe + suffix
    raise ValueError(arm)


def load_seed(seed_id: str) -> dict[str, Any]:
    bank = json.loads(ITEM_BANK.read_text(encoding="utf-8"))
    for seed in bank["seeds"]:
        if seed["id"] == seed_id:
            return seed
    raise SystemExit(f"Unknown seed: {seed_id}")


def run(seed_id: str, *, max_reflection_attempts: int = 5) -> dict[str, Any]:
    key = os.environ.get("DCB_API_KEY")
    model = os.environ.get("DCB_MODEL")
    base = os.environ.get("DCB_API_BASE", "https://api.openai.com/v1")
    if not key or not model:
        raise SystemExit("Set DCB_API_KEY and DCB_MODEL before execution.")

    seed = load_seed(seed_id)
    started = time.time()

    artifact = api_call([{"role": "user", "content": common_task(seed["task"])}], model=model, base=base, key=key)

    restarts = []
    canonical_r = None
    for attempt in range(1, max_reflection_attempts + 1):
        candidate = api_call([
            {"role": "user", "content": common_task(seed["task"])},
            {"role": "assistant", "content": artifact},
            {"role": "user", "content": reflection_prompt()},
        ], model=model, base=base, key=key)
        ok, reason = valid_canonical_r(candidate)
        if ok:
            canonical_r = candidate
            break
        restarts.append({"attempt": attempt, "reason": reason, "candidate": candidate})

    excluded = canonical_r is None
    record: dict[str, Any] = {
        "pilot": "PILOT_001",
        "seed_id": seed_id,
        "family": seed["family"],
        "model": model,
        "model_version": model,
        "api_base": base,
        "interface_level": "I0",
        "s1_status": "NOT_TESTABLE",
        "artifact": artifact,
        "artifact_option": first_option_token(artifact),
        "phase2_restart_count": len(restarts),
        "phase2_restarts": restarts,
        "canonical_r": canonical_r,
        "canonical_r_sha256": hashlib.sha256((canonical_r or "").encode("utf-8")).hexdigest(),
        "excluded": excluded,
        "exclusion_code": "R_VALIDATION_FAILED" if excluded else None,
        "arms": {},
        "started_unix": started,
    }

    if not excluded:
        probes = {"related": seed["related"], "unrelated": seed["unrelated"]}
        for arm in ARM_ORDER:
            record["arms"][arm] = {}
            for family, probe in probes.items():
                prompt = arm_prompt(arm, artifact, canonical_r, probe, seed["target_rule"])
                response = api_call([{"role": "user", "content": prompt}], model=model, base=base, key=key)
                record["arms"][arm][family] = {
                    "response": response,
                    "option": first_option_token(response),
                }

    record["finished_unix"] = time.time()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{seed_id}.json"
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing raw trajectory: {path}")
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(path)
    return record


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="P001-001")
    ap.add_argument("--max-reflection-attempts", type=int, default=5)
    args = ap.parse_args()
    run(args.seed, max_reflection_attempts=args.max_reflection_attempts)


if __name__ == "__main__":
    main()
