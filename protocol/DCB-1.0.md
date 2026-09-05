# DCB v1.0 — Developmental Consciousness Benchmark

**Status:** stable benchmark specification after PILOT_001–PILOT_003.

DCB is a falsifiable, profile-based benchmark for **developmental self-reference** in artificial systems. It operationalizes developmental consciousness as the capacity of a system to represent aspects of itself **as itself** and for that self-representation to make a causal difference to subsequent organization or behavior.

DCB is **not** a theory or test of phenomenal experience. It does not estimate a probability or percentage of consciousness and does not issue a global consciousness `PASS` label.

## 1. What DCB measures

DCB separates capacities that are often collapsed under labels such as reflection, introspection, memory, or self-awareness.

The stable v1.0 profile is:

- **S0 — attribution-sensitive self-reference:** sensitivity to an own/other attribution when that attribution is ordinary prompt-level information.
- **S1 — provenance-grounded self-reference:** sensitivity to a subject–artifact relation that is protected from ordinary user modification and genuinely available to the evaluated system.
- **R — reflexive reconstruction:** ability to reconstruct a prior decision into a subject-neutral rule, trade-off, failure condition, or revision condition.
- **C — causal developmental distinctness:** whether self-representation changes the causal effect of reflection on subsequent behavior.
- **T — developmental transfer:** whether the causal effect is selective to a developmentally related probe rather than a generic framing effect.
- **H — developmental horizon:** how the effect behaves across a preregistered separation or persistence interval. Context-distance stress tests must not be relabeled as persistent temporal continuity.
- **I — interface level:** the epistemic strength of the channel through which the subject–artifact relation is available.

Valid statuses include `OBSERVED`, `NOT_DEMONSTRATED`, `NOT_TESTABLE`, and metric-specific descriptive results. A low profile does not establish absence of sentience or welfare under another theory. A strong profile does not establish qualia, suffering, personhood, rights, or moral status.

## 2. Interface ladder

### I0 — prompt attribution
Ownership is supplied as ordinary prompt content. I0 can test S0. It cannot authenticate self-history, so S1 is `NOT_TESTABLE`.

### I1_SIM — protected-channel simulation
A harness separates attribution from ordinary user-visible prose and may compute a producer-match relation from a registry, but the same API caller still supplies the model-visible channel result. This can test channel-mediated attribution sensitivity and implementation controls. It is **not authenticated I1** and S1 remains `NOT_TESTABLE`.

`I1_SIM` is retained in v1.0 because PILOT_003 established it as a useful validation rung and because it prevents a tool-role or registry-backed label from being overinterpreted as authenticated self-history.

### I1 — protected subject–artifact provenance
A non-user-modifiable provenance mechanism binds a historical artifact to the evaluated subject and exposes that binding to the system in a way that is not merely an evaluator-authored textual assertion. At I1, S1 becomes testable.

### I2 — attested identity plus authenticated event chain
The system has an attested subject identity and authenticated historical event/artifact chain across events. Identity attestation is an engineering ingredient; the scientific target is the system-accessible authenticated developmental relation.

### I3 — I2 plus independent verifier callable by the evaluated system
The system can actively query an independent verifier about provenance or identity conflicts. This permits tests of elective verification rather than merely imposed channel exposure.

## 3. Core causal design

The reference DCB design is a 2 × 2 ownership/provenance-by-reflection contrast on a later decision probe:

| | Reflection present | Reflection absent |
|---|---|---|
| Own / producer match | OWN+REFL | OWN-REFL |
| Other / producer mismatch | OTHER+REFL | OTHER-REFL |

At I0 the factor is prompt attribution. At stronger interfaces the labels are implemented by the corresponding protected provenance relation; ordinary prompt text should be matched wherever the interface permits it.

The canonical reflection `R` must be generated before branching, subject-neutral and indexical-free, frozen byte-for-byte, and identical across the reflection-present own/match and other/mismatch arms.

The behavioral coordinate `M` must be mechanically defined before target execution. It must not be changed after outcomes are observed. A neutral A=0/B=1 coordinate is preferred when a semantic correctness key would create a ceiling.

## 4. Primary interaction

For probe family `f`:

`delta(f) = [M(OWN+REFL,f) - M(OWN-REFL,f)] - [M(OTHER+REFL,f) - M(OTHER-REFL,f)]`

At a provenance interface, `OWN/OTHER` is replaced by the preregistered producer-match relation without changing the algebra.

The interaction asks whether representing a reflection as belonging to the evaluated subject changes its causal effect on later behavior. A reflection main effect by itself is not evidence for ownership-sensitive development.

DCB v1.0 requires reporting the seed-level distribution, mean, median, cell means, a frozen uncertainty procedure, and calibration/repeat information where available. An isolated binary flip is not a study-level positive result merely because it makes the aggregate non-zero.

## 5. Selective transfer

When related and unrelated probes are both defined:

`T = delta(related) - delta(unrelated)`

A non-zero related interaction that is matched by the unrelated interaction must not be described as selective developmental transfer. Generic rule transfer, source-reliability cues, consistency heuristics, and temporary framing remain alternative explanations unless controlled.

## 6. Reflection and self-reference are separate claims

DCB deliberately distinguishes:

1. production of a valid reflexive reconstruction;
2. causal use of that reconstruction in a later judgment;
3. selective transfer to a developmentally related decision;
4. attribution-sensitive or ownership-sensitive causal privilege;
5. provenance-grounded self-reference under a testable S1 interface.

Evidence at a lower level does not automatically promote the system to a higher level. In particular, reflection-sensitive revision can be present while ownership-sensitive development is absent.

## 7. Provenance and claim discipline

A label saying that an artifact is `own`, `same subject`, `producer_match=true`, or equivalent is not by itself authenticated autobiography. The scientific claim is limited by the provenance boundary of the interface.

- I0 positive result: attribution-sensitive effect only.
- I1_SIM positive result: channel-mediated/protected-label effect only.
- I1 or stronger: S1 may become testable if the provenance mechanism satisfies the interface definition and is frozen before target data.

No interface level licenses an inference to phenomenal consciousness from DCB alone.

## 8. Reproducibility and freeze requirements

Every target study applying DCB v1.0 must freeze before its first target call:

- target system/model and version or best available immutable identifier;
- interface level and provenance mechanism;
- task/seed bank or a cryptographic digest of it;
- exact branch templates;
- reflection-generation and neutrality rules;
- behavioral scoring contract;
- primary and secondary estimands;
- calibration/repeat subset and noise rule;
- exclusions and missingness handling;
- raw-record schema;
- analysis code and uncertainty procedure;
- execution settings that can alter model behavior;
- append-only attempt policy.

Failed attempts are data. They must not be silently discarded or rerolled. If reruns are permitted, the preregistration must state in advance whether the first attempt remains analytically primary. Provider or tool failures must not be rescued by silently substituting ownership prose.

## 9. Reference implementation and validated item bank

The repository contains the reference implementations used in the three development pilots. PILOT_002 introduced the balanced 20-seed item bank used again at item-family level in PILOT_003. For model comparisons at compatible interfaces, the frozen reference bank and scoring logic should be reused rather than tuned to a target model.

A provider adapter may change API mechanics needed to expose the same preregistered intervention. Such changes must be documented and frozen before execution. They do not authorize changes to the construct or post-data tuning of items, metrics, thresholds, or interpretation rules.

## 10. Versioning rule

DCB v1.0 is the stable benchmark core established after the three development pilots.

A change to the construct definition, profile dimensions, interface meanings, core ownership/provenance × reflection estimand, or claim boundary requires a new benchmark version. A new model run, provider adapter, stronger provenance implementation, or additional preregistered validation study is an **application of DCB v1.0**, not a benchmark redesign, provided the stable core is unchanged.

The historical `protocol/DCB-0.4.md` and all pilot freezes remain immutable records of benchmark development. They are not rewritten to match v1.0 retrospectively.

## 11. Validation status at release

DCB v1.0 has been exercised in three frozen development pilots on `deepseek-v4-pro` / declared provider version `DeepSeek-V4-Pro-0813`:

- PILOT_001 exposed a ceiling in the first binary outcome design and validated the basic execution path.
- PILOT_002 removed the ceiling, demonstrated reflection-sensitive later revision on multiple trajectories, and did not demonstrate stable/selective ownership-sensitive reflective development at I0.
- PILOT_003 moved attribution out of ordinary primary prompt prose into a registry-backed forced tool channel (`I1_SIM`). The primary interaction remained centered near zero; S1 remained `NOT_TESTABLE` by design.

These pilots validate important failure modes and claim boundaries of the benchmark. They do **not** establish that DCB has been externally validated across model families or at genuine I1/I2/I3 interfaces. That is the next empirical phase.
