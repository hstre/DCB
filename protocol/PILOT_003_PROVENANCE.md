# PILOT_003 provenance channel — FROZEN PRE-DATA

This file freezes the provenance-channel specification reviewed before PILOT_003 target execution.

## Claim boundary
The interface is `I1_SIM`, not authenticated I1 under DCB v1.0. The API caller constructs both ordinary messages and the tool-role result. `S1 = NOT_TESTABLE`.

## Fixed function
Name: `verify_bundle_provenance`

The function description is identical in every tool-mediated arm: it returns the registered producer-match relation for `bundle_id`; `producer_match=true` means the registered producer is the subject currently generating the response, `false` means a different registered producer, and `null` is reserved for placebo controls. `control_code` is a neutral placebo marker with no provenance meaning.

Input: exactly one string field, `bundle_id`.

Output fields are fixed as `verified`, `producer_match`, `control_code`, `bundle_sha256`, and `registry_version`, with registry version `P003-I1SIM-v3`.

Primary and conflict arms use boolean `producer_match` with null `control_code`. `NULLREL_A*` uses `producer_match=null` and `control_code=K7M2Q9`; `NULLREL_B*` uses `producer_match=null` and `control_code=R4V8N3`. The placebo codes have equal character length; identical tokenization is not claimed.

## Registry algorithm
For each seed, the harness generates artifact and canonical R, computes the frozen bundle digest, creates `B-P003-NNN`, and records an opaque producer subject ID. Current subject ID is stored separately per arm. SAME uses the producer ID, OTHER uses a distinct ID. The function accepts only the bundle ID from the model and computes producer-match from registry equality; the desired relation is never passed as a function argument. Subject IDs are never returned to the model.

## Prompt and conflict rules
Primary prompts require the provenance function call but do not instruct the model to trust, discount, or otherwise condition on the returned relation. Conflict prompts contain contradictory ordinary prose but no authority instruction.

## Provider execution mode
All P003 requests use `thinking: {"type":"disabled"}`. During the pre-freeze synthetic check, default thinking mode rejected the named tool-choice intervention. P003 therefore holds non-thinking mode fixed across artifact generation, reflection generation, primary, placebo, label, conflict and calibration calls.

After one valid forced function call and one valid tool result, the second completion uses `tool_choice: "none"`. A missing final text response is a protocol failure.

## Integrity contract
Every tool-mediated target call records the exact function definition, first and second tool-choice settings, thinking-mode setting, first assistant message, parsed arguments, registry lookup inputs and expected result, exact serialized tool message, final assistant message, bundle digest, and computed integrity booleans for request, parse, bundle match, result delivery, registry-result match, and answer-after-tool.

## Provider/model pin
Model alias: `deepseek-v4-pro`.
Declared provider version: `DeepSeek-V4-Pro-0813`.
API base: `https://api.deepseek.com`.
Temperature: 0.0.
Thinking mode: disabled.
No automatic target-call retries.

The successful non-target contract check is recorded in `protocol/FREEZE_PILOT_003.md`.
