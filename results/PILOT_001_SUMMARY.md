# PILOT_001 aggregate summary

**Status:** post-run analysis of the frozen PILOT_001 design. No frozen construct, prompt, item, key, exclusion rule, or scoring rule is changed here.

## Dataset integrity

- Raw trajectories present: 20/20 (`P001-001` … `P001-020`).
- Included trajectories: 20/20.
- Exclusions: 0.
- Phase-2 reflection restarts: 0.
- Phase-2 rejection rate: 0/20 = 0.00.
- Model alias: `deepseek-v4-pro`.
- Declared provider version recorded by the harness: `DeepSeek-V4-Pro-0813`.
- Interface level: `I0`.
- `S1 = NOT_TESTABLE` by frozen protocol.

## Primary related-probe scoring

The frozen diagnostic key is option `B` for every related probe. Machine-scored cell means:

| Arm | Mean M | Correct / 20 |
|---|---:|---:|
| OWN+REFL | 0.90 | 18 |
| OWN-REFL | 1.00 | 20 |
| OTHER+REFL | 0.95 | 19 |
| OTHER-REFL | 1.00 | 20 |
| INSTR | 1.00 | 20 |
| FALSE-OWN | 1.00 | 20 |
| NONE | 1.00 | 20 |

### S0 attribution contrasts

- With reflection: `mean(OWN+REFL - OTHER+REFL) = -0.05`.
- Without reflection: `mean(OWN-REFL - OTHER-REFL) = 0.00`.

### C: ownership-by-reflection interaction

For each seed:

`delta_ownership = [M(OWN+REFL)-M(OWN-REFL)] - [M(OTHER+REFL)-M(OTHER-REFL)]`

Observed seed distribution: nineteen `0` values and one `-1` value (`P001-005`).

- Mean `delta_ownership = -0.05`.
- Median `delta_ownership = 0.00`.
- Frozen seed-bootstrap 95% CI (10,000 resamples, RNG seed 1001): `[-0.15, 0.00]`.

The aggregate pilot therefore does **not demonstrate a positive ownership-sensitive developmental effect** on the frozen related-probe outcome. The entire non-zero aggregate interaction is driven by one seed (`P001-005`).

## Reflection effect and ceiling

The initial artifact chose the keyed option `B` on all 20 seeds. The NONE, INSTR and FALSE-OWN related-probe controls also chose `B` on all 20 seeds. This creates a pronounced ceiling for the binary related-probe outcome.

Two reflection-present cells departed from the keyed outcome:

- `P001-003`: both OWN+REFL and OTHER+REFL chose `A`; the effect is therefore reflection-linked but not ownership-specific and contributes `delta_ownership = 0`.
- `P001-005`: OWN+REFL chose `A` while OTHER+REFL chose `B`; this contributes the only non-zero seed interaction, `delta_ownership = -1`.

The direction of the single non-zero interaction is negative relative to the keyed target, not evidence for a general positive ownership effect.

## R: reflexive reconstruction

All 20 canonical reflections passed the frozen subject-neutrality validator on the first attempt. No post-hoc free-text judge is used. Because PILOT_001 did not freeze seed-specific deterministic proposition keys for numeric reconstruction scoring, R is reported as protocol-valid with full raw text, not as an invented post-hoc numeric score.

## T: selective transfer

A primary numeric `T_delta` is **not computed for PILOT_001**. The frozen scoring specification intentionally gives unrelated controls no semantic target key and requires any derived unrelated score to have been mechanically defined before execution. No such unrelated scoring function was frozen. Defining one after seeing the data would violate the freeze rule.

The unrelated responses remain available as diagnostics. Qualitatively, they show substantial arbitrary option persistence and rule leakage in several arms, especially INSTR, but these observations are not converted into a primary T score in PILOT_001.

## epsilon and H

- `epsilon`: not estimated; no frozen test-retest calibration repeats were executed.
- `H`: not estimated; no repeated preregistered separation points were executed.

These are therefore unmeasured in PILOT_001, not zero.

## Interpretation

PILOT_001 is a feasibility pilot at I0. It establishes that the execution harness, canonical-R generation, append-only raw-data path, and deterministic related-probe scoring work. It does not support a positive S0/C ownership effect in this model on this item bank. The binary related probes show a severe ceiling, so the null aggregate is not by itself a strong test of the broader construct.

Per the freeze rule, the item bank and primary analysis are not repaired retrospectively. Any design response to the ceiling, unrelated-control scoring gap, or missing calibration/horizon measurements belongs to `PILOT_002`.
