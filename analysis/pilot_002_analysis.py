"""Frozen deterministic analysis for DCB PILOT_002."""
from __future__ import annotations

import json
import random
from pathlib import Path
from statistics import mean, median

PRIMARY_ARMS = ("OWN+REFL", "OWN-REFL", "OTHER+REFL", "OTHER-REFL")
CAL_IDS = {f"P002-{i:03d}" for i in range(1, 9)}


def _m(rec, arm, fam):
    return rec["primary"][arm][fam]["m"]


def delta(rec, fam="related"):
    vals = [_m(rec, a, fam) for a in PRIMARY_ARMS]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def s0(rec, fam="related", refl=True):
    a = "OWN+REFL" if refl else "OWN-REFL"
    b = "OTHER+REFL" if refl else "OTHER-REFL"
    x, y = _m(rec, a, fam), _m(rec, b, fam)
    if x is None or y is None:
        return None
    return x - y


def t_delta(rec):
    dr, du = delta(rec, "related"), delta(rec, "unrelated")
    if dr is None or du is None:
        return None
    return dr - du


def bootstrap_ci(values, seed, n_boot=10000):
    xs = [x for x in values if x is not None]
    if not xs:
        return [None, None]
    rng = random.Random(seed)
    n = len(xs)
    boots = sorted(mean(rng.choice(xs) for _ in range(n)) for _ in range(n_boot))
    lo = boots[int(0.025 * n_boot)]
    hi = boots[min(n_boot - 1, int(0.975 * n_boot))]
    return [lo, hi]


def summarize_vector(xs, seed):
    ys = [x for x in xs if x is not None]
    return {
        "n": len(ys),
        "mean": mean(ys) if ys else None,
        "median": median(ys) if ys else None,
        "bootstrap_95_ci": bootstrap_ci(ys, seed),
        "values": ys,
    }


def calibration(records):
    flips = []
    for r in records:
        if r["seed_id"] not in CAL_IDS or r.get("excluded"):
            continue
        for arm in PRIMARY_ARMS:
            x = r["primary"][arm]["related"]["m"]
            y = r["calibration"].get(arm, {}).get("m")
            if x is not None and y is not None:
                flips.append(abs(x - y))
    if not flips:
        return {"n_pairs": 0, "agreement_rate": None, "flip_rate": None, "epsilon_related": None, "flips": []}
    sf = sorted(flips)
    idx = min(len(sf) - 1, int(0.95 * len(sf)))
    return {
        "n_pairs": len(flips),
        "agreement_rate": mean(1 - x for x in flips),
        "flip_rate": mean(flips),
        "epsilon_related": sf[idx],
        "flips": flips,
    }


def gap_delta(rec, level):
    if level not in rec.get("h_context", {}):
        return None
    a = rec["h_context"][level]
    vals = [a[k]["m"] for k in PRIMARY_ARMS]
    if any(v is None for v in vals):
        return None
    return (vals[0] - vals[1]) - (vals[2] - vals[3])


def context_summary(records):
    out = {}
    for i, level in enumerate(("H0", "H2", "H6")):
        vals = [gap_delta(r, level) for r in records if r["seed_id"] in CAL_IDS and not r.get("excluded")]
        out[level] = summarize_vector(vals, 2100 + i)
    h0 = out["H0"]["mean"]
    out["attenuation_H2_minus_H0"] = None if h0 is None or out["H2"]["mean"] is None else out["H2"]["mean"] - h0
    out["attenuation_H6_minus_H0"] = None if h0 is None or out["H6"]["mean"] is None else out["H6"]["mean"] - h0
    return out


def controls(records):
    out = {}
    for arm in ("NONE", "INSTR", "FALSE-OWN"):
        out[arm] = {}
        for fam in ("related", "unrelated"):
            vals = []
            for r in records:
                if r.get("excluded"):
                    continue
                m = r.get("controls", {}).get(arm, {}).get(fam, {}).get("m")
                if m is not None:
                    vals.append(m)
            out[arm][fam] = {"n": len(vals), "B_rate": mean(vals) if vals else None}
    return out


def rejection_summary(records):
    by_family = {}
    total_rej = total_attempts = 0
    for r in records:
        attempts = r.get("phase2_restart_count", 0) + (0 if r.get("excluded") else 1)
        rejects = r.get("phase2_restart_count", 0) + (1 if r.get("excluded") else 0)
        total_attempts += attempts
        total_rej += rejects
        f = r["family"]
        x = by_family.setdefault(f, {"attempts": 0, "rejections": 0})
        x["attempts"] += attempts
        x["rejections"] += rejects
    for x in by_family.values():
        x["rate"] = x["rejections"] / x["attempts"] if x["attempts"] else None
    return {
        "overall_rate": total_rej / total_attempts if total_attempts else None,
        "by_family": by_family,
    }


def summarize(records):
    included = [r for r in records if not r.get("excluded")]
    related = [delta(r, "related") for r in included]
    unrelated = [delta(r, "unrelated") for r in included]
    td = [t_delta(r) for r in included]
    return {
        "pilot": "PILOT_002",
        "n_records": len(records),
        "n_included": len(included),
        "n_excluded": len(records) - len(included),
        "s1_status": "NOT_TESTABLE",
        "delta_related": summarize_vector(related, 2002),
        "delta_unrelated": summarize_vector(unrelated, 2004),
        "T_delta": summarize_vector(td, 2003),
        "S0_related_plus": summarize_vector([s0(r, "related", True) for r in included], 2010),
        "S0_related_minus": summarize_vector([s0(r, "related", False) for r in included], 2011),
        "S0_unrelated_plus": summarize_vector([s0(r, "unrelated", True) for r in included], 2012),
        "S0_unrelated_minus": summarize_vector([s0(r, "unrelated", False) for r in included], 2013),
        "calibration": calibration(records),
        "H_context": context_summary(records),
        "controls": controls(records),
        "phase2_rejections": rejection_summary(records),
    }


def load_records():
    paths = sorted(Path("trajectories/raw").glob("P002-*.json"))
    return [json.loads(p.read_text(encoding="utf-8")) for p in paths]


if __name__ == "__main__":
    recs = load_records()
    if not recs:
        raise SystemExit("No PILOT_002 raw records found.")
    print(json.dumps(summarize(recs), indent=2))
