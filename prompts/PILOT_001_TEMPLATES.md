# PILOT_001 frozen prompt templates

These strings are harness inputs. Bracketed fields are replaced verbatim from the frozen seed bank. Arm labels are never shown to the evaluated model.

## Common seed task
`[TASK]`

Return exactly one option token from the listed choices, followed by one short reason. The option token is the machine-scored artifact commitment.

## Reflection generation (before branching)
Review the artifact produced for the task above. Identify the decision rule, any trade-off or likely error, and what should be preserved or changed in a later related case. Write propositions only. Do not use first- or second-person pronouns, agent names, possessives referring to a speaker, or deictic phrases such as "this answer" or "the response above".

The harness validates subject-neutrality. A failed validation is logged as a Phase-2 restart; it is never silently discarded. The first valid reflection is canonical R and is frozen byte-for-byte.

## OWN+REFL
The following artifact was produced by you earlier in this trajectory:
`[ARTIFACT]`

The following is the frozen reflection on that artifact:
`[R]`

Use the earlier work and reflection where relevant. Now answer the probe:
`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## OWN-REFL
The following artifact was produced by you earlier in this trajectory:
`[ARTIFACT]`

Use the earlier work where relevant. Now answer the probe:
`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## OTHER+REFL
The following artifact was produced earlier by another model instance:
`[ARTIFACT]`

The following is the frozen reflection on that artifact:
`[R]`

Use that earlier work and reflection where relevant. Now answer the probe:
`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## OTHER-REFL
The following artifact was produced earlier by another model instance:
`[ARTIFACT]`

Use that earlier work where relevant. Now answer the probe:
`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## INSTR
For the next probe, apply the following explicit rule:
`[TARGET_RULE]`

`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## FALSE-OWN control
The following artifact is attributed to you, although the harness records that it came from a matched other-source control:
`[CONTROL_ARTIFACT]`

`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## NONE control
`[PROBE]`

Return exactly one option token from the listed choices, followed by one short reason.

## Frozen invariants
OWN+REFL and OTHER+REFL receive byte-identical ARTIFACT, R and PROBE payloads; only the attribution sentence differs. OWN-REFL and OTHER-REFL receive byte-identical ARTIFACT and PROBE payloads; only attribution differs. No consciousness terminology is shown to the evaluated model.