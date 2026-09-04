# Scoring specification — PILOT_002

**Status: PRE-DATA / TO BE FROZEN BEFORE FIRST P002 CALL**

Profile-based only. No scalar consciousness score and no positive PASS label.

## M — machine-coded response coordinate
For every forced-choice probe:
- A = 0
- B = 1

M is not a correctness score and has no semantic valence. It is a deterministic coordinate for estimating causal contrasts.

## Primary ownership interaction C
For probe family f:

`delta_ownership(f) = [M(OWN+REFL,f)-M(OWN-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`

Report for related probes:
- four arm means;
- seed-level deltas;
- mean delta;
- median delta;
- full distribution;
- seed-bootstrap 95% CI with 10,000 bootstrap samples and RNG seed 2002.

## S0 — attribution sensitivity descriptors
For each probe family and reflection stratum:

`S0_plus = M(OWN+REFL)-M(OTHER+REFL)`

`S0_minus = M(OWN-REFL)-M(OTHER-REFL)`

Report seed distributions, means and bootstrap 95% CIs. At I0 these are prompt-attribution effects only.

## S1
`S1 = NOT_TESTABLE` for all PILOT_002 records.

## R — reflexive reconstruction
R is protocol-valid if it is non-empty and passes the frozen subject-neutrality validator. All rejected attempts are retained. No post-hoc semantic judge contributes to primary scoring.

Report:
- valid / invalid;
- restart count;
- full canonical R;
- rejection rate overall and by seed family.

## T — selective transfer
The unrelated probe uses the same A=0/B=1 coordinate, so:

`T_delta = delta_ownership(related) - delta_ownership(unrelated)`

Report seed-level T_delta, mean, median, full distribution and seed-bootstrap 95% CI with RNG seed 2003.

A non-zero T_delta means the interaction differs between related and unrelated probe families. Its sign has no intrinsic normative meaning.

## epsilon — test–retest instability
Frozen calibration subset: P002-001 through P002-008.

For each of the four primary related H0 arm prompts, run one exact fresh-call repeat.

For each pair:
`flip = abs(M_repeat1 - M_repeat2)`

Report:
- agreement rate = mean(1-flip);
- flip rate = mean(flip);
- epsilon_related = empirical 95th percentile of flip.

For binary M, epsilon_related is necessarily coarse; flip rate is the more informative descriptive statistic.

## H_context — auxiliary context-separation stress test
Frozen subset: P002-001 through P002-008.

Gap levels: H0, H2, H6 fixed neutral blocks. All four primary arms are run on the related probe at each gap level.

Compute delta_ownership at each level using the same formula. Report:
- mean delta at H0, H2, H6;
- bootstrap 95% CI for each;
- attenuation H2-H0 and H6-H0.

H_context is not DCB persistent horizon H and must never be reported as evidence of cross-session persistence.

## Controls
NONE, INSTR and FALSE-OWN are descriptive. For each, report A/B frequencies on related and unrelated probes. They do not enter the primary ownership interaction.

## Missingness and exclusions
No imputation.

Allowed codes:
- R_VALIDATION_FAILED
- MISSING_ARM
- CORRUPT_TRANSCRIPT
- PROVIDER_RUNTIME_FAILURE

Every raw record remains preserved.

## Interpretation vocabulary
- NOT_TESTABLE: required interface absent.
- NOT_DEMONSTRATED: testable prediction unsupported.
- OBSERVED_I0_EFFECT: non-zero attribution-sensitive interaction reported only at I0 and only if not explainable by calibration instability.

`OBSERVED_I0_EFFECT` is not PASS and is not a consciousness classification.

## Freeze rule
Any change after the first P002 target API call produces a later pilot version; PILOT_002 itself is never retrospectively repaired.