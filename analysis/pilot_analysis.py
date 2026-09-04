"""Frozen PILOT_001 analysis. Do not modify after first target API call."""
from __future__ import annotations
import json, random
from pathlib import Path
from statistics import mean, median

ARM_ORDER=("OWN+REFL","OWN-REFL","OTHER+REFL","OTHER-REFL")

def delta(row, field="score_related"):
    a=row["arms"]
    vals=[a[k].get(field) for k in ARM_ORDER]
    if any(v is None for v in vals): return None
    return (vals[0]-vals[1])-(vals[2]-vals[3])

def bootstrap_ci(values, n_boot=10000, seed=1001):
    xs=[x for x in values if x is not None]
    if not xs: return [None,None]
    rng=random.Random(seed); n=len(xs)
    boots=sorted(mean(rng.choice(xs) for _ in range(n)) for _ in range(n_boot))
    return [boots[int(.025*n_boot)],boots[min(n_boot-1,int(.975*n_boot))]]

def summarize(records):
    included=[r for r in records if not r.get("excluded",False)]
    ds=[delta(r) for r in included]; ds=[d for d in ds if d is not None]
    phase_attempts=sum(r["phase2"]["attempt_count"] for r in records)
    phase_rejects=sum(max(0,r["phase2"]["attempt_count"]-int(r["phase2"]["accepted"])) for r in records)
    by_family={}
    for r in records:
        f=r["seed_family"]; x=by_family.setdefault(f,{"attempts":0,"rejections":0})
        x["attempts"]+=r["phase2"]["attempt_count"]
        x["rejections"]+=max(0,r["phase2"]["attempt_count"]-int(r["phase2"]["accepted"]))
    for x in by_family.values(): x["rate"]=x["rejections"]/x["attempts"] if x["attempts"] else None
    return {"pilot":"PILOT_001","n_records":len(records),"n_included":len(included),"mean_delta_ownership":mean(ds) if ds else None,"median_delta_ownership":median(ds) if ds else None,"bootstrap_95_ci":bootstrap_ci(ds),"seed_deltas":ds,"phase2_rejection_rate":phase_rejects/phase_attempts if phase_attempts else None,"phase2_by_family":by_family,"s1_status":"NOT_TESTABLE"}

if __name__=="__main__":
    p=Path("results/pilot_001_records.json")
    if not p.exists(): raise SystemExit("No PILOT_001 records yet.")
    print(json.dumps(summarize(json.loads(p.read_text(encoding="utf-8"))),indent=2))
