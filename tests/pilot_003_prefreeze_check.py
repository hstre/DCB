#!/usr/bin/env python3
"""Mechanical pre-freeze checks for PILOT_003. No provider or target calls."""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


runner = load_module("p003_runner", ROOT / "runner" / "run_pilot_003_draft.py")
analysis = load_module("p003_analysis", ROOT / "analysis" / "pilot_003_analysis_draft.py")


def block_after(markdown: str, heading: str) -> str:
    pattern = rf"^##+ {re.escape(heading)}\s*$.*?^```text\s*$\n(.*?)\n^```\s*$"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    if not match:
        raise AssertionError(f"prompt block not found: {heading}")
    return match.group(1)


def prompt_diff_check() -> None:
    md = (ROOT / "prompts" / "PILOT_003_PROMPTS_DRAFT.md").read_text(encoding="utf-8")
    vals = {"artifact": "ART", "canonical_r": "REFL", "bundle_id": "B-P003-999", "probe": "PROBE", "related_probe": "PROBE"}
    expected = {
        "Tool-mediated +REFL": runner.tool_prompt("ART", "REFL", "B-P003-999", "PROBE"),
        "Tool-mediated -REFL": runner.tool_prompt("ART", None, "B-P003-999", "PROBE"),
        "LABEL_OWN+REFL": runner.label_prompt("LABEL_OWN+REFL", "ART", "REFL", "PROBE"),
        "LABEL_OWN-REFL": runner.label_prompt("LABEL_OWN-REFL", "ART", "REFL", "PROBE"),
        "LABEL_OTHER+REFL": runner.label_prompt("LABEL_OTHER+REFL", "ART", "REFL", "PROBE"),
        "LABEL_OTHER-REFL": runner.label_prompt("LABEL_OTHER-REFL", "ART", "REFL", "PROBE"),
        "CLAIM_OWN_TOOL_OTHER": runner.conflict_prompt(True, "ART", "REFL", "B-P003-999", "PROBE"),
        "CLAIM_OTHER_TOOL_SAME": runner.conflict_prompt(False, "ART", "REFL", "B-P003-999", "PROBE"),
    }
    for heading, generated in expected.items():
        documented = block_after(md, heading).format(**vals)
        if documented != generated:
            raise AssertionError(f"prompt/runner diff for {heading}\nDOC={documented!r}\nRUN={generated!r}")
    forbidden = ("after the provenance result", "Treat the verified provenance", "SAME_SUBJECT", "OTHER_SUBJECT")
    for token in forbidden:
        if token in md:
            raise AssertionError(f"forbidden stale prompt token remains: {token}")
    assert runner.THINKING == {"type": "disabled"}


def base_record(seed_id: str, attempt: int, excluded: bool = False, code=None):
    primary = {
        "SAME+REFL": {"related": {"m": 1}, "unrelated": {"m": 1}},
        "SAME-REFL": {"related": {"m": 0}, "unrelated": {"m": 0}},
        "OTHER+REFL": {"related": {"m": 0}, "unrelated": {"m": 0}},
        "OTHER-REFL": {"related": {"m": 0}, "unrelated": {"m": 0}},
    }
    placebo = {
        "NULLREL_A+REFL": {"m": 1}, "NULLREL_A-REFL": {"m": 0},
        "NULLREL_B+REFL": {"m": 1}, "NULLREL_B-REFL": {"m": 0},
    }
    label = {arm: {"m": 0} for arm in analysis.LABEL}
    return {
        "pilot": "PILOT_003", "status": "FREEZE_CANDIDATE_EXECUTION",
        "seed_id": seed_id, "attempt": attempt, "source_seed": seed_id.replace("P003", "P002"), "family": "synthetic",
        "model": "deepseek-v4-pro", "model_version": "DeepSeek-V4-Pro-0813", "api_base": "https://api.deepseek.com",
        "request_parameters": {"temperature": 0.0, "thinking": {"type": "disabled"}}, "interface_level": "I1_SIM", "s1_status": "NOT_TESTABLE",
        "registry_version": "P003-I1SIM-v3", "excluded": excluded, "exclusion_code": code,
        "exclusion_detail": "synthetic" if excluded else None, "errors": [],
        "primary": primary, "placebo": placebo, "label_controls": label,
        "conflict": {"CLAIM_OWN_TOOL_OTHER": {"m": None}, "CLAIM_OTHER_TOOL_SAME": {"m": 1}},
        "calibration": {}, "tool_integrity": [], "started_unix": 1.0, "finished_unix": 2.0,
    }


def analysis_contract_check() -> None:
    included = base_record("P003-009", 1)
    excluded_first = base_record("P003-010", 1, True, "PROVIDER_RUNTIME_FAILURE")
    later_success = base_record("P003-010", 2)
    summary = analysis.summarize([included, excluded_first, later_success])
    assert summary["n_seed_earliest_attempts"] == 2
    assert summary["n_included_earliest_attempts"] == 1
    assert summary["n_later_audit_only_attempts"] == 1
    assert summary["exclusion_counts_first_attempt"] == {"PROVIDER_RUNTIME_FAILURE": 1}
    assert summary["conflict_diagnostic"]["n_discriminating_seeds"] == 1
    assert summary["conflict_diagnostic"]["n_conflict_arms_scored"] == 1
    assert summary["conflict_diagnostic"]["missing_conflict_arms"] == 1
    assert summary["delta_NULL_DiD_related"]["by_seed"] == [{"seed_id": "P003-009", "value": 0}]


def seed_map_check() -> None:
    mapping = runner.load_seed_map()
    assert len(mapping) == 20
    assert mapping["P003-001"] == "P002-001"
    assert mapping["P003-020"] == "P002-020"


def schema_check() -> None:
    try:
        import jsonschema
    except ImportError:
        return
    schema = json.loads((ROOT / "scoring" / "schema_pilot_003.json").read_text(encoding="utf-8"))
    jsonschema.validate(base_record("P003-009", 1), schema)
    jsonschema.validate(base_record("P003-010", 1, True, "PROVIDER_RUNTIME_FAILURE"), schema)


if __name__ == "__main__":
    prompt_diff_check()
    seed_map_check()
    analysis_contract_check()
    schema_check()
    print("PILOT_003 pre-freeze mechanical checks: PASS")
