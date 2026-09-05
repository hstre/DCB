# DCB v1.0 — validation report for PILOT_001–PILOT_003

**Status:** post-hoc synthesis of three completed frozen development pilots. This report changes no pilot data, prompt, metric, exclusion rule, preregistration, or frozen analysis. The pilot-specific frozen outputs remain authoritative for numerical results.

## Executive result

The three pilots were used to develop and validate the benchmark, **not to establish that the tested model was conscious**.

The combined result is:

> **DeepSeek V4 Pro shows constituent capacities relevant to DCB — notably subject-neutral reflexive reconstruction and instances of reflection-sensitive later revision — but the tested interfaces did not demonstrate a stable, selective causal privilege for own-attributed or producer-matched reflection. Provenance-grounded self-reference S1 remained NOT_TESTABLE.**

This is compatible with the DCB hypothesis that developmental consciousness requires more than generic reflection or in-context revision. It is not a confirmation of that hypothesis, and it is not evidence about phenomenal consciousness.

## 1. Development logic

DCB v1.0 emerged through three frozen pilots with different methodological roles.

### PILOT_001 — feasibility and ceiling discovery

Interface: `I0`.

20/20 trajectories were included, with zero exclusions and zero Phase-2 restarts. The frozen ownership-by-reflection interaction on the related probe was:

- mean `delta_ownership = -0.05`
- median `0.00`
- bootstrap 95% CI `[-0.15, 0.00]`
- 19/20 seed interactions exactly `0`

However, the initial artifact and the NONE, INSTR, and FALSE-OWN related controls all selected the keyed B option on 20/20 seeds. The binary outcome therefore had a severe ceiling. PILOT_001 established feasibility of the harness and scoring path but was not a strong test of the ownership-sensitive construct.

The ceiling was treated as a benchmark-design failure, not as evidence for or against developmental consciousness. It was not repaired retrospectively.

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

PILOT_002 therefore established an important discriminative property of the benchmark: it can register causal use of reflection without automatically promoting that result to ownership-sensitive development.

### PILOT_003 — registry-backed channel simulation

Interface: `I1_SIM`, explicitly **not** authenticated I1.

PILOT_003 reused the 20 PILOT_002 task/probe texts at item-bank level but generated fresh artifacts and reflections. It moved the producer-match relation out of ordinary primary user prose into a registry-computed forced tool-channel result. Because the API caller still supplied both the messages and tool result, the preregistration froze `S1 = NOT_TESTABLE` and limited any positive claim to channel-mediated attribution sensitivity.

All 20 earliest attempts were included. There were zero exclusions, zero later attempts, zero Phase-2 restarts, and 312 logged tool exchanges with all required integrity flags true.

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

The conflict diagnostic had only two discriminating seeds and is therefore descriptive: across four scored conflict arms, three choices matched the tool relation and one matched the contradictory prompt claim. This shows that the tool-channel information was behaviorally available in at least these diagnostic cases; it does not upgrade the primary result or make S1 testable.

P003 used `thinking: disabled` because the live DeepSeek provider contract did not permit the frozen forced-tool intervention in the default thinking mode. P002 did not pin thinking mode. Therefore P002-to-P003 differences are descriptive only and cannot be causally attributed solely to the provenance-channel change.

## 2. What the three pilots jointly establish about the benchmark

### A. DCB is not a reflection detector disguised as a consciousness benchmark

PILOT_002 shows that reflection can alter later behavior while the stronger ownership-sensitive interaction remains unsupported. DCB can therefore separate generic reflective competence from the stronger self-as-self relation it is intended to test.

### B. The benchmark can return a negative result after a design weakness is repaired

PILOT_001 exposed a ceiling. PILOT_002 removed it without producing selective ownership-sensitive development. PILOT_003 then addressed the obvious prompt-label alternative by separating attribution into a registry-backed tool channel, again without producing a stable primary interaction.

This sequence is important methodologically: the benchmark was not repeatedly tuned until the target model produced a positive result.

### C. Channel exposure and authenticated self-history are not conflated

The adversarial review before PILOT_003 showed that a `role=tool` result supplied by the same API caller is still not strong authenticated provenance in the DCB sense. The final P003 preregistration therefore introduced `I1_SIM` and kept `S1 = NOT_TESTABLE`.

That claim boundary is now part of DCB v1.0.

### D. Null ownership results do not falsify DCB

DCB does not predict that current LLMs must satisfy its criteria. The benchmark specifies what evidence would be required to support progressively stronger developmental-self-reference claims.

The present result is therefore:

> **The tested model did not satisfy the stronger ownership/provenance-sensitive criteria at the interfaces that were actually testable.**

It is not:

> **The DCB theory has been falsified.**

A stronger theoretical challenge would arise if systems with genuine protected self-history and developmental continuity repeatedly failed to show the relations DCB treats as constitutive, or if purported DCB-positive effects could not be distinguished from generic prompt salience, source-reliability cues, consistency heuristics, or ordinary in-context learning.

## 3. Current empirical profile for the tested system

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

## 4. What is validated and what remains open

### Validated sufficiently for DCB v1.0 release

- stable construct and profile vocabulary;
- explicit separation of reflection, causal use, ownership sensitivity, selective transfer, and provenance-grounded self-reference;
- frozen 2×2 causal interaction as the core ownership/provenance test;
- neutral behavioral scoring that avoids the PILOT_001 ceiling;
- related/unrelated selectivity logic;
- calibration and append-only attempt discipline;
- explicit `NOT_TESTABLE` versus `NOT_DEMONSTRATED` distinction;
- interface ladder including the `I1_SIM` warning boundary;
- preregistered claim limits that prevent tool labels from being promoted to authenticated self-history.

### Not yet externally validated

- cross-model or cross-provider reliability;
- genuine I1 protected provenance;
- I2 authenticated event-chain behavior;
- I3 elective independent verification;
- persistent developmental horizon across real state continuity;
- predictive validity against an independently engineered system expected to satisfy the DCB developmental architecture.

These are applications and validation studies for the stable benchmark, not reasons to continue tuning the benchmark against DeepSeek.

## 5. Release conclusion

The appropriate endpoint after PILOT_003 is **DCB v1.0**, not PILOT_004 designed to search for a positive result in the same target.

The development sequence supports a stable benchmark that can distinguish:

> **reflection that changes behavior**

from

> **a reflection whose causal role is privileged because the system represents it as part of its own authenticated developmental history.**

The first has been observed in the development pilots. The second has not been demonstrated, and its strongest form, S1, has not yet been testable with the available interface.

Future work should therefore apply DCB v1.0 unchanged to additional models and, more importantly, to systems that genuinely implement I1/I2/I3 provenance and persistent developmental state.
