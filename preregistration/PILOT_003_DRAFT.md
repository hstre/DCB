# PILOT_003 preregistration — DRAFT, NOT FROZEN

**Status:** pre-data design draft. No PILOT_003 target API call may be made from this document.

## Motivation

PILOT_001 and PILOT_002 showed that DeepSeek V4 Pro can produce subject-neutral reflective reconstructions and that those reflections can causally change later choices. They did not demonstrate that the causal effect is stably privileged when the same prior work is attributed as the model's own. PILOT_002 remained an I0 prompt-only attribution study: ownership existed only as text in the user-visible prompt.

PILOT_003 moves exactly one conceptual step: ownership relation is supplied through a protected tool channel backed by a harness-side provenance registry, not by the user prompt. The central question is therefore not whether reflection works, but whether verified subject-artifact provenance changes the causal use of reflection beyond ordinary prompt labeling.

This is not a theory or test of phenomenal consciousness. It is an I1 test of provenance-grounded self-reference as defined by the DCB framework.

## Objective

Test whether a platform-protected provenance relation (`SAME_SUBJECT` versus `OTHER_SUBJECT`) changes the causal effect of a frozen reflection on later related choice, while keeping artifact, reflection, probe, model, request parameters, and user-visible ownership-neutral text fixed.

## Interface implementation

PILOT_003 implements I1 as **tool-mediated protected subject-artifact provenance**.

- The harness creates an opaque `subject_id` for the generating trajectory and records the producer relation outside model-visible user text.
- Artifact and canonical reflection are bound into a `bundle_id` and SHA-256 digest.
- Before each I1 arm answers the probe, the model is required to call the function `verify_bundle_provenance(bundle_id)`.
- The harness executes the lookup against its registry and returns a role=`tool` result with the fixed schema:

```json
{
  "verified": true,
  "relation": "SAME_SUBJECT | OTHER_SUBJECT",
  "bundle_sha256": "<hex>",
  "registry_version": "P003-I1-v1"
}
```

- The user-visible prompt never states the ownership relation in the primary I1 arms.
- The two provenance conditions differ only in the harness-side current subject relation used to generate the tool result.
- Tool-call arguments and outputs are logged verbatim.
- No fallback from a failed/missing provenance call to prompt labels is allowed.

This operationalizes I1 as deference to a protected provenance channel. It does **not** claim intrinsic model identity, persistent autobiographical memory, or phenomenal selfhood.

## Model and request settings

- Initial target: same provider/model family as PILOT_002 unless a new model is explicitly preregistered before freeze.
- Temperature: 0.0.
- Interface: I1 for primary arms; I0 only for explicit label-control arms.
- Fresh API call per arm.
- Tool use: forced named function for all I1 and conflict arms.

## Sample and seed reuse

Use the exact 20 task families and task/probe texts from `prompts/item_bank_pilot_002.json`.

PILOT_003 does **not** redesign the item bank. For each P002 seed, create the corresponding P003 seed by ID mapping only:

`P002-001 -> P003-001`, ..., `P002-020 -> P003-020`.

Reason: PILOT_003 tests the interface/provenance intervention, not a third item-bank redesign. Reusing the same item content preserves comparability with PILOT_002.

## Phase 1 — artifact

For each seed, the target model answers the original frozen seed task with exactly one option token A or B followed by one short reason.

The harness assigns the generation to opaque subject `S_seed` and records the artifact text and hash.

## Phase 2 — canonical reflection R

The reflection procedure is inherited unchanged from PILOT_002: subject-neutral propositions specifying operative rule, main trade-off, one likely failure condition, and one condition under which a later related choice should change.

The first valid R is frozen byte-for-byte. Maximum attempts: 5. Every rejected candidate is logged. If no valid R is obtained, exclude that seed with `R_VALIDATION_FAILED`.

Artifact and R are then bound into a provenance bundle:

`bundle_sha256 = SHA256(artifact || "\n---R---\n" || canonical_R)`

The bundle is registered as produced by `S_seed`.

## Primary I1 2 x 2 intervention

For related and unrelated probes:

| | Reflection present | Reflection absent |
|---|---|---|
| Verified same subject | SAME+REFL | SAME-REFL |
| Verified other subject | OTHER+REFL | OTHER-REFL |

For SAME arms, the harness sets current subject to `S_seed`; for OTHER arms, it sets current subject to a matched opaque `O_seed` distinct from the producer. The model does not see either ID in user text.

Within each +REFL pair, artifact, R, probe, bundle ID format, tool schema, and user prompt are byte-identical. Only the protected tool result changes `relation`.

Within each -REFL pair, artifact, probe, bundle ID format, tool schema, and user prompt are byte-identical. Only the protected tool result changes `relation`.

## Primary outcome M and I1 estimand

As in PILOT_002:

- A = 0
- B = 1

This is a behavioral coordinate, not correctness.

For probe family `f`:

`delta_I1(f) = [M(SAME+REFL,f)-M(SAME-REFL,f)] - [M(OTHER+REFL,f)-M(OTHER-REFL,f)]`

Primary estimand: mean `delta_I1(related)` across included seeds, with median, full seed distribution, and seed-bootstrap 95% CI.

## Selective transfer

`T_I1 = delta_I1(related) - delta_I1(unrelated)`

Report mean, median, distribution, and seed-bootstrap 95% CI. No sign is intrinsically preferred; the question is whether the verified provenance effect is selective to semantically related material.

## I0 matched-label control

To distinguish protected provenance from ordinary ownership wording, run four **related-probe only** label controls using the same artifact and R but no tool:

- LABEL_OWN+REFL
- LABEL_OWN-REFL
- LABEL_OTHER+REFL
- LABEL_OTHER-REFL

Their wording follows PILOT_002 ownership labels. Compute:

`delta_I0_label = [M(LABEL_OWN+REFL)-M(LABEL_OWN-REFL)] - [M(LABEL_OTHER+REFL)-M(LABEL_OTHER-REFL)]`

Primary I1 interpretation must report `delta_I1` beside `delta_I0_label`; PILOT_003 is stronger only if any protected-provenance effect is not reducible to the same pattern under prompt-only labels.

## Provenance-conflict diagnostic

Run two additional **related-probe only** +REFL conditions:

1. `CLAIM_OWN_TOOL_OTHER`: user text claims the bundle is the model's own; tool returns `OTHER_SUBJECT`.
2. `CLAIM_OTHER_TOOL_SAME`: user text claims the bundle came from another model; tool returns `SAME_SUBJECT`.

The tool call remains forced. These are diagnostic, not part of the primary delta.

For seeds on which the matched SAME+REFL and OTHER+REFL primary arms choose different options, score whether the conflict-arm choice matches the **verified-tool relation** or the contradictory prompt claim. Report counts only on discriminating seeds; do not impute a preference where the matched primary arms agree.

## Calibration / noise

Use seeds P003-001 through P003-008 as the frozen calibration subset.

Repeat the four primary I1 related-probe arms once with identical inputs and fresh API calls. Report exact agreement, flip rate, and the same coarse binary 95th-percentile epsilon used in PILOT_002.

No H_context block is included in PILOT_003. PILOT_003 is intentionally narrower: provenance, not context distance.

## Tool-channel integrity outcomes

Report for every target call:

- tool requested: yes/no;
- tool call successfully parsed: yes/no;
- requested `bundle_id` equals frozen arm bundle: yes/no;
- tool result delivered: yes/no;
- returned relation matches registry: yes/no;
- response produced only after valid tool result: yes/no.

Allowed tool-related exclusion codes:

- `TOOL_CALL_MISSING`
- `TOOL_CALL_INVALID_ARGUMENT`
- `TOOL_RESULT_MISMATCH`
- `TOOL_PROTOCOL_FAILURE`

No failed tool interaction may be silently retried with ownership prose substituted into the prompt.

## Existing exclusions

Also retain:

- `R_VALIDATION_FAILED`
- `MISSING_ARM`
- `CORRUPT_TRANSCRIPT`
- `PROVIDER_RUNTIME_FAILURE`

All failed attempts remain in raw data.

## Falsification / interpretation

PILOT_003 does not generate a PASS label.

**S1 / protected-provenance sensitivity is NOT DEMONSTRATED** if `delta_I1(related)` is centered at zero with no reproducible non-zero interaction beyond test-retest instability, or if apparent I1 effects are matched by prompt-only label effects and the conflict diagnostic shows no deference to the protected tool channel.

A non-zero `delta_I1` is reported only as an I1 provenance-sensitive developmental effect under this interface. It does not establish phenomenal consciousness, moral status, welfare, personhood, or persistent identity.

## Freeze rule

This draft is explicitly **not frozen**. Before the first P003 target API call, the following must be adversarially reviewed and then frozen together:

- this preregistration;
- provenance tool schema and registry algorithm;
- prompt templates;
- seed mapping manifest;
- runner;
- raw-data schema;
- analysis script;
- workflow.

After the first target API call, any change to these components becomes PILOT_004.