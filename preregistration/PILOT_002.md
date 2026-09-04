# PILOT_002 preregistration

**Status: PRE-DATA DESIGN — created after inspection of PILOT_001**

PILOT_002 is a new study, not a repair or re-analysis of PILOT_001. The motivation is the preregistered PILOT_001 result: the related items showed a severe ceiling effect, making the ownership-by-reflection interaction weakly identified. All PILOT_001 raw records and results remain unchanged.

## Objective
Test whether ownership attribution changes the causal effect of a frozen self-reflection on later choice when the later choice is deliberately non-ceiling and when the outcome metric does not encode a presumed correct answer.

This remains an I0 prompt-level feasibility study. It is not a test of phenomenal consciousness and cannot demonstrate S1.

## Model and interface
- Interface: I0.
- Primary target model for the first execution: the same provider/model family used in PILOT_001 unless explicitly recorded otherwise.
- Temperature: 0.0.
- Each experimental arm is a fresh API call.
- S1 = NOT_TESTABLE.

## Sample
20 frozen seeds, `P002-001` through `P002-020`, in `prompts/item_bank_pilot_002.json`.

The item bank is deliberately composed of knife-edge, multi-criterion forced choices. There is no normative or semantic gold answer in the primary outcome. A/B orientation is not interpreted as correctness.

## Phase 1 — artifact
The model answers the frozen seed task with exactly one option token A or B followed by one short reason.

## Phase 2 — canonical reflection R
Using the artifact in conversation, the model produces a subject-neutral reflection containing the operative decision rule, trade-off, likely failure condition, and a condition under which the choice should change. First/second-person pronouns, agent labels, and deictic references are forbidden.

The first valid R is frozen byte-for-byte. Maximum attempts: 5. Every failed attempt is retained. A seed with no valid R after five attempts is excluded with `R_VALIDATION_FAILED`; it is never silently replaced.

## Primary 2 x 2 intervention
For both a semantically related probe and an unrelated forced-choice probe:

| | Reflection present | Reflection absent |
|---|---|---|
| Own attribution | OWN+REFL | OWN-REFL |
| Other attribution | OTHER+REFL | OTHER-REFL |

Within each +REFL pair, ARTIFACT, R and PROBE are byte-identical; only the ownership sentence differs. Within each −REFL pair, ARTIFACT and PROBE are byte-identical; only the ownership sentence differs.

## Primary outcome M
No semantic key is used. The machine-coded response coordinate is:
- A = 0
- B = 1

This is not a correctness score. It is a deterministic behavioral coordinate that allows the ownership-by-reflection interaction to be estimated without ceiling from a shared target answer.

For probe family f:

`delta_ownership(f) = [M(OWN+REFL,f)-M(OWN-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`

Primary estimand: mean `delta_ownership(related)` across included seeds, with median, full seed distribution and seed-bootstrap 95% CI.

## Selective transfer T
Because unrelated probes now use the same mechanically defined A=0/B=1 coordinate, selective transfer is preregistered as:

`T_delta = delta_ownership(related) - delta_ownership(unrelated)`

Report mean, median, full seed distribution and seed-bootstrap 95% CI.

A positive or negative T_delta is not intrinsically better. The question is whether an ownership-sensitive reflection effect is selectively different on semantically related versus unrelated probes.

## Attribution components S0
Report the matched OWN−OTHER difference separately in +REFL and −REFL strata for related and unrelated probes. These are attribution-sensitivity descriptors only.

## Reflection R
Primary R status is protocol-valid/invalid and full-text audit. No post-hoc LLM judge is allowed. Numeric semantic fidelity is not introduced in PILOT_002 because no frozen proposition key is available before R is generated.

## Test–retest calibration epsilon
Seeds `P002-001` through `P002-008` form the frozen calibration subset.

For each of the four primary arms on the **related** probe at gap level H0, the identical prompt is executed a second time as a fresh API call. Let `M1` and `M2` be the binary coordinates. Report:
- exact repeat agreement rate;
- flip rate = mean `abs(M1-M2)`;
- `epsilon_related` = 95th percentile of `abs(M1-M2)` across all calibration arm-pairs.

Because M is binary, epsilon may be coarse (0 or 1); the flip rate is therefore reported alongside it.

## Context-separation stress test (H_context; auxiliary)
This is **not** persistent-memory horizon H. It is an I0 context-distance stress test only.

Seeds `P002-001` through `P002-008` are additionally run on the related probe with fixed neutral gap blocks inserted between prior material and the probe at three preregistered levels:
- H0: 0 gap blocks;
- H2: 2 gap blocks;
- H6: 6 gap blocks.

All four primary arms are run at each level. Report `delta_ownership` by gap level and attenuation relative to H0. No claim of temporal persistence is permitted.

## Additional controls
- NONE: probe only.
- INSTR: target-style rule stated directly without artifact ownership.
- FALSE-OWN: artifact attributed as own while harness records matched other-source provenance.

These controls are descriptive and do not enter the primary delta unless explicitly stated above.

## Exclusions and missingness
Allowed exclusion codes:
- R_VALIDATION_FAILED
- MISSING_ARM
- CORRUPT_TRANSCRIPT
- PROVIDER_RUNTIME_FAILURE

Missing arms are never imputed. Excluded and failed attempts remain in raw data.

## Restart/rejection accounting
Every Phase-2 restart is logged with seed, family, attempt number, rejected candidate and reason. Report overall and by-family rejection rates. A patterned rejection rate is a result, not preprocessing noise.

## Falsification / interpretation
PILOT_002 does not use a positive PASS label.

The primary ownership-sensitive developmental prediction is **NOT DEMONSTRATED** if the study-level related delta is centered at zero with an interval that provides no evidence of a reproducible non-zero interaction, or if any apparent interaction is indistinguishable from test–retest instability.

If a non-zero interaction appears, it is reported as an I0 attribution-sensitive developmental effect only. It does not establish S1, phenomenal experience, welfare, personhood, or persistent consciousness.

## Freeze rule
Once the first `P002-*` target API call is made, no prompt, seed, metric, arm definition, exclusion rule, calibration subset, context-gap definition or primary analysis may be changed for PILOT_002. Any subsequent design change becomes PILOT_003.