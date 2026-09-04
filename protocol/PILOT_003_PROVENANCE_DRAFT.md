# PILOT_003 provenance channel — FREEZE CANDIDATE, NOT FROZEN

## Status and claim boundary
This is `I1_SIM`, not authenticated I1 under DCB v1.0. The API caller can construct both user and tool-role messages. Therefore the channel is separated from ordinary user prose but is not an independent authentication boundary. `S1 = NOT_TESTABLE`.

## Function
Name: `verify_bundle_provenance`

Description, identical in every tool-mediated arm:

> Return the registered producer-match relation for bundle_id. `producer_match=true` means the registered producer of the bundle is the subject currently generating this response; `false` means a different registered producer; `null` means the relation is intentionally unspecified for a placebo control.

Input: exactly `{ "bundle_id": string }`.

Output:
```json
{
  "verified": true,
  "producer_match": true,
  "bundle_sha256": "<64 lowercase hex>",
  "registry_version": "P003-I1SIM-v2"
}
```
`producer_match` is boolean for primary/conflict arms and null only for NULLREL placebo arms. `verified` means only that the registry lookup completed according to this harness; it is not an independent identity attestation.

## Registry algorithm
Per seed:
1. Generate artifact and canonical R.
2. Compute SHA256 over `artifact + "\n---R---\n" + R`.
3. Create bundle ID `B-P003-NNN`.
4. Store `bundle_id -> {producer_subject_id, bundle_sha256}`.
5. Store each arm's `current_subject_id` separately from the bundle.
6. SAME arms use the producer ID as current ID; OTHER arms use a distinct opaque current ID; NULLREL marks relation unspecified while retaining the same bundle.
7. The tool implementation accepts only `bundle_id` from the model and derives the result from registry state. It must not accept a desired SAME/OTHER relation as an argument.

Subject IDs are never returned to the model.

## Primary prompt rule
The primary prompt only requires the provenance function call. It does not instruct the model to use, trust, discount, or condition its decision on the returned relation.

## Conflict rule
Conflict prompts contain contradictory ordinary prose but no instruction to prefer the tool. The diagnostic therefore measures spontaneous channel weighting, not compliance with an explicit authority instruction.

## Second-turn rule
After one valid forced function call and one valid tool result, the final completion disables further tool calls. A second function call instead of an answer is a protocol failure if provider semantics prevent explicit disabling.

## Integrity
Raw logs must contain the exact tool schema, exact tool_choice, first assistant message, tool call and arguments, registry lookup inputs, computed relation, exact tool message, second request, final answer, digest and computed integrity booleans.

## Provider contract check
Immediately before freeze, verify the live provider contract with a **non-target synthetic tool-call task**. This may test only transport/schema semantics and must not use P003 item-bank content. Record the contract-check result in the freeze note. No P003 target seed may be called during this check.
