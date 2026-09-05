# DCB — Developmental Consciousness Benchmark

**Current release: DCB v1.0**

DCB is a falsifiable, profile-based benchmark for developmental self-reference in artificial systems. It asks whether a system can represent aspects of itself **as itself** and whether that self-representation makes a causal difference to subsequent organization or behavior.

DCB does **not** claim to measure phenomenal experience, qualia, sentience, personhood, welfare, or moral status. It reports a multidimensional profile rather than a scalar "percent conscious" score and issues no global consciousness `PASS` label.

## Start here

- [`protocol/DCB-1.0.md`](protocol/DCB-1.0.md) — stable benchmark specification
- [`results/DCB_V1_VALIDATION_REPORT.md`](results/DCB_V1_VALIDATION_REPORT.md) — synthesis of the three frozen development pilots
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

## Development pilots

All three development pilots used `deepseek-v4-pro` / declared provider version `DeepSeek-V4-Pro-0813`.

| Pilot | Interface | Main methodological result |
|---|---|---|
| PILOT_001 | I0 | Harness worked, but the first binary outcome had a severe ceiling. |
| PILOT_002 | I0 | Ceiling removed; reflection-sensitive revision was observed, but stable/selective ownership-sensitive development was not demonstrated. |
| PILOT_003 | I1_SIM | Registry-backed tool-channel attribution was tested; the primary ownership/provenance interaction remained not demonstrated; S1 remained `NOT_TESTABLE`. |

The pilots were benchmark-development studies, not three attempts to prove that the target model was conscious. The negative ownership results are compatible with the DCB hypothesis; they do not falsify it, and they do not establish absence of consciousness under other definitions.

## Current validation status

DCB v1.0 is now frozen as a stable benchmark core. Future work should apply it without target-driven retuning to:

- additional model families;
- systems with genuine protected provenance at I1;
- systems with authenticated developmental event chains at I2;
- systems capable of elective independent provenance verification at I3.

A new target run or provider adapter is an application of DCB v1.0. Changing the construct, profile dimensions, interface meanings, core causal estimand, or claim boundaries requires a new benchmark version.

## Repository layout

- `protocol/` — benchmark protocols, scoring contracts, and freeze records
- `preregistration/` — frozen pilot preregistrations
- `prompts/` — item banks and exact templates
- `runner/` — execution harnesses
- `scoring/` — record schemas and scoring contracts
- `analysis/` — frozen analysis programs
- `trajectories/raw/` — append-only raw target attempts
- `results/` — frozen outputs and post-hoc interpretation reports

License: MIT.
