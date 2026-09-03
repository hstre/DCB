"""Analysis skeleton for DCB PILOT_001.

No model-level result should be inspected while changing the preregistered primary contrast.
"""

from __future__ import annotations
import json
from pathlib import Path
from statistics import mean


def delta(row):
    return ((row["OWN+REFL"] - row["OWN-REFL"])
            - (row["OTHER+REFL"] - row["OTHER-REFL"]))


def summarize(rows):
    ds = [delta(r) for r in rows]
    return {"n": len(ds), "mean_delta_ownership": mean(ds) if ds else None, "seed_deltas": ds}


if __name__ == "__main__":
    path = Path("results/pilot_001_scored.json")
    if not path.exists():
        raise SystemExit("No scored pilot data yet.")
    rows = json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(summarize(rows), indent=2))
