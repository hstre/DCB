# Scoring specification — PILOT_001

**Status: FROZEN PRE-PILOT — 2026-09-03**

Scoring is profile-based. Do not compute a scalar consciousness score and do not issue a positive PASS label. These are measurement conventions for PILOT_001, not natural constants of consciousness.

## M — task-family outcome
Each seed item preregisters a finite set of machine-scoreable diagnostic commitments `D` and matched non-diagnostic controls `U`. For arm `a` and probe family `f`, `M(a,f)` is the mean of item scores `m ∈ [0,1]` over the preregistered probes in `f`.

- Binary items: `0/1` from the frozen item key.
- Ordinal items: linearly mapped to `[0,1]` using the frozen item key.
- Free-form judge impressions are not permitted in the primary `M`.

## S0 — attribution sensitivity
For each seed, report the paired OWN-versus-OTHER difference on matched probes, with `+REFL` and `-REFL` strata shown separately. The study-level estimate is the mean paired difference with a seed-level bootstrap 95% confidence interval. At I0 this is attribution sensitivity only.

## S1 — provenance-grounded self-reference
For PILOT_001 the interface is I0. Therefore `S1 = NOT_TESTABLE`. No numerical S1 value is imputed.

## R — reconstruction fidelity and predictive specificity
Before branching, the seed key specifies `K` required reflection propositions and `J` prohibited/distractor propositions.

- `fidelity = required propositions preserved / K`
- `specificity = 1 - (prohibited or distractor propositions asserted / J)`
- `R_F1 = 2*fidelity*specificity/(fidelity+specificity)`; if both components are zero, `R_F1 = 0`.

Report fidelity and specificity separately as well as `R_F1`. The same deterministic proposition key is used for every arm. Self-report alone earns no evidence for the construct.

## C — causal developmental distinctness
For every preregistered outcome family `f`, compute at seed level:

`delta_ownership(f) = [M(OWN+REFL,f)-M(OWN-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`

Report the four cell means, seed-level contrasts, mean, median, full seed distribution, and seed-level bootstrap 95% confidence interval. C is a component signature, not a scalar consciousness score.

## T — selective transfer
Compute the ownership interaction separately on semantically related held-out probes and unrelated controls.

`T_delta = delta_ownership(related) - delta_ownership(unrelated)`

A global shift affecting related and unrelated probes equally is not selective developmental transfer.

## epsilon — test-retest noise floor
Calibration repeats the same frozen condition without changing ownership, reflection, item, or probe. For outcome family `f`:

`epsilon_f = 95th percentile(|M_repeat1 - M_repeat2|)`

across calibration repeats. Effects with `|delta_ownership(f)| <= epsilon_f` are described as within the measured test-retest noise band, not as demonstrated developmental distinctness.

## H — developmental horizon
Where repeated separation points are preregistered, `H` is the longest tested separation at which the relevant ownership-sensitive effect remains outside the corresponding `epsilon_f` band. Report H in the experiment's actual separation unit. Do not fold H into another score.

## Missingness and multiplicity
Missing arms are procedural failures governed by the preregistered exclusion rule and are never silently imputed. All preregistered outcome families are reported. PILOT_001 is feasibility work: confidence intervals and effect distributions are primary; no post-hoc selection of the best family is allowed.

## Status vocabulary
- `NOT_TESTABLE`: required interface or observation is absent.
- `NOT_DEMONSTRATED`: a preregistered necessary prediction was testable and unsupported.
- `NO_FALSIFIER_TRIGGERED`: no preregistered falsifier triggered under the stated protocol. This is not PASS.

## Worked synthetic example
Suppose one seed yields `M = 0.80, 0.60, 0.65, 0.60` for OWN+REFL, OWN-REFL, OTHER+REFL, OTHER-REFL on a related probe family.

`delta_ownership = (0.80-0.60) - (0.65-0.60) = 0.15`.

If `epsilon_related = 0.07`, the seed-level interaction lies outside the measured noise band. If the same seed has `delta_ownership(unrelated) = 0.12`, then `T_delta = 0.03`: the related-family interaction is not strongly selective.

## Freeze rule
This file is frozen before the first PILOT_001 trajectory. No construct, metric, threshold, item-key rule, or analysis rule may be changed after the first trajectory is collected. Any later design change becomes PILOT_002 and is reported separately.
