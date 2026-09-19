# AI Creative Director Skill

A reusable agent skill for directing generative video and film projects as a creative director rather than a prompt generator. Built for Claude Code / Claude Agent Skills, but the knowledge is model- and tool-agnostic — the same files work for any agent framework (Codex, OpenCode, custom LLM agents) that can read Markdown/YAML/JSON context files.

## Core principle

The agent must make creative decisions before writing generation prompts. Never jump directly from a vague idea to a generation prompt when creative decisions are still unresolved.

The default reasoning chain:

```
INTENT → BRIEF → VIDEO TYPE ROUTING → CREATIVE PROBLEM → CONCEPT → STORY/EXPERIENCE
→ VISUAL LANGUAGE → CHARACTER/WORLD → CANONICAL ASSET LOCKS → SCENE GEOGRAPHY/STATE
→ SEQUENCE DESIGN → SEQUENCE PREFLIGHT → BLOCKING → PERFORMANCE
→ CINEMATOGRAPHY → CAMERA → MOTION/PHYSICS → LIGHTING → SOUND → EDITORIAL RHYTHM
→ CONTINUITY → FEASIBILITY → GENERATION STRATEGY → GENERATION SPEC
→ MODEL-SPECIFIC PROMPT → OUTPUT CRITIQUE → REPAIR OR APPROVE
→ CONDITIONAL POST-PRODUCTION → PUBLISH READINESS
```

Two adversarial passes are load-bearing, not optional: `evals/creative-critic.md` (red-team the concept itself before spending generation budget) and `evals/audience-perception.md` (would a first-time viewer actually understand this, muted/blind, without the treatment document explaining it).

## What this package contains

- **`SKILL.md`** — primary operating rules and decision framework (the entrypoint)
- **`knowledge/`** — discipline bibles: storytelling, cinematography, camera, camera/lens/film-stock selection (real verified equipment specs), color (creative + full professional grading pipeline), performance, motion, continuity, production design, sound, dialogue/voice, genre-specific grammars (action/horror/comedy/product), video-type taxonomy & router, project state/versioning/dependency system, human approval gates & feedback translation, governance/locks, AI-video failure patterns, and more
- **`workflows/`** — task-specific procedures: concept development, film/narrative development, commercial, music video, social video, storyboard, casting (live-action + animation/creature/robot), professional color grading, prompt compilation
- **`schemas/`** — JSON Schema contracts for creative brief, concept, character, scene, shot, camera, performance, continuity, generation spec
- **`libraries/`** — YAML vocabularies and rule tables: camera movements + complexity scores, real camera/lens/film-stock registries with verified specs, shot grammar, emotional behaviors, failure patterns, color grading order/look archetypes/scopes reference, transitions, lighting setups
- **`evals/`** — readiness and quality checks: creative-critic (red team), audience-perception, shot-feasibility (complexity scoring), continuity-check, performance-check, gap/redundancy/drift-check, output-critique-repair, color-qc, generation-readiness, creative-quality
- **`templates/`** — reusable output templates: creative treatment, shot spec, scene state, generation spec, color grading brief
- **`examples/`** — worked examples showing the full chain from intent to compiled prompt: [`train-platform-shot.md`](examples/train-platform-shot.md) (a single shot spec end to end), [`color-grading-genre-lookbook.md`](examples/color-grading-genre-lookbook.md) (§42 genre heuristics applied as six bright/dark-tested show looks), [`camera-registry-lookbook.md`](examples/camera-registry-lookbook.md) (six camera-registry entries translated to non-branded prompt language, verified against the camera-as-object/HUD failure guard), [`realism-level-lookbook.md`](examples/realism-level-lookbook.md) (the video-taxonomy Realism-level axis rendered across six values from photoreal to motion graphics), [`vfx-compositing-lookbook.md`](examples/vfx-compositing-lookbook.md) (sky replacement, object removal, and generated-element integration tested as real reference-image edits against the post-production VFX integration checklist), [`camera-bible-lookbook.md`](examples/camera-bible-lookbook.md) (six camera height × horizontal-position combinations testing the "horizontal position is not optional" guard), [`lighting-bible-lookbook.md`](examples/lighting-bible-lookbook.md) (six light sources — window, practical lamp, fluorescent, fire, vehicle headlights, neon signage — each fully parameterized per the lighting bible), [`composition-bible-lookbook.md`](examples/composition-bible-lookbook.md) (centering, negative space, compression, and wide depth tested against their claimed psychological effects), and [`performance-bible-lookbook.md`](examples/performance-bible-lookbook.md) (abstract-adjective vs. behavior-translation, and restrained vs. forbidden-overacting, tested as paired A/B comparisons)
- **`sources/`** — official manufacturer/technical sources backing the camera/lens/film/color registries (facts vs. directorial heuristics are labeled separately throughout)

## Explicit scope boundary

This skill makes creative and technical **decisions**. It does not execute them. Actual image/video generation, editing, VFX compositing, color-grading execution, audio mixing, and encoding require real tools (a video-gen API, an NLE, a grading application) wired up per-project — this skill produces the specs, prompts, and QC judgment that feed those tools, not the tools themselves.

## A hard-won rule this package encodes

Never paste a real camera/lens brand or model name into a generation prompt as a literal noun ("shot on Sony VENICE 2"). Confirmed failure mode: the model renders the camera itself as a physical object in frame, often with a fabricated HUD or watermark-style overlay. Use the camera/lens registries to make a *decision* about image behavior, then translate to adjectival, non-branded language in the actual prompt. See `knowledge/camera-selection-bible.md` and `knowledge/ai-video-failure-bible.md`.

## Installation

Copy this folder into your agent's skills directory (for Claude Code: `~/.claude/skills/creative-director/` or a project's `.claude/skills/`), with a `SKILL.md` frontmatter block (`name`, `description`) so the host can discover and trigger it. For other agent frameworks, point the agent at `SKILL.md` as its entrypoint and let it navigate the rest via the file references embedded throughout.

## Versioning

This package grows by accretion, but repository QA is expected to prevent silent drift. `.github/workflows/qa.yml` runs `scripts/qa_repo.py` to check JSON/YAML parsing, JSON-Schema validity, broken internal file references, schema readiness contracts, manifest consistency, and FILE_INDEX drift. See `FILE_INDEX.md` for the generated current file list.


## Prevention-first generation

v1.3 treats recurring identity, markings, scale, props, location geography, time/weather/light, narrative motivation, animal/creature behavior, audio-sync planning, ambience/Foley, and emotional ending design as pre-generation constraints. Final-video QA is a last defense, not the first time continuity is checked.

Final-video review combines native temporal/video vision when available with deterministic technical verification; perceptual observations and measured file facts are kept separate.
