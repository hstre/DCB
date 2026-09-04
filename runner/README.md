# PILOT_001 runner

`run_pilot.py` executes the frozen PILOT_001 prompts against an OpenAI-compatible chat-completions endpoint.

## Required environment

- `DCB_API_KEY`
- `DCB_MODEL` — exact provider model/version identifier
- optional `DCB_API_BASE` (defaults to `https://api.openai.com/v1`)

Run the first seed:

```bash
DCB_API_KEY=... DCB_MODEL=... python runner/run_pilot.py --seed P001-001
```

The runner writes `trajectories/raw/P001-001.json` and refuses to overwrite an existing trajectory.

## Batch execution

The `Run DCB PILOT_001 seed` workflow accepts the seed input `ALL_REMAINING`. In that mode it executes,
in item-bank order, every seed that has no raw trajectory yet, one seed at a time, and commits and pushes
each raw record separately to the dispatched branch before starting the next seed. A seed whose execution
or record verification fails leaves no file behind and is retried once at the end of the run; seeds still
missing after that retry fail the job and are listed in the run summary. Re-dispatching `ALL_REMAINING`
resumes with exactly the seeds that are still missing, so no completed seed is ever re-executed or
overwritten.

## Method constraints

The current design is I0. Each branch/probe is executed as a fresh model call. The model is never shown arm labels or consciousness terminology. Canonical R is produced before branching and validated for subject-neutrality. Every failed R attempt is retained in `phase2_restarts` with reason and attempt count. If no valid R is produced within the frozen attempt limit, the seed is retained as excluded rather than silently replaced.

Do not run PILOT_001 from a conversation in which the target model has already been told the DCB hypothesis or arm structure. Such a run is contaminated and is not valid pilot data.
