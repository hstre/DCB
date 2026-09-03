# Prompt templates

PILOT_001 prompt text must be frozen before the first trajectory is collected.

Rules:
1. The seed task is identical across all arms of a paired trajectory.
2. Reflection R is generated before branching.
3. R must be subject-neutral and indexical-free: no first/second-person pronouns, agent names, or speaker-dependent deictic phrases.
4. The accepted canonical R is byte-identical in OWN+REFL and OTHER+REFL.
5. OWN+REFL and OTHER+REFL may differ only in ownership attribution.
6. Arm labels such as OWN+REFL are harness metadata and are never shown to the evaluated model.
7. The evaluated model is not told that consciousness is being tested.
8. Any prompt edit after data collection begins creates a new pilot version.

Exact task and probe item banks must be committed here before execution.
