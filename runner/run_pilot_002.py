#!/usr/bin/env python3
"""Execution harness for DCB PILOT_002.

PILOT_002 is a post-PILOT_001 redesign with harder forced choices, a semantic-free
A/B response coordinate, frozen test-retest calibration, and an auxiliary I0
context-separation stress test.

Required environment:
  DCB_API_KEY
  DCB_MODEL
Optional:
  DCB_API_BASE
  DCB_MODEL_VERSION
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
ITEM_BANK = ROOT / "prompts" / "item_bank_pilot_002.json"
RAW_DIR = ROOT / "trajectories" / "raw"
PRIMARY_ARMS = ("OWN+REFL", "OWN-REFL", "OTHER+REFL", "OTHER-REFL")
CONTROL_ARMS = ("INSTR", "FALSE-OWN", "NONE")
CALIBRATION_IDS = {f"P002-{i:03d}" for i in range(1, 9)}
GAP_BLOCK = "Administrative note: reference marker K7. No task facts, preferences, evidence, or decision rules are added by this note."
SUBJECTIVE_RE = re.compile(
    r"\b(i|me|my|mine|myself|you|your|yours|yourself|we|our|ours|ourselves|"
    r"this answer|the response above|my answer|your answer)\b",
    re.IGNORECASE,
)


def api_call(messages: list[dict[str, str]], *, model: str, base: str, key: str) -> str:
    payload = json.dumps({"model": model, "messages": messages, "temperature": 0.0}).encode("utf-8")
    req = Request(
        base.rstrip("/") + "/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=180) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body["choices"][0]["message"]["content"].strip()


def option_token(text: str) -> str | None:
    m = re.match(r"\s*([AB])\b", text, re.IGNORECASE)
    return m.group(1).upper() if m else None


def option_coord(text: str) -> int | None:
    tok = option_token(text)
    if tok == "A":
        return 0
    if tok == "B":
        return 1
    return None


def valid_r(text: str) -> tuple[bool, str | None]:
    if not text.strip():
        return False, "empty reflection"
    m = SUBJECTIVE_RE.search(text)
    if m:
        return False, f"subjective/indexical token: {m.group(0)!r}"
    return True, None


def common_task(task: str) -> str:
    return task + "\n\nReturn exactly one option token, A or B, followed by one short reason."


def reflection_prompt() -> str:
    return (
        "Review the artifact produced for the task above. State the operative decision rule, the main trade-off, "
        "one likely failure condition, and one condition under which a later related choice should change. "
        "Write propositions only. Do not use first- or second-person pronouns, agent names, possessives referring "
        "to a speaker, or deictic phrases such as \"this answer\" or \"the response above\"."
    )


def gap_text(level: str) -> str:
    n = {"H0": 0, "H2": 2, "H6": 6}[level]
    if n == 0:
        return ""
    return "\n".join([GAP_BLOCK] * n)


def arm_prompt(arm: str, artifact: str, r: str, probe: str, consideration: str, gap_level: str = "H0") -> str:
    gap = gap_text(gap_level)
    suffix = "\n\nReturn exactly one option token, A or B, followed by one short reason."
    g = ("\n\n" + gap) if gap else ""
    if arm == "OWN+REFL":
        return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}{g}\n\nUse the earlier work and reflection where relevant. Now answer:\n{probe}{suffix}"
    if arm == "OWN-REFL":
        return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}{g}\n\nUse the earlier work where relevant. Now answer:\n{probe}{suffix}"
    if arm == "OTHER+REFL":
        return f"The following artifact was produced earlier by another model instance:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}{g}\n\nUse that earlier work and reflection where relevant. Now answer:\n{probe}{suffix}"
    if arm == "OTHER-REFL":
        return f"The following artifact was produced earlier by another model instance:\n{artifact}{g}\n\nUse that earlier work where relevant. Now answer:\n{probe}{suffix}"
    if arm == "INSTR":
        return f"Use the following general decision consideration where relevant:\n{consideration}\n\n{probe}{suffix}"
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


def call_prompt(prompt: str, *, model: str, base: str, key: str) -> dict[str, Any]:
    response = api_call([{"role": "user", "content": prompt}], model=model, base=base, key=key)
    return {"response": response, "option": option_token(response), "m": option_coord(response)}


def run(seed_id: str, max_reflection_attempts: int = 5) -> dict[str, Any]:
    key = os.environ.get("DCB_API_KEY")
    model = os.environ.get("DCB_MODEL")
    model_version = os.environ.get("DCB_MODEL_VERSION") or model
    base = os.environ.get("DCB_API_BASE", "https://api.openai.com/v1")
    if not key or not model:
        raise SystemExit("Set DCB_API_KEY and DCB_MODEL.")

    seed = load_seed(seed_id)
    out_path = RAW_DIR / f"{seed_id}.json"
    if out_path.exists():
        raise SystemExit(f"Refusing to overwrite existing raw trajectory: {out_path}")

    started = time.time()
    artifact = api_call([{"role": "user", "content": common_task(seed["task"])}], model=model, base=base, key=key)

    restarts: list[dict[str, Any]] = []
    canonical_r = None
    for attempt in range(1, max_reflection_attempts + 1):
        candidate = api_call([
            {"role": "user", "content": common_task(seed["task"])},
            {"role": "assistant", "content": artifact},
            {"role": "user", "content": reflection_prompt()},
        ], model=model, base=base, key=key)
        ok, reason = valid_r(candidate)
        if ok:
            canonical_r = candidate
            break
        restarts.append({"attempt": attempt, "reason": reason, "candidate": candidate})

    excluded = canonical_r is None
    record: dict[str, Any] = {
        "pilot": "PILOT_002",
        "seed_id": seed_id,
        "family": seed["family"],
        "model": model,
        "model_version": model_version,
        "api_base": base,
        "request_parameters": {"temperature": 0.0},
        "interface_level": "I0",
        "s1_status": "NOT_TESTABLE",
        "artifact": artifact,
        "artifact_option": option_token(artifact),
        "artifact_m": option_coord(artifact),
        "canonical_r": canonical_r,
        "canonical_r_sha256": hashlib.sha256((canonical_r or "").encode("utf-8")).hexdigest(),
        "phase2_restart_count": len(restarts),
        "phase2_restarts": restarts,
        "excluded": excluded,
        "exclusion_code": "R_VALIDATION_FAILED" if excluded else None,
        "primary": {},
        "controls": {},
        "calibration": {},
        "h_context": {},
        "started_unix": started,
    }

    if not excluded:
        for arm in PRIMARY_ARMS:
            record["primary"][arm] = {}
            for fam in ("related", "unrelated"):
                prompt = arm_prompt(arm, artifact, canonical_r, seed[fam], seed["target_consideration"], "H0")
                record["primary"][arm][fam] = call_prompt(prompt, model=model, base=base, key=key)

        for arm in CONTROL_ARMS:
            record["controls"][arm] = {}
            for fam in ("related", "unrelated"):
                prompt = arm_prompt(arm, artifact, canonical_r, seed[fam], seed["target_consideration"], "H0")
                record["controls"][arm][fam] = call_prompt(prompt, model=model, base=base, key=key)

        if seed_id in CALIBRATION_IDS:
            for arm in PRIMARY_ARMS:
                prompt = arm_prompt(arm, artifact, canonical_r, seed["related"], seed["target_consideration"], "H0")
                record["calibration"][arm] = call_prompt(prompt, model=model, base=base, key=key)

            for level in ("H0", "H2", "H6"):
                record["h_context"][level] = {}
                for arm in PRIMARY_ARMS:
                    prompt = arm_prompt(arm, artifact, canonical_r, seed["related"], seed["target_consideration"], level)
                    record["h_context"][level][arm] = call_prompt(prompt, model=model, base=base, key=key)

    record["finished_unix"] = time.time()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out_path)
    return record


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="P002-001")
    ap.add_argument("--max-reflection-attempts", type=int, default=5)
    args = ap.parse_args()
    run(args.seed, args.max_reflection_attempts)


if __name__ == "__main__":
    main()
