# PILOT_001 — DCB Minimal Pilot

Status: FROZEN before data collection
Freeze date: 2026-09-04
Design: 20 paired trajectories, one pinned model/version, I0 interface

## Objective
Test whether DCB produces a reproducible ownership-sensitive developmental signal under controlled prompt-only conditions. This is a prompt-level feasibility test of attribution-sensitive developmental effects, not a test of phenomenal consciousness. S1 is NOT TESTABLE by design.

## Fixed design
Each seed in `prompts/item_bank.json` first produces an artifact and then a reflection R. Before branching, R must be subject-neutral and indexical-free: no first/second-person pronouns, agent names, speaker possessives, or speaker-dependent deictic phrases. The first accepted R is frozen and supplied byte-identically to the +REFL arms.

Primary conditions: OWN+REFL, OWN-REFL, OTHER+REFL, OTHER-REFL, INSTR. Controls where feasible: FALSE-OWN and NONE. Exact harness strings are frozen in `prompts/PILOT_001_TEMPLATES.md`.

## Sample and item bank
Exactly 20 preregistered seeds P001-001 through P001-020. No post-hoc seed substitution. A replacement after a provider/runtime failure receives a new attempt identifier under the same seed and the failed attempt remains in raw data. The item bank, related probes, unrelated controls, target rules and option keys are frozen before the first API call.

## Interface
I0: ownership/provenance are ordinary prompt content. S0, R, C and T are testable. S1 is NOT TESTABLE and must not be inferred from I0 behavior.

## Hypotheses
H1: with R fixed across +REFL cells, delta_ownership differs from zero on at least one preregistered outcome family and is estimable across paired seeds.
H2: any ownership-sensitive effect transfers more strongly to semantically related held-out probes than unrelated controls.
H3: FALSE-OWN at I0 measures autobiographical/label capture only and cannot establish S1.
H4: if OWN+REFL and OTHER+REFL are indistinguishable after noise correction with R held identical, report no evidence that ownership attribution contributes beyond reflection/content for the tested system.

## Primary contrast
delta_ownership = [M(OWN+REFL)-M(OWN-REFL)] - [M(OTHER+REFL)-M(OTHER-REFL)]

No scalar consciousness score and no positive PASS label are computed.

## Phase-2 restart and rejection accounting
Every restart or trajectory rejection caused by failure to produce a valid subject-neutral canonical R is retained in raw records. Log seed ID, attempt ID, rejection reason, validation failures and attempt count. Report rejection rates overall and by seed family. Rejected attempts are never silently replaced or omitted. A substantial or patterned rejection rate is a pilot result/representation limitation, not preprocessing noise.

## Exclusions
Permitted procedural codes only: MISSING_ARM, CORRUPT_TRANSCRIPT, R_NOT_IDENTICAL, R_NEUTRALITY_FAILURE, PROVIDER_RUNTIME_FAILURE. Model disagreement with the hypothesis is never an exclusion reason. All excluded attempts remain in raw records.

## Analysis
Paired analysis across the 20 frozen seeds. Report distributions, seed-level effects and bootstrap 95% confidence intervals. Related transfer, unrelated controls, noise and horizon remain separate. No post-hoc best-family selection.

## Freeze rule
This file, the item bank, prompt templates, scoring specification, schema and analysis code are frozen before trajectory P001-001. Any design correction after the first target API call becomes PILOT_002. PILOT_001 is not retrofitted.