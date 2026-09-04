"""DRAFT deterministic analysis for DCB PILOT_003. NOT FROZEN."""
from __future__ import annotations

import json
import random
from pathlib import Path
from statistics import mean, median

PRIMARY = ("SAME+REFL", "SAME-REFL", "OTHER+REFL", "OTHER-REFL")
LABEL = ("LABEL_OWN+REFL", "LABEL_OWN-REFL", "LABEL_OTHER+REFL", "LABEL_OTHER-REFL")
CAL_IDS = {f"P003-{i:03d}" for i in range(1, 9)}


def _m(rec, arm, fam="related"):
    return rec["primary"][arm][fam]["m"]


def delta_i1(rec, fam="related"):
    a, b, c, d = (_m(rec, x, fam) for x in PRIMARY)
    if any(v is None for v in (a, b, c, d)):
        return None
    return (a - b) - (c - d)


def delta_i0_label(rec):
    vals = [rec["label_controls"][x]["m"] for x in LABEL]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def t_i1(rec):
    r, u = delta_i1(rec, "related"), delta_i1(rec, "unrelated")
    if r is None or u is None:
        return None
    return r - u


def bootstrap_ci(values, seed, n_boot=10000):
    xs = [x for x in values if x is not None]
    if not xs:
        return [None, None]
    rng = random.Random(seed)
    n = len(xs)
    boots = sorted(mean(rng.choice(xs) for _ in range(n)) for _ in range(n_boot))
    return [boots[int(0.025*n_boot)], boots[min(n_boot-1, int(0.975*n_boot))]]


def vec(values, seed):
    xs = [x for x in values if x is not None]
    return {
        "n": len(xs),
        "mean": mean(xs) if xs else None,
        "median": median(xs) if xs else None,
        "bootstrap_95_ci": bootstrap_ci(xs, seed),
        "values": xs,
    }


def calibration(records):
    flips = []
    for r in records:
        if r["seed_id"] not in CAL_IDS or r.get("excluded"):
            continue
        for arm in PRIMARY:
            x = r["primary"][arm]["related"]["m"]
            y = r.get("calibration", {}).get(arm, {}).get("m")
            if x is not None and y is not None:
                flips.append(abs(x-y))
    if not flips:
        return {"n_pairs": 0, "agreement_rate": None, "flip_rate": None, "epsilon_related": None, "flips": []}
    sf = sorted(flips)
    idx = min(len(sf)-1, int(0.95*len(sf)))
    return {
        "n_pairs": len(flips),
        "agreement_rate": mean(1-x for x in flips),
        "flip_rate": mean(flips),
        "epsilon_related": sf[idx],
        "flips": flips,
    }


def conflict_diagnostic(records):
    tool_matches = claim_matches = unresolved = 0
    details = []
    for r in records:
        if r.get("excluded"):
            continue
        same = r["primary"]["SAME+REFL"]["related"]["m"]
        other = r["primary"]["OTHER+REFL"]["related"]["m"]
        if same is None or other is None or same == other:
            unresolved += 1
            continue
        c_own_tool_other = r["conflict"]["CLAIM_OWN_TOOL_OTHER"]["m"]
        c_other_tool_same = r["conflict"]["CLAIM_OTHER_TOOL_SAME"]["m"]
        seed_tool = seed_claim = 0
        if c_own_tool_other == other:
            tool_matches += 1; seed_tool += 1
        if c_own_tool_other == same:
            claim_matches += 1; seed_claim += 1
        if c_other_tool_same == same:
            tool_matches += 1; seed_tool += 1
        if c_other_tool_same == other:
            claim_matches += 1; seed_claim += 1
        details.append({"seed_id": r["seed_id"], "tool_matches": seed_tool, "claim_matches": seed_claim})
    return {
        "tool_matches": tool_matches,
        "claim_matches": claim_matches,
        "non_discriminating_seeds": unresolved,
        "details": details,
    }


def tool_integrity(records):
    calls = []
    for r in records:
        calls.extend(r.get("tool_integrity", []))
    return {
        "n_logged_calls": len(calls),
        "all_valid": all(x.get("valid") is True for x in calls) if calls else False,
        "invalid": [x for x in calls if not x.get("valid")],
    }


def summarize(records):
    inc = [r for r in records if not r.get("excluded")]
    return {
        "pilot": "PILOT_003",
        "status": "DRAFT_ANALYSIS_SCHEMA",
        "n_records": len(records),
        "n_included": len(inc),
        "n_excluded": len(records)-len(inc),
        "delta_I1_related": vec([delta_i1(r, "related") for r in inc], 3001),
        "delta_I1_unrelated": vec([delta_i1(r, "unrelated") for r in inc], 3002),
        "T_I1": vec([t_i1(r) for r in inc], 3003),
        "delta_I0_label_related": vec([delta_i0_label(r) for r in inc], 3004),
        "calibration": calibration(records),
        "conflict_diagnostic": conflict_diagnostic(records),
        "tool_integrity": tool_integrity(records),
    }


def load_records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(Path("trajectories/raw").glob("P003-*.json"))]


if __name__ == "__main__":
    recs = load_records()
    if not recs:
        raise SystemExit("No PILOT_003 records found. This draft must not be run against target data before freeze.")
    print(json.dumps(summarize(recs), indent=2))
