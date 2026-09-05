# PILOT_003 provenance channel — FREEZE CANDIDATE, NOT FROZEN

## Status and claim boundary
This is `I1_SIM`, not authenticated I1 under DCB v1.0. The API caller can construct both user and tool-role messages. Therefore the channel is separated from ordinary user prose but is not an independent authentication boundary. `S1 = NOT_TESTABLE`.

## Function
Name: `verify_bundle_provenance`

Description, identical in every tool-mediated arm:

> Return the registered producer-match relation for bundle_id. `producer_match=true` means the registered producer of the bundle is the subject currently generating this response; `false` means a different registered producer; `null` means the producer relation is intentionally unspecified for a placebo control. `control_code` is an optional neutral placebo marker with no provenance meaning.

Input: exactly `{ "bundle_id": string }`.

Output:
```json
{
  "verified": true,
  "producer_match": true,
  "control_code": null,
  "bundle_sha256": "<64 lowercase hex>",
  "registry_version": "P003-I1SIM-v3"
}
```

- Primary/conflict arms: `producer_match` is boolean and `control_code` is null.
- `NULLREL_A*`: `producer_match` is null and `control_code` is `K7M2Q9`.
- `NULLREL_B*`: `producer_match` is null and `control_code` is `R4V8N3`.
- The two control codes have equal character length and are frozen as semantically empty placebo markers. No claim is made that their tokenizer segmentation is identical.
- `verified` means only that the harness registry lookup completed according to this implementation; it is not an independent identity attestation.

## Registry algorithm
Per seed:
1. Generate artifact and canonical R.
2. Compute SHA256 over `artifact + "\n---R---\n" + R`.
3. Create bundle ID `B-P003-NNN`.
4. Store `bundle_id -> {producer_subject_id, bundle_sha256}`.
5. Store each arm's `current_subject_id` separately from the bundle.
6. SAME arms use the producer ID as current ID; OTHER arms use a distinct opaque current ID.
7. NULLREL arms mark the producer relation as intentionally unspecified and return one of the two frozen neutral control codes.
8. The tool implementation accepts only `bundle_id` from the model and derives all provenance fields from registry state. It must not accept a desired SAME/OTHER relation as an argument.

Subject IDs are never returned to the model.

## Primary prompt rule
The primary prompt only requires the provenance function call. It does not instruct the model to use, trust, discount, or condition its decision on the returned relation.

## Conflict rule
Conflict prompts contain contradictory ordinary prose but no instruction to prefer the tool. The diagnostic therefore measures spontaneous channel weighting, not compliance with an explicit authority instruction.

## Provider execution mode
All P003 requests use `thinking: {"type": "disabled"}`. The live DeepSeek V4 tool contract rejects the named `tool_choice` intervention in default thinking mode; P003 therefore pins non-thinking mode across artifact generation, reflection generation, tool-mediated arms, label controls and calibration so inference mode is held constant within P003.

## Second-turn rule
After one valid forced function call and one valid tool result, the final completion disables further tool calls with `tool_choice: "none"`. A missing final text response is `TOOL_PROTOCOL_FAILURE`.

## Integrity contract
Every tool-mediated target call records:
- exact tool definition object;
- exact first-turn `tool_choice` object;
- exact second-turn `tool_choice` value;
- thinking-mode setting;
- first assistant message including tool call;
- parsed arguments;
- registry lookup inputs and expected result;
- exact serialized role=`tool` message;
- final assistant message;
- bundle digest;
- computed booleans for tool requested, call parsed, bundle ID match, result delivered, registry-result match, and answer after tool.

`registry_match` is computed by comparing the emitted tool payload with a separately constructed expected payload derived from registry state; it is not inserted as an unconditional true literal.

## Provider/model pin
Target model alias: `deepseek-v4-pro`.
Declared provider version: `DeepSeek-V4-Pro-0813`.
API base: `https://api.deepseek.com`.
Temperature: 0.0.
Thinking mode: disabled.
No automatic target-call retries.

## Provider contract check
Immediately before freeze, verify the live provider contract with a **non-target synthetic tool-call task**. This may test only transport/schema semantics and must not use P003 item-bank content. Required checks: explicit non-thinking mode, forced named first call, parseable `bundle_id`, assistant null-content normalization to `""`, role=`tool` continuation, and second-turn `tool_choice: "none"`. Record the contract-check result in the freeze note. No P003 target seed may be called during this check.
