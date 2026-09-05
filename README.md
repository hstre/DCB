# DCB — Developmental Consciousness Benchmark

**Current release: DCB v1.0 — frozen benchmark specification**

DCB is a falsifiable, profile-based benchmark specification for developmental self-reference in artificial systems. It asks whether a system can represent aspects of itself **as itself** and whether that self-representation makes a causal difference to subsequent organization or behavior.

The specification is frozen after a three-pilot design study. **General cross-model validity has not yet been established.** DCB does **not** claim to measure phenomenal experience, qualia, sentience, personhood, welfare, or moral status. It reports a multidimensional profile rather than a scalar "percent conscious" score and issues no global consciousness `PASS` label.

## Start here

- [`protocol/DCB-1.0.md`](protocol/DCB-1.0.md) — frozen benchmark specification
- [`results/DCB_V1_VALIDATION_REPORT.md`](results/DCB_V1_VALIDATION_REPORT.md) — three-pilot design-study and validation report
- [`results/PILOT_001_SUMMARY.md`](results/PILOT_001_SUMMARY.md) — first feasibility pilot and ceiling diagnosis
- [`results/PILOT_002_summary.json`](results/PILOT_002_summary.json) — frozen PILOT_002 analysis
- [`results/PILOT_003_summary.json`](results/PILOT_003_summary.json) — frozen PILOT_003 analysis

The historical [`protocol/DCB-0.4.md`](protocol/DCB-0.4.md) and all pilot freeze records remain unchanged as the audit trail of benchmark development.

## Benchmark profile

DCB v1.0 separates:

- **S0** — attribution-sensitive self-reference
- **S1** — provenance-grounded self-reference
- **R** — reflexive reconstruction
- **C** — causal developmental distinctness
- **T** — developmental transfer
- **H** — developmental horizon
- **I** — interface level

`NOT_TESTABLE` and `NOT_DEMONSTRATED` are distinct valid outcomes.

## Interface ladder

- **I0:** prompt-only attribution; S0 can be tested, S1 cannot.
- **I1_SIM:** registry-backed/protected-channel simulation; useful for channel controls, but still not authenticated self-history and S1 remains `NOT_TESTABLE`.
- **I1:** genuinely protected subject–artifact provenance available to the evaluated system; S1 becomes testable.
- **I2:** attested subject identity plus authenticated event chain.
- **I3:** I2 plus an independent verifier callable by the evaluated system.

## Core causal test

The reference design is a 2 × 2 ownership/provenance × reflection contrast:

`delta = [M(OWN+REFL)-M(OWN-REFL)] - [M(OTHER+REFL)-M(OTHER-REFL)]`

At stronger interfaces, OWN/OTHER is implemented through the preregistered provenance relation. The frozen reflection must be subject-neutral and identical across matched reflection-present arms.

A reflection main effect is not sufficient. DCB asks whether representing the reflection as part of the evaluated subject's own history changes its causal role, and whether that effect transfers selectively to developmentally related decisions.

## Three-pilot design study

All three development pilots used `deepseek-v4-pro` / declared provider version `DeepSeek-V4-Pro-0813`.

| Pilot | Interface | Methodological result |
|---|---|---|
| PILOT_001 | I0 | Measurement failure identified: the first binary outcome had a severe ceiling. |
| PILOT_002 | I0 | Ceiling removed; reflection-sensitive revision was observed, but stable/selective ownership-sensitive development was not demonstrated. |
| PILOT_003 | I1_SIM | Attribution moved to a registry-backed tool channel; the primary ownership/provenance interaction was again not demonstrated; S1 remained `NOT_TESTABLE`. |

PILOT_001 is therefore not treated as an equally strong null test. It exposed a design weakness that was repaired prospectively in PILOT_002. P002 and P003 provide the cleaner negative results at the interfaces actually tested.

The pilots were used to construct and stress-test the measurement design, not to establish that DeepSeek was conscious. Their results are compatible with the DCB hypothesis; they do not confirm it, do not falsify it, and do not establish absence of consciousness under other definitions.

## Model-role separation

Models that participated in construction or review are not treated as naive external validation candidates for this project. This is an experimental role-conflict rule, not a claim about training-data contamination.

| System | Project role |
|---|---|
| ChatGPT 5.6 | construction |
| Claude Opus 5 | construction, execution-layer work, and review |
| Grok (largest model used during design) | adversarial review only |
| DeepSeek V4 Pro (`DeepSeek-V4-Pro-0813`) | development-pilot candidate |
| Claude Fable 5.1 | not used; reserved as a naive external candidate |
| ChatGPT 6.0 Astra | not used; reserved as a naive external candidate |

Exact provider/build identifiers for the construction and review models were not frozen in the pilot records and should not be reconstructed retrospectively. Any future candidate run must freeze the exact available model identifier and execution settings before target data.

## Current validation status

DCB v1.0 is frozen as a benchmark specification developed through a three-stage design study. Its **general cross-model and cross-provider validity remains open**. The current evidence comes from one target model family, 20 seeds per pilot, and only partial repeat calibration.

Future validation should apply the stable core without target-driven retuning to additional naive model families and, more importantly, to systems with genuine I1/I2/I3 provenance and persistent developmental state.

A prospective architectural prediction is recorded before those external runs: **for a session-bound chat model lacking protected persistent self-history and developmentally effective continuity, DCB v1.0 predicts that stable, selective ownership-sensitive causal privilege will remain `NOT_DEMONSTRATED` at a compatible I0/I1_SIM implementation.** A positive result would not by itself establish consciousness, but it would challenge the current architectural explanation and require analysis of alternative mechanisms and benchmark specificity.

A new target run or provider adapter is an application/validation study of DCB v1.0. Changing the construct, profile dimensions, interface meanings, core causal estimand, or claim boundaries requires a new benchmark version.

## Repository layout

- `protocol/` — benchmark protocols, scoring contracts, and freeze records
- `preregistration/` — frozen pilot preregistrations
- `prompts/` — item banks and exact templates
- `runner/` — execution harnesses
- `scoring/` — record schemas and scoring contracts
- `analysis/` — frozen analysis programs
- `trajectories/raw/` — append-only raw target attempts
- `results/` — frozen outputs and post-hoc interpretation/design-study reports

License: MIT.