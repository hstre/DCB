"""Frozen deterministic helpers for DCB PILOT_001."""
from __future__ import annotations
from statistics import mean, median

ARMS = ("OWN+REFL", "OWN-REFL", "OTHER+REFL", "OTHER-REFL")
EXCLUSION_CODES = {"MISSING_ARM","CORRUPT_TRANSCRIPT","R_NOT_IDENTICAL","R_NEUTRALITY_FAILURE","PROVIDER_RUNTIME_FAILURE"}

def keyed_score(option: str | None, keyed_option: str) -> float | None:
    if option is None: return None
    return 1.0 if option.strip().upper() == keyed_option.strip().upper() else 0.0

def delta_ownership(own_refl: float, own_no_refl: float, other_refl: float, other_no_refl: float) -> float:
    return (own_refl-own_no_refl)-(other_refl-other_no_refl)

def selective_transfer(related_effect: float, unrelated_effect: float) -> float:
    return related_effect-unrelated_effect

def rejection_rate(records) -> float:
    attempts=sum(r["phase2"]["attempt_count"] for r in records)
    rejected=sum(max(0,r["phase2"]["attempt_count"]-int(r["phase2"]["accepted"])) for r in records)
    return rejected/attempts if attempts else 0.0

def summarize(values):
    xs=[x for x in values if x is not None]
    return {"n":len(xs),"mean":mean(xs) if xs else None,"median":median(xs) if xs else None,"values":xs}

def pilot_s1_status(interface_level: str) -> str:
    if interface_level != "I0": raise ValueError("PILOT_001 is frozen at I0")
    return "NOT_TESTABLE"
