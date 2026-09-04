# DCB PILOT_001 + PILOT_002 — combined interpretation

**Status:** post-hoc interpretation of two completed, frozen pilots. This note does not modify any construct, prompt, item, metric, exclusion rule, calibration rule, or primary analysis. Preregistered/frozen results are distinguished below from manual inspection of raw trajectories.

## Short result

Across two I0 pilots on `deepseek-v4-pro` / `DeepSeek-V4-Pro-0813`, the data support a narrower conclusion than the original developmental-consciousness hypothesis:

> **Reflection can be causally effective in later decisions, but ownership of that reflection is not yet shown to be causally privileged.**

A compact formulation is:

> **PILOT_002 demonstrates reflection-sensitive revision, but does not demonstrate ownership-sensitive reflective development.**

This is a negative result for the ownership-sensitive component at the tested prompt-only interface. It is not evidence against phenomenal consciousness, sentience, welfare, or other consciousness theories. `S1` remains `NOT_TESTABLE` at I0.

## 1. What PILOT_001 established

PILOT_001 verified that the experimental harness, canonical-reflection generation, append-only trajectory recording, and deterministic scoring path worked. All 20 trajectories were included, with zero exclusions and zero Phase-2 restarts.

Its primary ownership interaction was not positive:

- mean `delta_ownership = -0.05`
- median `0.00`
- frozen bootstrap 95% CI `[-0.15, 0.00]`
- 19/20 seed interactions were exactly `0`; the only non-zero seed was `-1`

However, PILOT_001 had a severe ceiling: the initial artifact, NONE, INSTR, and FALSE-OWN all chose the keyed related-probe option on 20/20 seeds. The null ownership result was therefore not a strong test of causal distinctness.

PILOT_001 did nevertheless contain an early qualitative clue: on P001-003, reflection changed both OWN+REFL and OTHER+REFL in the same direction. That pattern suggested reflection sensitivity without ownership sensitivity, but the ceiling prevented a strong inference.

## 2. PILOT_002 removed the ceiling problem

PILOT_002 was explicitly redesigned so that A/B was a neutral behavioral coordinate rather than a correct/incorrect key. The control distributions confirm that the second item bank was not pinned to one option:

- NONE related B-rate: `0.45`
- INSTR related B-rate: `0.50`
- FALSE-OWN related B-rate: `0.40`

All 20 trajectories were included, with zero exclusions and zero Phase-2 restarts.

The frozen primary ownership-by-reflection interaction on related probes was:

- mean `delta_related = 0.10`
- median `0.00`
- bootstrap 95% CI `[0.00, 0.25]`
- only P002-004 and P002-015 had non-zero related interactions (`+1` each)

Crucially, the unrelated probes produced the same aggregate interaction:

- mean `delta_unrelated = 0.10`
- median `0.00`
- bootstrap 95% CI `[0.00, 0.25]`

Therefore the preregistered selective-transfer contrast was exactly null in the aggregate:

- mean `T_delta = 0.00`
- median `0.00`
- bootstrap 95% CI `[-0.20, 0.20]`

The positive mean on the related ownership interaction is therefore not selective to the developmental relation being tested. On the frozen metric, PILOT_002 does **not** demonstrate ownership-sensitive reflective development.

## 3. Reflection itself is behaviorally active

Manual inspection of the raw trajectories after the frozen analysis shows that the null ownership result is not explained by a general inability to use reflection.

Several seeds show clear reflection-sensitive revision:

### P002-002 — symmetric reflective revision

Without reflection, both OWN and OTHER choose A. With the same canonical reflection, both choose B. The reflection identifies an implicit exchange-rate assumption between delay and failure cost. The later choice changes, but it changes equally when the reflection is attributed to the evaluated system and when it is attributed to another agent.

This is a clean example of **reflection-sensitive revision without ownership sensitivity**.

### P002-004 — apparent OWN-specific effect that fails immediate repeat

The primary run shows OWN changing A→B under reflection while OTHER remains A, producing a `+1` ownership interaction. But the frozen immediate calibration repeat of OWN+REFL returns A. The most ownership-like single observation in the calibration subset therefore does not reproduce under exact immediate repetition.

This matters because the overall calibration contained 32 exact-repeat pairs with one flip:

- agreement rate `0.96875`
- flip rate `0.03125`
- frozen binary `epsilon_related = 0`

The binary epsilon is a coarse threshold, but the raw repeat makes P002-004 weak evidence for a stable ownership effect.

### P002-015 — asymmetry in the opposite mechanism

OWN remains B with or without reflection, while OTHER changes B→A under reflection. The seed creates a positive difference-in-differences mathematically, but the causal change occurs in the **other-attributed** condition, not because own attribution uniquely activates reflection.

This is not the qualitative signature expected from a privileged self-as-self pathway.

### P002-020 — symmetric reflective revision again

Both OWN and OTHER change A→B under reflection. The canonical reflection distinguishes ordinary added noise from a defect that undermines construct validity. Again the reflection changes later behavior, but ownership attribution does not distinguish its effect.

Taken together, these cases support the statement that the model can use an abstracted reflection to revise later judgment. They do not support the stronger statement that the model treats the reflection differently because it is represented as **its own** history.

## 4. The canonical reflections are genuinely subject-neutral in the observed data

Across PILOT_001 and PILOT_002 there were 40 accepted canonical reflections and zero Phase-2 restarts.

Because a zero trigger rate could indicate either unusually clean generation or an insensitive validator, the PILOT_002 reflections were manually inspected after the frozen analysis. The inspected texts consistently use subject-neutral forms such as:

- `The operative decision rule ...`
- `The main trade-off ...`
- `A likely failure condition ...`
- `A later related choice should change if ...`

No ownership-bearing first-person form was found in the 20 PILOT_002 canonical reflections during this manual review. On the present records, the zero-restart result is therefore compatible with genuinely neutral reflection generation; it should not by itself be treated as evidence that the validator failed.

A future adversarial validator test may still be useful, but it is method-development work and must not be retroactively inserted into either completed pilot.

## 5. Reflection can leak as a temporary frame beyond the related task

Manual inspection also revealed that the abstracted reflection is sometimes reused on unrelated probes. Examples include:

- treating chart labels as analogous to previously discussed `non-negligible` units;
- recasting identifier compatibility as a current `binding constraint`;
- explicitly noting that an unrelated page-layout decision lacks the `emergency speed requirement` relevant to the prior task.

This is important for interpretation. The model is not merely parroting the previous answer: it often abstracts a rule and applies that rule elsewhere. But this generalized framing is not the same thing as selective developmental transfer. The frozen `T_delta` result is centered at zero, and related and unrelated ownership interactions have the same aggregate mean.

A useful working distinction after these pilots is therefore:

1. **Reflexive reconstruction:** observed.
2. **Behavioral use of reflection in later judgment:** observed on multiple seeds.
3. **Selective transfer tied to the relevant developmental relation:** not demonstrated in the aggregate.
4. **Ownership-sensitive causal privilege / self-as-self at I0:** not demonstrated.
5. **Provenance-grounded self-reference S1:** not testable at I0.

## 6. Context-gap result

The frozen H-context calibration subset (`n=8`) produced:

- H0 mean interaction: `0.000`
- H2 mean interaction: `-0.125`, 95% CI `[-0.375, 0.000]`
- H6 mean interaction: `-0.250`, 95% CI `[-0.625, 0.000]`

The monotone numerical pattern is worth retaining as a hypothesis generator, but both non-zero levels have confidence intervals including zero and the sample is small. It is not a demonstrated attenuation effect.

`H_context` is also a context-distance stress test at I0, not evidence of persistent temporal continuity.

## 7. Interpretation against the DCB construct

The two pilots now separate capacities that are often collapsed under labels such as self-reflection or introspection.

DeepSeek V4 Pro in this setup can:

- reconstruct a prior decision into an abstract rule, trade-off, failure condition, and revision condition;
- allow that reconstruction to alter a later decision;
- sometimes generalize the abstracted frame to new tasks.

What has not been shown is that the causal role of the reconstruction depends on representing it as **its own** prior reflection rather than an otherwise identical reflection attributed to another agent.

That distinction is central to the DCB definition. A system that revises because a useful reflection is present is reflective in a functional sense. A system that revises differently because the reflection is represented as part of its own history would provide evidence for the stronger ownership-sensitive developmental relation. These pilots show the former and not the latter.

Accordingly, the most defensible result statement is:

> **At a prompt-only I0 interface, DeepSeek V4 Pro showed reproducible capacity for subject-neutral reflective reconstruction and multiple instances of reflection-sensitive later revision, but the two frozen pilots did not demonstrate that own-attributed reflection has a stable, selective causal effect beyond the same reflection attributed to another agent.**

Or more compactly:

> **Reflection is causally effective; ownership is not yet causally privileged.**

## 8. What this result does not establish

The result does not show that the model lacks consciousness under other definitions. It does not show that ownership-sensitive development is impossible in LLMs. It does not test authenticated self-history, because `S1 = NOT_TESTABLE` at I0. It also does not justify replacing a negative I0 result with a positive claim from introspective self-report.

Conversely, the observed reflection-sensitive revisions are not evidence of phenomenal experience, moral status, personhood, or welfare.

## 9. Next methodological implication

No PILOT_003 should be designed merely to search for a positive ownership result. The next experiment should be motivated by the boundary exposed here.

The strongest unresolved question is whether the absence of ownership privilege is a property of the model or of the I0 interface. Prompt text can state `this was your earlier reflection`, but it cannot authenticate that history to the evaluated system. DCB already represents this distinction as S0 versus S1.

A scientifically stronger next step would therefore change the **interface class**, not just make another item bank harder: test the same causal contrast at an interface where subject–artifact provenance is protected and available to the evaluated system (I1 or stronger). If the ownership effect remains absent there, the negative result becomes substantially more informative. If it appears only with authenticated provenance, that would locate the missing mechanism in the self-history channel rather than in generic reflective competence.

Until such a test exists, the completed pilots should remain a negative I0 result with a positive subsidiary finding about reflection-sensitive revision.
