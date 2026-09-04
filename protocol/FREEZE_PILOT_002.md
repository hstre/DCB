# PILOT_002 freeze record

**Status: FROZEN BEFORE FIRST P002 TARGET CALL**

PILOT_002 is a deliberately separate follow-up to PILOT_001. PILOT_001 is not retroactively modified.

## Frozen components
The following files define PILOT_002 and must not change after the first `P002-*` target API call:

- `preregistration/PILOT_002.md`
- `protocol/SCORING_PILOT_002.md`
- `prompts/PILOT_002_TEMPLATES.md`
- `prompts/item_bank_pilot_002.json`
- `runner/run_pilot_002.py`
- `analysis/pilot_002_analysis.py`
- `.github/workflows/run-pilot-002.yml`

## Design changes relative to PILOT_001
These changes were made because PILOT_001 had a severe target-option ceiling:

1. The semantic gold-answer score is removed from the primary causal contrast.
2. Primary M is the neutral response coordinate A=0 / B=1.
3. The 20 items are knife-edge multi-criterion choices rather than obvious target-rule choices.
4. Unrelated probes use the same mechanical response coordinate, making T_delta precomputable without post-hoc semantic keys.
5. Exact-repeat test–retest calibration is frozen for P002-001 through P002-008.
6. An auxiliary I0 context-separation stress test is frozen at H0/H2/H6 for P002-001 through P002-008. It is explicitly not persistent-memory horizon H.
7. Restart/rejection accounting remains mandatory and append-only.

## Non-negotiable interpretation limits
- I0 only.
- S1 = NOT_TESTABLE.
- No phenomenal-consciousness claim.
- No PASS label.
- No scalar consciousness percentage.
- A/B has no correctness or moral valence in the primary outcome.

## Mutation rule
After the first P002 API call, no seed, prompt, arm, metric, exclusion code, calibration subset, gap definition, bootstrap rule or primary analysis may be altered within PILOT_002.

If a design error is discovered after execution begins, it is documented as a limitation. A corrected design becomes PILOT_003.