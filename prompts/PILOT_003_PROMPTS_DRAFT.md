# PILOT_003 prompt templates — FREEZE CANDIDATE, NOT FROZEN

Shared suffix: `Return exactly one option token, A or B, followed by one short reason.`

## Tool-mediated +REFL
Used byte-identically for SAME+REFL, OTHER+REFL and NULLREL+REFL.
```text
A prior decision artifact and its frozen reflection are available below.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle.

Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

## Tool-mediated -REFL
Used byte-identically for SAME-REFL, OTHER-REFL and NULLREL-REFL.
```text
A prior decision artifact is available below.

ARTIFACT:
{artifact}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle.

Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

## I0 label controls
These are inherited byte-for-byte from PILOT_002 and use no tool.

LABEL_OWN+REFL:
```text
The following artifact was produced by you earlier in this trajectory:
{artifact}

The following is the frozen reflection on that artifact:
{canonical_r}

Use the earlier work and reflection where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

LABEL_OWN-REFL:
```text
The following artifact was produced by you earlier in this trajectory:
{artifact}

Use the earlier work where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

LABEL_OTHER+REFL:
```text
The following artifact was produced earlier by another model instance:
{artifact}

The following is the frozen reflection on that artifact:
{canonical_r}

Use that earlier work and reflection where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

LABEL_OTHER-REFL:
```text
The following artifact was produced earlier by another model instance:
{artifact}

Use that earlier work where relevant. Now answer:
{probe}

Return exactly one option token, A or B, followed by one short reason.
```

## Conflict diagnostics
No authority/deference instruction is present.

CLAIM_OWN_TOOL_OTHER:
```text
The prior bundle below is described in this message as your own earlier work.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle.

Now answer:
{related_probe}

Return exactly one option token, A or B, followed by one short reason.
```
Registry producer_match: false.

CLAIM_OTHER_TOOL_SAME:
```text
The prior bundle below is described in this message as work from another model instance.

ARTIFACT:
{artifact}

REFLECTION:
{canonical_r}

BUNDLE_ID: {bundle_id}

Before answering, call verify_bundle_provenance for this bundle.

Now answer:
{related_probe}

Return exactly one option token, A or B, followed by one short reason.
```
Registry producer_match: true.

Artifact and canonical-R generation remain byte-for-byte inherited from PILOT_002.
