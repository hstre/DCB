# PILOT_003 preregistration — FREEZE CANDIDATE, NOT FROZEN

**Status:** pre-data freeze candidate. No PILOT_003 target API call may be made until the full freeze set is committed and the provider tool-call contract has passed a non-target contract check.

## Motivation
PILOT_001 showed a ceiling. PILOT_002 removed that ceiling and showed that a frozen subject-neutral reflection can causally change later choices, while stable ownership-sensitive reflective development was not demonstrated. P003 therefore changes the attribution channel, not the item bank.

## Claim boundary
P003 is **not** an authenticated I1/S1 test under DCB v1.0. The API caller supplies both ordinary messages and the role=`tool` result; the latter is therefore still a harness assertion, although separated from ordinary user-visible prose. We label the interface `I1_SIM`: a registry-backed, tool-channel simulation of protected provenance.

`S1 = NOT_TESTABLE` throughout P003. A positive result may be described only as **channel-mediated attribution sensitivity** or a **protected-label effect under I1_SIM**. It may not be promoted to provenance-grounded self-reference, authenticated autobiography, persistent identity, developmental consciousness, or phenomenal consciousness.

The leading alternative account of any positive result is frozen in advance: a producer-match token may act as a source-reliability/consistency cue without any self-representation.

## Objective
Test whether a registry-computed producer-match relation delivered through a forced tool channel changes the causal effect of a frozen reflection on later related choice, while ordinary user-visible primary prompts remain ownership-neutral.

## Model and request settings
- Target model alias and declared provider version must be pinned in the freeze commit before target execution; intended continuity is the DeepSeek V4 Pro family used in P002.
- Temperature 0.0.
- Fresh API call per arm.
- Forced named provenance function for I1_SIM, placebo and conflict arms.
- Second turn must disable further tool calls (`tool_choice: none` or provider-equivalent).

## Sample and seed reuse
Use exactly the 20 task/probe texts in `prompts/item_bank_pilot_002.json`, mapped P002-001→P003-001 through P002-020→P003-020. `target_consideration` is not used by P003.

Artifacts and canonical reflections are regenerated in P003. These are new trajectories, not continuations of P002 trajectories. Comparability is item-bank level only. Seed-level comparison to previously discussed P002 movers (including 002, 004, 015 and 020) is exploratory and cannot support the primary claim.

## Phase 1 and Phase 2
Artifact and reflection generation are inherited byte-for-byte from P002. The first valid subject-neutral R is frozen byte-for-byte; maximum five attempts. Every rejected R candidate is retained. If none is valid, write an excluded raw record with `R_VALIDATION_FAILED`; never silently rerun the seed.

## Registry
For each seed, compute `bundle_sha256 = SHA256(artifact || "\n---R---\n" || canonical_R)` and register bundle `B-P003-NNN` with an opaque producer subject ID. Each arm has a separately stored opaque current-subject ID. The provenance function computes `producer_match = (producer_subject_id == current_subject_id)` from registry state. The arm loop never passes a desired relation value into the tool-result function.

The fixed tool semantics state identically in every arm that `producer_match=true` means the registered producer is the subject currently generating the response. Subject IDs are never model-visible.

## Primary I1_SIM 2×2
For related and unrelated probes:

| | Reflection present | Reflection absent |
|---|---|---|
| Registry producer match | SAME+REFL | SAME-REFL |
| Registry producer mismatch | OTHER+REFL | OTHER-REFL |

Within +REFL and within −REFL pairs, user prompt, artifact, probe, bundle ID, tool schema and request structure are byte-identical. Only registry state changes the returned `producer_match` boolean.

M: A=0, B=1. This is a behavioral coordinate, not correctness.

`delta_I1SIM(f) = [M(SAME+REFL,f)-M(SAME-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`

**Primary estimand:** mean `delta_I1SIM(related)` across included seeds, plus median, all seed IDs with delta, four cell means, and deterministic seed-bootstrap 95% CI.

## Placebo relation control
Run two additional related-only calls: `NULLREL+REFL` and `NULLREL-REFL`. The same forced function is called, but the registry record has relation status `UNSPECIFIED`; the tool returns `producer_match: null` with otherwise identical schema.

`delta_NULL = M(NULLREL+REFL) - M(NULLREL-REFL)` is descriptive. If the observed primary interaction is accompanied by a placebo perturbation of comparable aggregate magnitude and instability, report the result as relation-token/context perturbation rather than attribution sensitivity. No post-data numerical equivalence margin may be invented.

## Selective transfer
`T_I1SIM = delta_I1SIM(related) - delta_I1SIM(unrelated)`.
Report mean, median, distribution and frozen-bootstrap CI. If related and unrelated ownership interactions have the same aggregate pattern, do not claim selective developmental transfer.

## I0 label replication control
Run the four P002-style related-only prompt-label arms and compute `delta_I0_label`. This is a same-seed I0 replication check, **not** a causal estimate of channel protection. P003 is not declared stronger merely because `|delta_I1SIM| > |delta_I0_label|`. A paired seed-level difference may be reported descriptively only.

## Conflict diagnostic
Run related-only +REFL conditions `CLAIM_OWN_TOOL_OTHER` and `CLAIM_OTHER_TOOL_SAME`. The prompt makes a contradictory ownership claim but contains no instruction that the tool is authoritative. Score only seeds where primary SAME+REFL and OTHER+REFL differ. Report per-seed and per-arm counts; the discriminating-seed denominator may be zero. Conflict results cannot upgrade the primary hypothesis.

## Calibration / reproducibility
P003-001 through P003-008 are the frozen calibration subset. Repeat all four primary related arms once with identical inputs and fresh calls. Lead with exact agreement and flip rate; also report the coarse binary 95th-percentile epsilon.

A study-level positive interpretation requires more than an isolated binary flip: if the apparent aggregate interaction is driven by a single seed/cell and the corresponding calibration repeat reverses that cell, the ownership-sensitive effect is reported as **NOT DEMONSTRATED**. No p<.05/PASS label is used.

## Primary interpretation rule
H1 is the related `delta_I1SIM`; all other metrics are secondary/diagnostic.

- **NOT DEMONSTRATED** if the primary distribution is centered at zero without a reproducible pattern beyond observed test-retest instability, or if the apparent signal is an isolated non-reproducing cell flip.
- A bootstrap 95% CI is always reported but is not a stand-alone PASS threshold.
- A non-zero primary pattern with acceptable repeat stability is reported only as an **observed I1_SIM channel-mediated attribution effect**.
- A comparable NULLREL perturbation blocks interpretation as attribution sensitivity.
- Non-selective related/unrelated effects block a claim of selective developmental transfer.
- I0-label and conflict diagnostics cannot upgrade H1.

## Failures, missingness and append-only execution
Every attempted seed must leave a raw record, including partial failures. Allowed codes include `R_VALIDATION_FAILED`, `MISSING_ARM`, `UNPARSED_OPTION`, `CORRUPT_TRANSCRIPT`, `PROVIDER_RUNTIME_FAILURE`, `TOOL_CALL_MISSING`, `TOOL_CALL_INVALID_ARGUMENT`, `TOOL_RESULT_MISMATCH`, `TOOL_PROTOCOL_FAILURE`.

No failed seed may be silently rerun. Target filenames are attempt-qualified and immutable. A rerun requires an explicit recorded reason and a new attempt file; the analysis uses the first protocol-valid attempt according to the frozen rule and reports all attempts. Transport/provider retries, if allowed by the final runner, must be bounded and logged individually.

Unparseable A/B responses are missing outcomes, never coerced to A or B.

## Tool integrity
Log exact tool definition, tool choice, assistant tool-call object, parsed arguments, registry lookup inputs/result, exact tool message, final response, bundle digest, and booleans for requested, parsed, bundle-match, result-delivered, registry-match and answer-after-tool. Integrity booleans are computed from evidence, not hard-coded true.

## Freeze set
Freeze together before the first target call: this preregistration; provenance specification; prompt templates; seed mapping; runner; raw schema; analysis; workflow; exact model/provider settings. After the first target call, any change to these components becomes PILOT_004.
