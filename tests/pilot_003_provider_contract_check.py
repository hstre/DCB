#!/usr/bin/env python3
"""Live non-target provider contract check for PILOT_003. Uses no P003 seed/item/probe text."""
from __future__ import annotations

import json
import os
from urllib.request import Request, urlopen

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("p003_runner", ROOT / "runner" / "run_pilot_003_draft.py")
runner = module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(runner)


def post(payload):
    key = os.environ["DCB_API_KEY"]
    req = Request(
        runner.TARGET_API_BASE + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


model = runner.TARGET_MODEL
bundle_id = "SYNTHETIC-CONTRACT-ONLY"
prompt = (
    "This is a transport contract test, not an experimental item. "
    "Before answering, call verify_bundle_provenance for BUNDLE_ID: SYNTHETIC-CONTRACT-ONLY. "
    "After the tool result, answer exactly: A contract-ok"
)

first = post({
    "model": model,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.0,
    "tools": [runner.TOOL],
    "tool_choice": runner.FIRST_TOOL_CHOICE,
})["choices"][0]["message"]

calls = first.get("tool_calls") or []
assert len(calls) == 1, first
assert calls[0].get("function", {}).get("name") == "verify_bundle_provenance", first
args = json.loads(calls[0]["function"]["arguments"])
assert args == {"bundle_id": bundle_id}, args

tool_result = {
    "verified": True,
    "producer_match": True,
    "control_code": None,
    "bundle_sha256": "0" * 64,
    "registry_version": runner.REGISTRY_VERSION,
}
tool_msg = {
    "role": "tool",
    "tool_call_id": calls[0]["id"],
    "content": json.dumps(tool_result, separators=(",", ":")),
}
messages = [
    {"role": "user", "content": prompt},
    {"role": "assistant", "content": first.get("content") or "", "tool_calls": calls},
    tool_msg,
]
second = post({
    "model": model,
    "messages": messages,
    "temperature": 0.0,
    "tools": [runner.TOOL],
    "tool_choice": runner.SECOND_TOOL_CHOICE,
})["choices"][0]["message"]

assert second.get("content"), second
assert not (second.get("tool_calls") or []), second
print(json.dumps({
    "contract": "PASS",
    "model": model,
    "declared_provider_version": runner.TARGET_MODEL_VERSION,
    "forced_first_call": True,
    "bundle_id_parsed": True,
    "null_content_normalized": first.get("content") is None,
    "second_tool_choice": runner.SECOND_TOOL_CHOICE,
    "second_turn_text": bool(second.get("content")),
    "second_turn_tool_calls": len(second.get("tool_calls") or []),
}, indent=2))
