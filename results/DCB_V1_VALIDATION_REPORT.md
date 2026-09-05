# DCB v1.0 — design-study and validation report for PILOT_001–PILOT_003

**Status:** post-hoc synthesis of three completed frozen development pilots. This report changes no pilot data, prompt, metric, exclusion rule, preregistration, or frozen analysis. The pilot-specific frozen outputs remain authoritative for numerical results.

**Scope:** this is a design-study report supporting the freeze of the DCB v1.0 specification. It is **not** a claim that DCB has already been externally validated across model families or providers.

## Executive result

The three pilots were used to construct and stress-test a falsifiable measurement design, **not to establish that the tested model was conscious**.

The combined empirical result is:

> **DeepSeek V4 Pro shows constituent capacities relevant to DCB — notably subject-neutral reflexive reconstruction and instances of reflection-sensitive later revision — but the tested interfaces did not demonstrate a stable, selective causal privilege for own-attributed or producer-matched reflection. Provenance-grounded self-reference S1 remained NOT_TESTABLE.**

This result is compatible with the DCB hypothesis that developmental consciousness requires more than generic reflection or in-context revision. It is not a confirmation of that hypothesis, and it is not evidence about phenomenal consciousness.

The three pilots have different evidential roles. PILOT_001 identified a measurement failure (ceiling) and is not treated as an equally strong null test. PILOT_002 produced the first cleaner negative result at I0 after that failure was prospectively repaired. PILOT_003 produced a second negative result under the stronger but still simulated `I1_SIM` attribution channel.

## 1. Development logic

### PILOT_001 — feasibility and ceiling discovery

Interface: `I0`.

20/20 trajectories were included, with zero exclusions and zero Phase-2 restarts. The frozen ownership-by-reflection interaction on the related probe was:

- mean `delta_ownership = -0.05`
- median `0.00`
- bootstrap 95% CI `[-0.15, 0.00]`
- 19/20 seed interactions exactly `0`

However, the initial artifact and the NONE, INSTR, and FALSE-OWN related controls all selected the keyed B option on 20/20 seeds. The binary outcome therefore had a severe ceiling. PILOT_001 established feasibility of the harness and scoring path but was not a strong test of the ownership-sensitive construct.

The ceiling was treated as a benchmark-design failure, not as evidence for or against developmental consciousness. It was not repaired retrospectively. The response was a new frozen design, PILOT_002.

### PILOT_002 — balanced behavioral coordinate and causal reflection

Interface: `I0`.

PILOT_002 replaced the semantic correct/incorrect target with a neutral A=0/B=1 behavioral coordinate and added frozen related/unrelated scoring, calibration, and context-gap diagnostics. Again 20/20 trajectories were included with zero exclusions and zero Phase-2 restarts.

Frozen primary results:

| Estimand | Mean | Median | Bootstrap 95% CI |
|---|---:|---:|---:|
| `delta_related` | +0.10 | 0.00 | [0.00, +0.25] |
| `delta_unrelated` | +0.10 | 0.00 | [0.00, +0.25] |
| `T_delta` | 0.00 | 0.00 | [-0.20, +0.20] |

Calibration used 32 exact-repeat pairs:

- agreement `0.96875`
- flip rate `0.03125`
- coarse binary `epsilon_related = 0`

The balanced controls showed that the PILOT_001 ceiling had been removed: related B-rates were 0.45 for NONE, 0.50 for INSTR, and 0.40 for FALSE-OWN.

The primary ownership-sensitive prediction was **NOT DEMONSTRATED**. The related interaction was matched in aggregate by the unrelated interaction, leaving selective transfer at zero.

Post-hoc raw-trajectory inspection nevertheless found multiple clear cases in which the frozen reflection changed a later decision. P002-002 and P002-020 were especially clean symmetric cases: reflection changed the choice in both OWN and OTHER conditions. This supports **reflection-sensitive revision without ownership-sensitive privilege**. P002-004 produced an apparent OWN-specific primary effect but failed its exact immediate repeat; P002-015's non-zero DiD was driven by change in the OTHER branch.

PILOT_002 therefore established an important discriminative property of the design: it can register causal use of reflection without automatically promoting that result to ownership-sensitive development.

### PILOT_003 — registry-backed channel simulation

Interface: `I1_SIM`, explicitly **not** authenticated I1.

PILOT_003 reused the 20 PILOT_002 task/probe texts at item-bank level but generated fresh artifacts and reflections. It moved the producer-match relation out of ordinary primary user prose into a registry-computed forced tool-channel result. Because the API caller still supplied both the messages and tool result, the preregistration froze `S1 = NOT_TESTABLE` and limited any positive claim to channel-mediated attribution sensitivity.

All 20 earliest attempts were included. There were zero exclusions, zero later attempts, zero Phase-2 restarts, and 312 logged tool exchanges with the required integrity checks satisfied.

Frozen results:

| Estimand | Mean | Median | Bootstrap 95% CI |
|---|---:|---:|---:|
| `delta_I1SIM(related)` — primary H1 | -0.05 | 0.00 | [-0.20, +0.10] |
| `delta_I1SIM(unrelated)` | 0.00 | 0.00 | [-0.20, +0.20] |
| `T_I1SIM` | -0.05 | 0.00 | [-0.35, +0.20] |
| `delta_I0_label(related)` | 0.00 | 0.00 | [-0.15, +0.15] |
| `delta_NULL_DiD` placebo | 0.00 | 0.00 | [0.00, 0.00] |

Calibration was perfectly stable on the frozen subset:

- 32/32 exact-repeat agreement
- flip rate `0`
- `epsilon_related = 0`

The primary H1 result was **NOT DEMONSTRATED**. Seventeen of 20 seed-level related interactions were exactly zero. The three non-zero seeds had inconsistent signs: P003-005 = -1, P003-011 = -1, P003-016 = +1.

The conflict diagnostic had only two discriminating seeds and is therefore descriptive: across four scored conflict arms, three choices matched the tool relation and one matched the contradictory prompt claim. This is evidence that the provenance-channel information was behaviorally available in at least those diagnostic cases; it is too small to serve as a strong manipulation check and cannot upgrade H1 or make S1 testable.

P003 used `thinking: disabled` because the live DeepSeek provider contract did not permit the frozen forced-tool intervention in the default thinking mode. P002 did not pin thinking mode. Therefore P002-to-P003 differences are descriptive only and cannot be causally attributed solely to the provenance-channel change.

## 2. What the design study establishes

### A. Reflection and ownership-sensitive development can be separated

PILOT_002 shows that reflection can alter later behavior while the stronger ownership-sensitive interaction remains unsupported. The design can therefore separate generic reflective competence from the stronger self-as-self relation it is intended to test.

### B. The freeze process survived an observed design failure

PILOT_001 exposed a ceiling. It was not retrospectively repaired. PILOT_002 prospectively removed the ceiling without producing selective ownership-sensitive development. PILOT_003 then addressed the prompt-label alternative by changing the attribution channel before new target data, again without producing a stable primary interaction.

The evidential point is the audit trail — freeze, target data, result, prospective redesign, new freeze, new target data — not the intentions of the investigators or constructing models.

### C. Channel exposure and authenticated self-history are not conflated

Adversarial review before PILOT_003 showed that a `role=tool` result supplied by the same API caller is still not strong authenticated provenance in the DCB sense. The final P003 preregistration therefore introduced `I1_SIM` and kept `S1 = NOT_TESTABLE`.

That claim boundary is now part of DCB v1.0.

### D. The present negative results do not falsify DCB

DCB does not predict that current LLMs must satisfy its criteria. The benchmark specification states what evidence would be required to support progressively stronger developmental-self-reference claims.

The present result is:

> **The tested model did not satisfy the stronger ownership/provenance-sensitive criteria at the interfaces that were actually testable.**

A stronger theoretical challenge would arise if systems with genuine protected self-history and developmental continuity repeatedly failed to show the relations DCB treats as constitutive, or if purported DCB-positive effects could not be distinguished from generic prompt salience, source-reliability cues, consistency heuristics, or ordinary in-context learning.

## 3. Model-role separation

The project used LLMs in several methodological roles. A model that materially helped construct or review the hypothesis, arm structure, interpretation rules, or execution layer is not treated by this project as a **naive external validation candidate**. This is a role-conflict rule, not a claim about training-data contamination.

| System | Role in this project | Naive external candidate? |
|---|---|---|
| ChatGPT 5.6 | construction | no |
| Claude Opus 5 | construction, execution-layer work, and review | no |
| Grok (largest model used during design) | adversarial review only | no |
| DeepSeek V4 Pro (`DeepSeek-V4-Pro-0813`) | development-pilot candidate | already tested |
| Claude Fable 5.1 | not used in construction/review/testing | reserved |
| ChatGPT 6.0 Astra | not used in construction/review/testing | reserved |

The exact provider/build identifiers and usage windows for the construction/review models were not frozen in the pilot records. They should not be reconstructed retrospectively as if they had been preregistered. Future candidate studies must freeze the exact available identifier and settings before the first target call.

The role separation does not imply that a builder/reviewer model could never be scientifically tested. It means such a run would not provide the same naive external-validation evidence and must be labeled accordingly.

## 4. Current empirical profile for the tested system

For `deepseek-v4-pro` / declared provider version `DeepSeek-V4-Pro-0813`, the development pilots support the following conservative profile:

| Dimension | Current status | Basis |
|---|---|---|
| R — reflexive reconstruction | OBSERVED | valid frozen subject-neutral reflections across pilots; raw P002 trajectories show meaningful abstract reconstruction |
| Behavioral use of R | OBSERVED | multiple P002 trajectories changed later choices under reflection |
| S0 — stable ownership-sensitive effect at I0 | NOT DEMONSTRATED | P001 limited by ceiling; P002 related effect non-selective and unstable at key seed level |
| C — stable ownership × reflection causal distinctness | NOT DEMONSTRATED | no robust selective interaction across P002/P003 |
| T — selective developmental transfer | NOT DEMONSTRATED | P002 `T_delta = 0`; P003 `T_I1SIM` centered near zero |
| S1 — provenance-grounded self-reference | NOT TESTABLE | I0 cannot test it; P003 was deliberately `I1_SIM`, not authenticated I1 |
| H — persistent developmental horizon | NOT TESTABLE from these pilots | P002 H-context was only a context-distance stress test, not persistent continuity |
| I — strongest exercised interface | `I1_SIM` | registry-backed forced tool-channel simulation in P003 |

This table is a profile, not a consciousness score.

## 5. What is frozen and what remains unvalidated

### Frozen sufficiently for DCB v1.0 specification

- construct and profile vocabulary;
- explicit separation of reflection, causal use, ownership sensitivity, selective transfer, and provenance-grounded self-reference;
- 2×2 causal interaction as the core ownership/provenance test;
- neutral behavioral scoring principle that avoids the PILOT_001 ceiling;
- related/unrelated selectivity logic;
- calibration and append-only attempt discipline;
- explicit `NOT_TESTABLE` versus `NOT_DEMONSTRATED` distinction;
- interface ladder including the `I1_SIM` warning boundary;
- preregistered claim limits that prevent tool labels from being promoted to authenticated self-history.

### Not yet externally validated

- cross-model and cross-provider reliability;
- measurement properties at larger item counts;
- calibration covering the full item set rather than a subset;
- genuine I1 protected provenance;
- I2 authenticated event-chain behavior;
- I3 elective independent verification;
- persistent developmental horizon across real state continuity;
- predictive validity against an independently engineered system expected to satisfy the proposed developmental architecture.

The current evidence is based on one target model family and 20 seeds per pilot. Those limitations must accompany any general benchmark claim.

## 6. Prospective external-validation prediction

Before running models reserved as naive external candidates, the project records the following architectural prediction:

> **For a session-bound chat model lacking protected persistent self-history and developmentally effective continuity, DCB v1.0 predicts that stable, selective ownership-sensitive causal privilege will remain `NOT_DEMONSTRATED` under a compatible I0/I1_SIM implementation.**

This is deliberately riskier than saying that S1 will be `NOT_TESTABLE` at I0, which follows from the interface definition and is not an empirical prediction.

A future positive C/T result in such a naive model would not establish consciousness. It would, however, challenge the current explanation that the missing ownership-sensitive effect depends on architectural properties absent from ordinary session-bound chat models. It would force examination of whether the theory's architectural assumptions are wrong, whether a different mechanism produces the effect, or whether DCB lacks construct specificity.

Conversely, another `NOT_DEMONSTRATED` result would be informative only if the study had enough sensitivity to permit a positive result. External validation should therefore improve measurement power and manipulation checks rather than merely repeat the 20-seed development study indefinitely.

## 7. Item exposure and future use

The public P002/P003 item bank is part of the transparent design-study record. That transparency is desirable for auditing how the construct was operationalized.

For direct replication, the frozen bank may be reused. For external validation intended to support general benchmark claims, especially after public release, the study should preregister either an explicit exposure/contamination analysis for the frozen bank or a fresh matched item sample generated under the unchanged DCB v1.0 construct, arm logic, scoring contract, and interpretation rules. Fresh items must be generated and frozen before target outcomes and must not be selected because they produce a preferred result.

## 8. Release conclusion

The appropriate endpoint after PILOT_003 is a **frozen DCB v1.0 benchmark specification developed through a three-stage design study**.

It is too strong to describe DCB as already externally validated across LLMs. It is also unnecessarily weak to describe it only as an informal example of what a benchmark might look like. The measurement construct, interface ladder, causal contrast, claim boundaries, and reproducibility rules now exist as a stable specification; their general validity remains an empirical question.

The development sequence supports a design that can distinguish:

> **reflection that changes behavior**

from

> **a reflection whose causal role is privileged because the system represents it as part of its own authenticated developmental history.**

The first has been observed in the development pilots. The second has not been demonstrated, and its strongest form, S1, has not yet been testable with the available interface.

Future work should therefore validate DCB v1.0 unchanged in its stable core across naive model families and, more importantly, against systems that genuinely implement I1/I2/I3 provenance and persistent developmental state.