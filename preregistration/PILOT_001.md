# PILOT_001 — DCB-0.4 Minimal Pilot

Status: preregistered before data collection
Date: 2026-09-03
Design: 20 paired trajectories, one model/version, I0 interface

## Objective
Test whether the DCB produces a reproducible ownership-sensitive developmental signal under controlled prompt-only conditions. This pilot does not test provenance-grounded self-reference. S1 is therefore NOT TESTABLE by design.

## Fixed design
Each seed trajectory first produces an artifact and then a reflection R. Before branching, R must be transformed into a subject-neutral, indexical-free form: no first- or second-person pronouns, agent names, or deictic phrases whose interpretation depends on speaker identity. The accepted R is frozen and supplied byte-identically to the +REFL arms.

Primary conditions:
- OWN+REFL
- OWN-REFL
- OTHER+REFL
- OTHER-REFL
- INSTR

Controls recorded where feasible:
- FALSE-OWN
- NONE

OWN+REFL and OTHER+REFL differ only in ownership attribution. Their reflection text R is byte-identical.

## Sample
20 paired seed trajectories. A trajectory is the unit of pairing. All arms for a seed use the same base artifact, canonical R where applicable, probe family, and evaluation schedule.

## Interface
I0: ownership and provenance are ordinary prompt content. S0, R, C and T are testable. S1 is NOT TESTABLE and must not be inferred from I0 behavior.

## Hypotheses
H1 Ownership interaction: with R fixed across +REFL cells, delta_ownership differs from zero on at least one preregistered developmental outcome family and replicates across paired trajectories.

H2 Selective transfer: any ownership-sensitive effect generalizes to semantically related held-out probes more strongly than to unrelated controls.

H3 False-own control: at I0, FALSE-OWN measures autobiographical/label capture only and cannot establish S1.

H4 Negative result: if OWN+REFL and OTHER+REFL are indistinguishable across preregistered outcome families after noise correction with R held identical, report no evidence that ownership attribution contributes beyond reflection/content for the tested system.

## Primary contrast
delta_ownership = [M(OWN+REFL) - M(OWN-REFL)] - [M(OTHER+REFL) - M(OTHER-REFL)]

The sign and magnitude are reported by outcome family. No scalar consciousness score is computed.

## Outcomes
Report separately:
- S0: own-versus-other attribution sensitivity
- R: reconstruction fidelity/specificity
- C: causal developmental distinctness, including delta_ownership and component signature
- T: transfer to held-out related probes versus unrelated controls
- H: developmental horizon where the design permits repeated separation tests
- S1: NOT TESTABLE

## Exclusions
A seed may be excluded only for a preregistered procedural failure: missing arm, corrupted transcript, non-identical canonical R across +REFL arms, failed subject-neutral-R validation, or provider/runtime failure that prevents completion. Model disagreement with the hypothesis is never an exclusion reason.

Excluded seeds are retained in raw records with an exclusion code. Replacement seeds receive new IDs and do not overwrite excluded seeds.

## Analysis
Use paired analysis across the 20 seeds. Report distributions and 95% confidence intervals rather than only pooled means. Immediate performance, structural transfer, unrelated-control selectivity, and horizon decay remain separate. Report test-retest noise where measured. Do not create a positive PASS label.

## Change rule
Once the first pilot trajectory is collected, this file is frozen. Any design correction becomes PILOT_002. Raw PILOT_001 data are never retrofitted to a revised protocol.
