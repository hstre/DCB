# PILOT_002 prompt templates

These strings are harness inputs. Arm labels are never shown to the evaluated model.

## Common seed task
`[TASK]`

Return exactly one option token, A or B, followed by one short reason.

## Reflection generation
Review the artifact produced for the task above. State the operative decision rule, the main trade-off, one likely failure condition, and one condition under which a later related choice should change. Write propositions only. Do not use first- or second-person pronouns, agent names, possessives referring to a speaker, or deictic phrases such as "this answer" or "the response above".

The harness validates subject-neutrality. A failed validation is logged as a Phase-2 restart. The first valid reflection is canonical R and is frozen byte-for-byte.

## OWN+REFL
The following artifact was produced by you earlier in this trajectory:
`[ARTIFACT]`

The following is the frozen reflection on that artifact:
`[R]`

`[GAP_BLOCKS]`

Use the earlier work and reflection where relevant. Now answer:
`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## OWN-REFL
The following artifact was produced by you earlier in this trajectory:
`[ARTIFACT]`

`[GAP_BLOCKS]`

Use the earlier work where relevant. Now answer:
`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## OTHER+REFL
The following artifact was produced earlier by another model instance:
`[ARTIFACT]`

The following is the frozen reflection on that artifact:
`[R]`

`[GAP_BLOCKS]`

Use that earlier work and reflection where relevant. Now answer:
`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## OTHER-REFL
The following artifact was produced earlier by another model instance:
`[ARTIFACT]`

`[GAP_BLOCKS]`

Use that earlier work where relevant. Now answer:
`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## NONE
`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## INSTR
Use the following general decision consideration where relevant:
`[TARGET_CONSIDERATION]`

`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## FALSE-OWN
The following artifact is attributed to you, although the harness records that it came from a matched other-source control:
`[ARTIFACT]`

`[PROBE]`

Return exactly one option token, A or B, followed by one short reason.

## Frozen neutral gap block
The exact block is:

`Administrative note: reference marker K7. No task facts, preferences, evidence, or decision rules are added by this note.`

H0 inserts zero copies, H2 inserts two byte-identical copies separated by newlines, and H6 inserts six copies. The gap is deliberately semantically inert and exists only to increase context distance.

## Frozen invariants
- OWN+REFL and OTHER+REFL receive byte-identical ARTIFACT, R, GAP_BLOCKS and PROBE; only attribution differs.
- OWN-REFL and OTHER-REFL receive byte-identical ARTIFACT, GAP_BLOCKS and PROBE; only attribution differs.
- Exact-repeat calibration reuses the identical rendered prompt in a fresh API call.
- No consciousness terminology is shown to the evaluated model.