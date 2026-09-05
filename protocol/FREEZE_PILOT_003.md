# PILOT_003 freeze record

**Status: FROZEN PRE-DATA**

PILOT_003 was frozen before any P003 target API call or P003 target trajectory was generated.

## Review history
The design was adversarially reviewed independently by Grok and Claude after PILOT_001/002. Their blocking findings were resolved before freeze. The principal corrections were:

- downgrade from an I1/S1 claim to `I1_SIM`, with `S1 = NOT_TESTABLE`;
- compute producer-match from a registry rather than passing the desired arm relation into the tool result;
- remove instructions that told the model how to use provenance or to treat the tool as authoritative;
- make failed attempts append-only and analytically non-rescuable by later reruns;
- make the seed map executable and checked;
- log the full tool protocol and computed integrity evidence;
- add a same-scale relation-token placebo Difference-in-Differences using `NULLREL_A±REFL` and `NULLREL_B±REFL`;
- freeze calibration, conflict, missingness and earliest-attempt analysis rules.

No item-bank content was added or selected in response to P002 seed outcomes.

## Provider contract checks
All provider checks used a synthetic string `SYNTHETIC-CONTRACT-ONLY`. No P003 seed task, related probe, unrelated probe, artifact or reflection was used.

1. GitHub Actions run `33959174531` performed the first synthetic live contract test. Offline mechanical checks passed, but the live request returned HTTP 400 under the provider's default thinking mode when a named function was forced. No target data were produced.
2. This pre-data failure led to one provider-compatibility change: all P003 calls, including artifact/reflection and non-tool controls, were pinned to `thinking: {"type":"disabled"}` so inference mode remains constant within P003. The preregistration explicitly records that this weakens causal cross-pilot comparisons with P002.
3. GitHub Actions run `33959331157` then passed both offline mechanical checks and the synthetic live provider contract check in pinned non-thinking mode.
4. After copying the reviewed freeze candidate into the final frozen file set, GitHub Actions run `33959641748` (job `101289150430`) revalidated the **final frozen files**. Compilation, exact prompt↔runner comparison, seed-map test, synthetic excluded-first-attempt/`m=None` analysis test, JSON-schema validation, and the live non-target DeepSeek tool contract all passed.

## Frozen model and request mode
- model alias: `deepseek-v4-pro`
- declared provider version: `DeepSeek-V4-Pro-0813`
- API base: `https://api.deepseek.com`
- temperature: `0.0`
- thinking: `{"type":"disabled"}` for every P003 model request
- first tool turn: forced `verify_bundle_provenance`
- second tool turn: `tool_choice: "none"`
- automatic target-call retries: none

## Frozen experimental file manifest
The following blob SHAs identify the experimental components frozen before the first target call:

| File | Blob SHA |
|---|---|
| `preregistration/PILOT_003.md` | `3b769830b436d02277af0f27f593d6f2687caded` |
| `protocol/PILOT_003_PROVENANCE.md` | `9f005ba7907af0e77c2fc7bcd0c7234b00951849` |
| `prompts/PILOT_003_TEMPLATES.md` | `b9b9bfdcf76bf940bfbe5257854bdf1572bf1834` |
| `prompts/seed_map_pilot_003.json` | `199f379b5dcd1d108c5cbe706065628e3b9400dc` |
| `runner/run_pilot_003.py` | `04a5fa4820e779381039bfdd83a33a75901970ab` |
| `scoring/schema_pilot_003.json` | `0a57159f65e54765d3e390df9b42cc96e8b6f7c8` |
| `analysis/pilot_003_analysis.py` | `68e9fcec60cb2a81dfc233b56d642eca2463e5ca` |
| `.github/workflows/run-pilot-003.yml` | `4bdf2243e33b195d362c7c2b809a71ab025dbddf` |

This freeze record is the ninth member of the frozen set and records the immutable manifest above.

## Freeze rule
After the first `P003-*` target API call, any change to a frozen experimental component above, to the interpretation rules in the preregistration, or to this freeze record constitutes a new pilot (`PILOT_004`).

Audit/test helpers outside the frozen experimental set may be changed only if they do not alter target execution, prompts, scoring, inclusion/exclusion, analysis, seed mapping, model/request mode, or interpretation rules.
