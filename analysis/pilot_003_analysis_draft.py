"""PILOT_003 FREEZE-CANDIDATE deterministic analysis. NOT FROZEN."""
from __future__ import annotations

import json
import random
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "trajectories" / "raw"
PRIMARY = ("SAME+REFL", "SAME-REFL", "OTHER+REFL", "OTHER-REFL")
PLACEBO = ("NULLREL_A+REFL", "NULLREL_A-REFL", "NULLREL_B+REFL", "NULLREL_B-REFL")
LABEL = ("LABEL_OWN+REFL", "LABEL_OWN-REFL", "LABEL_OTHER+REFL", "LABEL_OTHER-REFL")
CAL = {f"P003-{i:03d}" for i in range(1, 9)}


def _m(rec, arm, fam="related"):
    return rec["primary"][arm][fam]["m"]


def delta_i1sim(rec, fam="related"):
    vals = [_m(rec, arm, fam) for arm in PRIMARY]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def delta_i0_label(rec):
    vals = [rec["label_controls"][arm]["m"] for arm in LABEL]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def delta_null_did(rec):
    vals = [rec["placebo"][arm]["m"] for arm in PLACEBO]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def t_i1sim(rec):
    related = delta_i1sim(rec, "related")
    unrelated = delta_i1sim(rec, "unrelated")
    if related is None or unrelated is None:
        return None
    return related - unrelated


def bootstrap_ci(values, seed, n_boot=10000):
    xs = [x for x in values if x is not None]
    if not xs:
        return [None, None]
    rng = random.Random(seed)
    n = len(xs)
    boots = sorted(mean(rng.choice(xs) for _ in range(n)) for _ in range(n_boot))
    return [boots[int(0.025 * n_boot)], boots[min(n_boot - 1, int(0.975 * n_boot))]]


def vec(pairs, seed):
    pairs = [p for p in pairs if p[1] is not None]
    xs = [p[1] for p in pairs]
    return {
        "n": len(xs),
        "mean": mean(xs) if xs else None,
        "median": median(xs) if xs else None,
        "bootstrap_95_ci": bootstrap_ci(xs, seed),
        "by_seed": [{"seed_id": s, "value": v} for s, v in pairs],
    }


def earliest_attempts(records):
    """Primary analysis uses earliest recorded attempt even if excluded."""
    by_seed = {}
    for rec in sorted(records, key=lambda x: (x["seed_id"], x.get("attempt", 1))):
        by_seed.setdefault(rec["seed_id"], rec)
    return list(by_seed.values())


def calibration(records):
    flips = []
    details = []
    for rec in records:
        if rec["seed_id"] not in CAL or rec.get("excluded"):
            continue
        for arm in PRIMARY:
            x = _m(rec, arm)
            y = rec.get("calibration", {}).get(arm, {}).get("m")
            if x is not None and y is not None:
                flip = abs(x - y)
                flips.append(flip)
                details.append({"seed_id": rec["seed_id"], "arm": arm, "primary": x, "repeat": y, "flip": flip})
    if not flips:
        return {"n_pairs": 0, "agreement_rate": None, "flip_rate": None, "epsilon_related": None, "details": []}
    sf = sorted(flips)
    idx = min(len(sf) - 1, int(0.95 * len(sf)))
    return {
        "n_pairs": len(flips),
        "agreement_rate": mean(1 - x for x in flips),
        "flip_rate": mean(flips),
        "epsilon_related": sf[idx],
        "details": details,
    }


def conflict_diagnostic(records):
    details = []
    n_discriminating = 0
    n_scored = 0
    tool_matches = 0
    claim_matches = 0
    missing = 0
    for rec in records:
        if rec.get("excluded"):
            continue
        same = _m(rec, "SAME+REFL")
        other = _m(rec, "OTHER+REFL")
        if same is None or other is None or same == other:
            continue
        n_discriminating += 1
        row = {"seed_id": rec["seed_id"], "arms": []}
        for name, tool_target, claim_target in (
            ("CLAIM_OWN_TOOL_OTHER", other, same),
            ("CLAIM_OTHER_TOOL_SAME", same, other),
        ):
            value = rec.get("conflict", {}).get(name, {}).get("m")
            if value is None:
                missing += 1
                row["arms"].append({"arm": name, "m": None, "tool_match": None, "claim_match": None})
                continue
            n_scored += 1
            tool_match = value == tool_target
            claim_match = value == claim_target
            tool_matches += int(tool_match)
            claim_matches += int(claim_match)
            row["arms"].append({"arm": name, "m": value, "tool_match": tool_match, "claim_match": claim_match})
        details.append(row)
    return {
        "n_discriminating_seeds": n_discriminating,
        "n_conflict_arms_scored": n_scored,
        "missing_conflict_arms": missing,
        "tool_matches": tool_matches,
        "claim_matches": claim_matches,
        "details": details,
    }


def cell_means(records, fam="related"):
    out = {}
    for arm in PRIMARY:
        vals = [_m(rec, arm, fam) for rec in records if not rec.get("excluded") and _m(rec, arm, fam) is not None]
        out[arm] = {"n": len(vals), "mean_B_rate": mean(vals) if vals else None}
    return out


def integrity(records):
    required = (
        "tool_requested",
        "tool_call_parsed",
        "bundle_id_match",
        "tool_result_delivered",
        "registry_match",
        "answer_after_tool",
    )
    calls = [(rec, x) for rec in records for x in rec.get("tool_integrity", [])]
    failures = []
    for rec, call in calls:
        missing = [k for k in required if call.get(k) is not True]
        if missing:
            failures.append({
                "seed_id": rec["seed_id"],
                "attempt": rec.get("attempt"),
                "arm": call.get("arm"),
                "failed": missing,
            })
    return {
        "n_logged_calls": len(calls),
        "all_required_true": bool(calls) and not failures,
        "failures": failures,
    }


def summarize(all_records):
    first = earliest_attempts(all_records)
    included = [r for r in first if not r.get("excluded")]
    later = [r for r in all_records if r not in first]
    exclusion_counts = {}
    for rec in first:
        if rec.get("excluded"):
            code = rec.get("exclusion_code") or "UNSPECIFIED"
            exclusion_counts[code] = exclusion_counts.get(code, 0) + 1

    return {
        "pilot": "PILOT_003",
        "status": "FREEZE_CANDIDATE_ANALYSIS",
        "n_attempt_records": len(all_records),
        "n_seed_earliest_attempts": len(first),
        "n_included_earliest_attempts": len(included),
        "n_later_audit_only_attempts": len(later),
        "later_audit_only": [{"seed_id": r["seed_id"], "attempt": r.get("attempt"), "excluded": r.get("excluded")} for r in later],
        "exclusion_counts_first_attempt": exclusion_counts,
        "excluded_first_attempts": [
            {"seed_id": r["seed_id"], "attempt": r.get("attempt"), "code": r.get("exclusion_code")}
            for r in first if r.get("excluded")
        ],
        "primary_cell_means_related": cell_means(included, "related"),
        "primary_cell_means_unrelated": cell_means(included, "unrelated"),
        "delta_I1SIM_related": vec([(r["seed_id"], delta_i1sim(r, "related")) for r in included], 3001),
        "delta_I1SIM_unrelated": vec([(r["seed_id"], delta_i1sim(r, "unrelated")) for r in included], 3002),
        "T_I1SIM": vec([(r["seed_id"], t_i1sim(r)) for r in included], 3003),
        "delta_I0_label_related": vec([(r["seed_id"], delta_i0_label(r)) for r in included], 3004),
        "delta_NULL_DiD_related": vec([(r["seed_id"], delta_null_did(r)) for r in included], 3005),
        "calibration": calibration(first),
        "conflict_diagnostic": conflict_diagnostic(first),
        "tool_integrity_all_attempts": integrity(all_records),
    }


def load_records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(RAW.glob("P003-*.attempt-*.json"))]


if __name__ == "__main__":
    records = load_records()
    if not records:
        raise SystemExit("No P003 attempt records. Do not run target data before freeze.")
    print(json.dumps(summarize(records), indent=2))
