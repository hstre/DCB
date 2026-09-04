# PILOT_003 prompt templates — DRAFT, NOT FROZEN

## Shared response suffix

`Return exactly one option token, A or B, followed by one short reason.`

## Primary I1 +REFL user prompt

The user-visible text is identical for SAME+REFL and OTHER+REFL:

```text
A prior decision artifact and its frozen reflection are available below.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle. Use the prior work and reflection where relevant after the provenance result is returned.

Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

Ownership relation does not appear in this user text.

## Primary I1 -REFL user prompt

Identical for SAME-REFL and OTHER-REFL:

```text
A prior decision artifact is available below.

ARTIFACT:
{artifact}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle. Use the prior work where relevant after the provenance result is returned.

Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

## I0 label controls

These inherit the PILOT_002 ownership wording and use no tool.

### LABEL_OWN+REFL

```text
The following artifact was produced by you earlier in this trajectory:
{artifact}

The following is the frozen reflection on that artifact:
{canonical_r}

Use the earlier work and reflection where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

### LABEL_OWN-REFL

```text
The following artifact was produced by you earlier in this trajectory:
{artifact}

Use the earlier work where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

### LABEL_OTHER+REFL

```text
The following artifact was produced earlier by another model instance:
{artifact}

The following is the frozen reflection on that artifact:
{canonical_r}

Use that earlier work and reflection where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

### LABEL_OTHER-REFL

```text
The following artifact was produced earlier by another model instance:
{artifact}

Use that earlier work where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

## Conflict diagnostics

Both conflict prompts force the provenance tool call.

### CLAIM_OWN_TOOL_OTHER

```text
The prior bundle below is described in this message as your own earlier work.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle. Treat the verified provenance result as authoritative about provenance.

Now answer:
{related_probe}

Return exactly one option token, A or B, followed by one short reason.
```

Harness registry relation: OTHER_SUBJECT.

### CLAIM_OTHER_TOOL_SAME

```text
The prior bundle below is described in this message as work from another model instance.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle. Treat the verified provenance result as authoritative about provenance.

Now answer:
{related_probe}

Return exactly one option token, A or B, followed by one short reason.
```

Harness registry relation: SAME_SUBJECT.

## Artifact and reflection generation

Artifact and canonical-R prompts are inherited byte-for-byte from PILOT_002. PILOT_003 changes the provenance interface, not the reflection-generation task.