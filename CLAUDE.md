# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not application code — it is a portable **Claude/Agent Skill package**: a directed knowledge base of Markdown/YAML/JSON files that an LLM agent reads to act as an "AI Creative Director" for generative video/film production (concept → shots → prompts → QA). There is no runtime application; the only executable is a repo QA/lint script. Content is model- and framework-agnostic (works for Claude Code, Codex, OpenCode, etc.).

`SKILL.md` is the entrypoint (has the Claude Agent Skills frontmatter: `name`, `description`). Everything else is reference material the agent navigates via explicit file paths embedded in `SKILL.md` and the other docs.

## Commands

Repository QA (the only "build/test" in this repo) validates schema/reference/manifest integrity — run it after any edit to `schemas/`, `libraries/`, `templates/`, `manifest.json`, `FILE_INDEX.md`, or files referenced by path elsewhere:

```bash
python -m pip install --upgrade jsonschema PyYAML   # first time / if missing
python scripts/qa_repo.py
```

`scripts/qa_repo.py` checks, in order:
- every `schemas/*.json` file is valid JSON Schema (Draft 2020-12)
- every `libraries/*.y*ml` and `templates/*.y*ml` file parses as YAML
- `manifest.json`'s `folders` all exist and `entrypoint` is `SKILL.md`
- every in-repo path reference matching `(knowledge|workflows|evals|schemas|libraries|templates|examples|sources)/<name>.<md|json|yaml|yml>` found anywhere in `.md`/`.json`/`.yaml`/`.yml`/`.py` files actually exists (broken-link check)
- `FILE_INDEX.md` exactly matches the tracked file set (no missing/extra entries)
- fixed "regression contracts" hard-coded in the script itself: `shot.schema.json` and `generation-spec.schema.json` must keep specific required fields and readiness conditionals; `templates/generation-spec.yaml`, `templates/shot-spec.md`, and `examples/train-platform-shot.md` must stay in sync with those schemas; certain prevention/QA files must keep existing; `SKILL.md` must retain certain phrases and keep `GENERATION STRATEGY` before `GENERATION SPEC` in the pipeline chain; `workflows/shot-design.md` must reference the animal-behavior bible and mention a continuity bridge.

CI (`qa.yml` under `.github/workflows/`) runs exactly this script on push/PR to `main`. There is no other lint, build, or test suite.

Note: this QA script currently has a known false-positive — its broken-reference regex matches the last two path segments of the CI workflow file wherever that path is spelled out in full in prose (e.g. in `README.md` and `FILE_INDEX.md`), so a `QA FAILED` with only that one complaint pre-dates any given change and isn't something to chase.

## Making changes safely

- **After adding/removing/renaming any tracked file**, update `FILE_INDEX.md` to match — QA fails on drift. It's a flat backtick-quoted list of every tracked repo-relative path except itself.
- **After adding a new folder that content lives in**, add it to `manifest.json`'s `folders` array.
- Any time you write a path like `knowledge/<name>.md` (or under `workflows/`, `evals/`, `schemas/`, `libraries/`, `templates/`, `examples/`, `sources/`) inside a `.md`/`.json`/`.yaml`/`.py` file, that file must actually exist — the QA script greps for this pattern repo-wide and fails on dangling references. Don't reference a file before creating it in the same change.
- If you touch `schemas/shot.schema.json`, `schemas/generation-spec.schema.json`, `templates/generation-spec.yaml`, `templates/shot-spec.md`, `examples/train-platform-shot.md`, or `SKILL.md`'s pipeline chain / key phrases, check `scripts/qa_repo.py`'s hard-coded regression assertions (bottom half of the file) — these encode intentional content contracts, not just structure, and editing the referenced files without updating the assertions (or vice versa) breaks QA.
- Run `python scripts/qa_repo.py` before considering an edit done whenever it touches any file under `schemas/`, `libraries/`, `templates/`, `examples/`, `manifest.json`, or `FILE_INDEX.md`.

## Architecture: the decision chain

The skill's core idea (stated in `SKILL.md` and `README.md`) is that the agent must resolve creative decisions in a fixed order before ever writing a generation prompt — never jump straight from an idea to a prompt:

```
INTENT → BRIEF → VIDEO TYPE ROUTING → CREATIVE PROBLEM → CONCEPT → STORY/EXPERIENCE
→ VISUAL LANGUAGE → CHARACTER/WORLD → CANONICAL ASSET LOCKS → SCENE GEOGRAPHY/STATE
→ SEQUENCE DESIGN → SEQUENCE PREFLIGHT → BLOCKING → PERFORMANCE
→ CINEMATOGRAPHY → CAMERA → MOTION/PHYSICS → LIGHTING → SOUND → EDITORIAL RHYTHM
→ CONTINUITY → FEASIBILITY → GENERATION STRATEGY → GENERATION SPEC
→ MODEL-SPECIFIC PROMPT → OUTPUT CRITIQUE → REPAIR OR APPROVE
→ CONDITIONAL POST-PRODUCTION → PUBLISH READINESS
```

Two adversarial evals are load-bearing (not skippable) before generation: `evals/creative-critic.md` (red-team the concept) and `evals/audience-perception.md` (would a first-time, muted/blind viewer actually understand it). After every generation, `evals/output-critique-repair.md` governs approve/repair/escalate.

### How the folders relate

- **`SKILL.md`** — the operating rules and the chain above; the only file an agent is guaranteed to read first. It cross-references everything else by explicit path — that's the navigation mechanism, there's no index/loader code.
- **`knowledge/*.md`** — discipline "bibles" (cinematography, camera, color, performance, motion, continuity, sound, production design, genre grammars, video taxonomy/router, AI-video failure patterns, model capabilities, etc.). These are prose decision frameworks, read on demand per the chain stage.
- **`libraries/*.yaml`** — structured vocabularies/rule tables backing the bibles: real camera/lens/film-stock registries with verified specs, shot grammar, emotional behaviors, lighting setups, color grading order, failure-pattern catalogs, model capability registry.
- **`schemas/*.json`** — JSON Schema (Draft 2020-12) contracts for the structured artifacts the agent produces mid-chain (creative brief, concept, character, scene, shot, camera, performance, continuity, generation spec). `shot.schema.json` and `generation-spec.schema.json` encode "readiness" gating via `allOf` conditionals — see QA notes above.
- **`templates/*`** — fill-in-the-blank output shapes matching the schemas (shot spec, scene state, generation spec, creative treatment, color grading brief).
- **`workflows/*.md`** — task-specific procedures per video-type family (concept development, film/narrative, commercial, music video, social video, storyboard, casting, professional color grading, prompt compilation, final video QA). `knowledge/video-taxonomy.md` decides which workflow(s) apply to a given brief.
- **`evals/*.md`** — the QC/readiness gates run at specific chain stages (creative-critic, audience-perception, shot-feasibility, continuity-check, performance-check, sequence-preflight, generation-readiness, output-critique-repair, color-qc, final-video-qa, publish-readiness, gap/redundancy/drift-check).
- **`examples/*.md`** — worked end-to-end traces from intent to compiled prompt; kept in sync with the schemas by QA.
- **`sources/official-sources.md`** — citations backing factual claims (real camera/lens/film specs) in the registries, kept separate from directorial heuristics.

### Key cross-cutting rules baked into `SKILL.md` worth knowing before editing content

- **Never let a real camera/lens brand/model name reach a final generation prompt as a literal noun** (confirmed failure mode: the model renders the physical camera/HUD in-frame). Registries (`libraries/camera-registry.yaml`, `lens-registry.yaml`, `film-stock-registry.yaml`, `camera-lens-pairing.yaml`) are for making a decision about image *behavior*; translate to non-branded adjectival language via `directorial_inference.character` before it reaches a prompt. See `knowledge/camera-selection-bible.md` and `knowledge/ai-video-failure-bible.md`.
- **GENERATION STRATEGY (method/model choice) must precede GENERATION SPEC** (execution parameters) — this ordering is enforced both narratively in `SKILL.md` and mechanically by `scripts/qa_repo.py`.
- **Prevention-first**: multi-shot sequences must lock canonical identity/scale/props/location/time-weather/motivation/continuity bridges *before* generation, not fix them via QA after (`knowledge/prevention-first-generation.md`, `evals/sequence-preflight.md`).
- Scope boundary: this skill produces creative/technical **decisions, specs, and prompts** — it does not execute generation, editing, grading, mixing, or encoding; those require real tools wired up per-project.

## Versioning

The package grows by accretion (see `manifest.json` version and README's "Prevention-first generation" section for the current version's focus). `FILE_INDEX.md` is the generated/maintained inventory truth source — always regenerate/edit it by hand to match tracked files rather than letting it drift, since QA enforces exact equality.
