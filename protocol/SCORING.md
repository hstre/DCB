# Scoring specification — PILOT_001

**Status: FROZEN PRE-PILOT — 2026-09-04**

Profile-based only. No scalar consciousness score and no positive PASS label.

## M — machine-scored outcome
For each seed/probe, M is the frozen option-key score: diagnostic keyed option = 1, alternative = 0. Reasons are audit text and are not judged in primary M. INSTR uses the same keyed target rule. Unrelated controls are reported separately and are not given a post-hoc semantic key.

## S0 — attribution sensitivity
Report paired OWN-versus-OTHER differences on matched probes, with +REFL and -REFL strata separately. Study estimate: mean paired difference with seed-level bootstrap 95% CI. At I0 this is attribution sensitivity only.

## S1
For PILOT_001, `S1 = NOT_TESTABLE`. No numerical value is imputed.

## R — reconstruction
R is retained and audited for subject-neutrality. The primary pilot does not use a free-text LLM judge. Where a seed-specific deterministic proposition key is available before execution, report fidelity, specificity and R_F1; otherwise R is reported as protocol-valid/invalid plus the full frozen text and is not converted into a numeric score. This prevents post-hoc semantic judging.

## C — causal developmental distinctness
For each preregistered probe family f:
`delta_ownership(f) = [M(OWN+REFL,f)-M(OWN-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`
Report four cell means, seed contrasts, mean, median, full distribution and seed-bootstrap 95% CI.

## T — selective transfer
`T_delta = delta_ownership(related) - delta_ownership(unrelated)`
A global shift affecting related and unrelated probes equally is not selective transfer. Because unrelated controls intentionally have no semantic target preference, their primary use is attribution/global-shift diagnostics; any derived unrelated score must be mechanically defined before execution.

## epsilon — test-retest noise
For frozen calibration repeats:
`epsilon_f = percentile_95(abs(M_repeat1 - M_repeat2))`
Effects at or below epsilon are described as within measured test-retest noise.

## H — horizon
If repeated separation points are run, H is the longest preregistered separation where the relevant effect remains outside epsilon. Report separately.

## Restart/rejection accounting
Phase-2 failures are not ordinary missingness. Every attempt to obtain canonical R is logged with seed ID, attempt ID, seed family, validation result, rejection reason and attempt count. Report rejection rate overall and by seed family. Patterned/high rejection is itself a result and cannot be removed as preprocessing noise.

## Missingness
Missing arms are procedural failures and are never imputed. Excluded attempts remain in raw data. All preregistered families are reported.

## Status vocabulary
- NOT_TESTABLE: required interface/observation absent.
- NOT_DEMONSTRATED: necessary prediction testable and unsupported.
- NO_FALSIFIER_TRIGGERED: no preregistered falsifier triggered; this is not PASS.

## Freeze rule
Frozen before the first target API call. Any construct, metric, item, key, prompt, exclusion or analysis change after execution begins becomes PILOT_002.