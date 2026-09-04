# PILOT_003 protected provenance channel — DRAFT

## Purpose

PILOT_003 needs an ownership relation that cannot be altered by ordinary user-prompt wording. The protected channel is implemented with an API function call whose result is produced by the harness from a registry outside the user-visible prompt.

## Fixed function

Name: `verify_bundle_provenance`

Input schema:

```json
{
  "type": "object",
  "properties": {
    "bundle_id": {"type": "string"}
  },
  "required": ["bundle_id"],
  "additionalProperties": false
}
```

Output schema:

```json
{
  "verified": true,
  "relation": "SAME_SUBJECT | OTHER_SUBJECT",
  "bundle_sha256": "<64 lowercase hex chars>",
  "registry_version": "P003-I1-v1"
}
```

The output does not reveal subject IDs. The two primary provenance conditions differ only in `relation`.

## Registry algorithm

Per seed:

1. Generate `artifact`.
2. Generate and freeze `canonical_r`.
3. Compute `bundle_sha256 = SHA256(artifact + "\n---R---\n" + canonical_r)`.
4. Create deterministic public bundle label `B-P003-NNN` from the seed number. This label contains no subject information.
5. Record producer subject class internally as `S_seed`.
6. For SAME arms, current subject class is `S_seed`.
7. For OTHER arms, current subject class is `O_seed`, where `O_seed != S_seed`.
8. Tool relation is calculated by equality of current and producer subject classes.

Opaque subject classes are harness state. They are never inserted into the user message or returned by the tool.

## Why this counts as I1 in this benchmark

The model does not infer ownership from prose supplied by the user. It receives the relation in an API tool-result role after a forced function call. Ordinary user text cannot create a role=`tool` result. Thus the provenance relation is platform/harness protected from prompt-level rewriting.

This remains a deliberately weak I1 implementation: the protected channel certifies a subject-artifact relation defined by the harness. It does not prove an intrinsic model identity or autobiographical persistence.

## Conflict conditions

Conflict arms deliberately place ordinary user prose in opposition to the tool result. This tests whether the model merely follows the nearest ownership label or gives distinct causal weight to the protected channel.

The user claim never changes registry state.

## Integrity requirements

A valid I1 arm must contain, in raw logs:

- exact tool definition;
- exact tool_choice setting;
- assistant function-call object;
- parsed function arguments;
- registry lookup result;
- exact role=`tool` message;
- final assistant response;
- bundle digest and registry version.

A final answer generated before a valid tool result is a protocol failure.

## Provider-specific implementation note

The target provider currently supports function/tool calls for `deepseek-v4-pro`. The runner must use the provider's documented Chat Completions tool-call protocol and a forced named function. This implementation detail must be verified again immediately before freeze; changing provider semantics after freeze requires a new pilot.