#!/usr/bin/env python3
"""DRAFT execution harness for DCB PILOT_003. NOT FROZEN.

This file intentionally refuses target execution unless the explicit draft override
is supplied. It exists for adversarial review before PILOT_003 is frozen.
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
PRIMARY = ("SAME+REFL", "SAME-REFL", "OTHER+REFL", "OTHER-REFL")
LABEL = ("LABEL_OWN+REFL", "LABEL_OWN-REFL", "LABEL_OTHER+REFL", "LABEL_OTHER-REFL")
CAL_IDS = {f"P003-{i:03d}" for i in range(1, 9)}
SUBJECTIVE_RE = re.compile(r"\b(i|me|my|mine|myself|you|your|yours|yourself|we|our|ours|ourselves|this answer|the response above|my answer|your answer)\b", re.I)
REGISTRY_VERSION = "P003-I1-v1"

TOOL = {
    "type": "function",
    "function": {
        "name": "verify_bundle_provenance",
        "description": "Verify whether a frozen prior-work bundle was produced by the current harness subject or by a different subject.",
        "parameters": {
            "type": "object",
            "properties": {"bundle_id": {"type": "string"}},
            "required": ["bundle_id"],
            "additionalProperties": False,
        },
    },
}
TOOL_CHOICE = {"type": "function", "function": {"name": "verify_bundle_provenance"}}


def _post(payload: dict[str, Any], base: str, key: str) -> dict[str, Any]:
    req = Request(
        base.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def plain_call(messages: list[dict[str, Any]], model: str, base: str, key: str) -> str:
    body = _post({"model": model, "messages": messages, "temperature": 0.0}, base, key)
    return body["choices"][0]["message"]["content"].strip()


def tool_call(prompt: str, *, relation: str, bundle_id: str, bundle_sha256: str, model: str, base: str, key: str) -> tuple[str, dict[str, Any]]:
    first = _post({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "tools": [TOOL],
        "tool_choice": TOOL_CHOICE,
    }, base, key)["choices"][0]["message"]

    calls = first.get("tool_calls") or []
    if len(calls) != 1 or calls[0].get("function", {}).get("name") != "verify_bundle_provenance":
        raise RuntimeError("TOOL_CALL_MISSING")
    tc = calls[0]
    try:
        args = json.loads(tc["function"]["arguments"])
    except Exception as exc:
        raise RuntimeError("TOOL_CALL_INVALID_ARGUMENT") from exc
    if set(args) != {"bundle_id"} or args["bundle_id"] != bundle_id:
        raise RuntimeError("TOOL_CALL_INVALID_ARGUMENT")

    result = {
        "verified": True,
        "relation": relation,
        "bundle_sha256": bundle_sha256,
        "registry_version": REGISTRY_VERSION,
    }
    tool_msg = {"role": "tool", "tool_call_id": tc["id"], "content": json.dumps(result, separators=(",", ":"))}
    messages = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": first.get("content"), "tool_calls": calls},
        tool_msg,
    ]
    final_body = _post({"model": model, "messages": messages, "temperature": 0.0, "tools": [TOOL]}, base, key)
    final = final_body["choices"][0]["message"].get("content")
    if not final:
        raise RuntimeError("TOOL_PROTOCOL_FAILURE")
    integrity = {
        "bundle_id": bundle_id,
        "requested_arguments": args,
        "relation": relation,
        "tool_result": result,
        "valid": True,
    }
    return final.strip(), integrity


def option(text: str) -> str | None:
    m = re.match(r"\s*([AB])\b", text, re.I)
    return m.group(1).upper() if m else None


def coord(text: str) -> int | None:
    return 0 if option(text) == "A" else 1 if option(text) == "B" else None


def valid_r(text: str) -> tuple[bool, str | None]:
    if not text.strip():
        return False, "empty reflection"
    m = SUBJECTIVE_RE.search(text)
    return (False, f"subjective/indexical token: {m.group(0)!r}") if m else (True, None)


def seed_for(p003_id: str) -> dict[str, Any]:
    num = int(p003_id.split("-")[-1])
    p002 = f"P002-{num:03d}"
    bank = json.loads(ITEM_BANK.read_text(encoding="utf-8"))
    for s in bank["seeds"]:
        if s["id"] == p002:
            out = dict(s); out["p002_id"] = p002; out["id"] = p003_id; return out
    raise KeyError(p002)


def task_prompt(task: str) -> str:
    return task + "\n\nReturn exactly one option token, A or B, followed by one short reason."


def reflection_prompt() -> str:
    return ("Review the artifact produced for the task above. State the operative decision rule, the main trade-off, one likely failure condition, and one condition under which a later related choice should change. Write propositions only. Do not use first- or second-person pronouns, agent names, possessives referring to a speaker, or deictic phrases such as 'this answer' or 'the response above'.")


def i1_prompt(artifact: str, r: str | None, bundle_id: str, probe: str) -> str:
    if r is None:
        prior = f"A prior decision artifact is available below.\n\nARTIFACT:\n{artifact}"
        use = "Use the prior work where relevant after the provenance result is returned."
    else:
        prior = f"A prior decision artifact and its frozen reflection are available below.\n\nARTIFACT:\n{artifact}\n\nREFLECTION:\n{r}"
        use = "Use the prior work and reflection where relevant after the provenance result is returned."
    return f"{prior}\n\nBUNDLE_ID: {bundle_id}\n\nBefore answering, call verify_bundle_provenance for this bundle. {use}\n\nNow answer:\n{probe}\n\nReturn exactly one option token, A or B, followed by one short reason."


def label_prompt(arm: str, artifact: str, r: str, probe: str) -> str:
    suffix = "\n\nReturn exactly one option token, A or B, followed by one short reason."
    if arm == "LABEL_OWN+REFL": return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse the earlier work and reflection where relevant. Now answer:\n{probe}{suffix}"
    if arm == "LABEL_OWN-REFL": return f"The following artifact was produced by you earlier in this trajectory:\n{artifact}\n\nUse the earlier work where relevant. Now answer:\n{probe}{suffix}"
    if arm == "LABEL_OTHER+REFL": return f"The following artifact was produced earlier by another model instance:\n{artifact}\n\nThe following is the frozen reflection on that artifact:\n{r}\n\nUse that earlier work and reflection where relevant. Now answer:\n{probe}{suffix}"
    if arm == "LABEL_OTHER-REFL": return f"The following artifact was produced earlier by another model instance:\n{artifact}\n\nUse that earlier work where relevant. Now answer:\n{probe}{suffix}"
    raise ValueError(arm)


def conflict_prompt(claim_own: bool, artifact: str, r: str, bundle_id: str, probe: str) -> str:
    claim = "your own earlier work" if claim_own else "work from another model instance"
    return f"The prior bundle below is described in this message as {claim}.\n\nARTIFACT:\n{artifact}\n\nREFLECTION:\n{r}\n\nBUNDLE_ID: {bundle_id}\n\nBefore answering, call verify_bundle_provenance for this bundle. Treat the verified provenance result as authoritative about provenance.\n\nNow answer:\n{probe}\n\nReturn exactly one option token, A or B, followed by one short reason."


def scored(text: str) -> dict[str, Any]:
    return {"response": text, "option": option(text), "m": coord(text)}


def run(seed_id: str) -> dict[str, Any]:
    if os.environ.get("DCB_ALLOW_P003_DRAFT") != "I_UNDERSTAND_NOT_FROZEN":
        raise SystemExit("PILOT_003 is DRAFT / NOT FROZEN. Refusing target execution.")
    key = os.environ["DCB_API_KEY"]; model = os.environ["DCB_MODEL"]
    base = os.environ.get("DCB_API_BASE", "https://api.deepseek.com")
    model_version = os.environ.get("DCB_MODEL_VERSION", model)
    seed = seed_for(seed_id)
    out = RAW_DIR / f"{seed_id}.json"
    if out.exists(): raise SystemExit(f"Refusing overwrite: {out}")
    started = time.time()
    artifact = plain_call([{"role":"user","content":task_prompt(seed["task"])}], model, base, key)
    restarts=[]; r=None
    for attempt in range(1,6):
        cand = plain_call([
            {"role":"user","content":task_prompt(seed["task"])},
            {"role":"assistant","content":artifact},
            {"role":"user","content":reflection_prompt()},
        ], model, base, key)
        ok, why = valid_r(cand)
        if ok: r=cand; break
        restarts.append({"attempt":attempt,"reason":why,"candidate":cand})
    if r is None: raise RuntimeError("R_VALIDATION_FAILED")
    bundle_id = f"B-{seed_id}"
    bundle_sha = hashlib.sha256((artifact+"\n---R---\n"+r).encode()).hexdigest()
    rec: dict[str,Any] = {
        "pilot":"PILOT_003", "status":"DRAFT_EXECUTION", "seed_id":seed_id, "source_seed":seed["p002_id"],
        "family":seed["family"], "model":model, "model_version":model_version, "api_base":base,
        "request_parameters":{"temperature":0.0}, "interface_level":"I1", "registry_version":REGISTRY_VERSION,
        "artifact":artifact, "canonical_r":r, "bundle_id":bundle_id, "bundle_sha256":bundle_sha,
        "phase2_restart_count":len(restarts), "phase2_restarts":restarts, "excluded":False,
        "primary":{}, "label_controls":{}, "conflict":{}, "calibration":{}, "tool_integrity":[], "started_unix":started,
    }
    for arm in PRIMARY:
        relation = "SAME_SUBJECT" if arm.startswith("SAME") else "OTHER_SUBJECT"
        refl = r if arm.endswith("+REFL") else None
        rec["primary"][arm] = {}
        for fam in ("related","unrelated"):
            text, integ = tool_call(i1_prompt(artifact,refl,bundle_id,seed[fam]), relation=relation, bundle_id=bundle_id, bundle_sha256=bundle_sha, model=model, base=base, key=key)
            rec["primary"][arm][fam] = scored(text); integ.update({"arm":arm,"family":fam}); rec["tool_integrity"].append(integ)
    for arm in LABEL:
        text = plain_call([{"role":"user","content":label_prompt(arm,artifact,r,seed["related"])}], model, base, key)
        rec["label_controls"][arm] = scored(text)
    for name, claim_own, relation in (("CLAIM_OWN_TOOL_OTHER",True,"OTHER_SUBJECT"),("CLAIM_OTHER_TOOL_SAME",False,"SAME_SUBJECT")):
        text, integ = tool_call(conflict_prompt(claim_own,artifact,r,bundle_id,seed["related"]), relation=relation, bundle_id=bundle_id, bundle_sha256=bundle_sha, model=model, base=base, key=key)
        rec["conflict"][name] = scored(text); integ.update({"arm":name,"family":"related"}); rec["tool_integrity"].append(integ)
    if seed_id in CAL_IDS:
        for arm in PRIMARY:
            relation = "SAME_SUBJECT" if arm.startswith("SAME") else "OTHER_SUBJECT"
            refl = r if arm.endswith("+REFL") else None
            text, integ = tool_call(i1_prompt(artifact,refl,bundle_id,seed["related"]), relation=relation, bundle_id=bundle_id, bundle_sha256=bundle_sha, model=model, base=base, key=key)
            rec["calibration"][arm] = scored(text); integ.update({"arm":"CAL:"+arm,"family":"related"}); rec["tool_integrity"].append(integ)
    rec["finished_unix"] = time.time()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return rec


if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--seed",default="P003-001"); args=ap.parse_args(); run(args.seed)
