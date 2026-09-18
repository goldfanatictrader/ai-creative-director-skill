# AI Creative Director Skill

A reusable agent skill for directing generative video and film projects as a creative director rather than a prompt generator. Built for Claude Code / Claude Agent Skills, but the knowledge is model- and tool-agnostic — the same files work for any agent framework (Codex, OpenCode, custom LLM agents) that can read Markdown/YAML/JSON context files.

## Core principle

The agent must make creative decisions before writing generation prompts. Never jump directly from a vague idea to a generation prompt when creative decisions are still unresolved.

The default reasoning chain:

```
INTENT → BRIEF → VIDEO TYPE ROUTING → CREATIVE PROBLEM → CONCEPT → STORY/EXPERIENCE
→ VISUAL LANGUAGE → CHARACTER/WORLD → SCENE DESIGN → BLOCKING → PERFORMANCE
→ CINEMATOGRAPHY → CAMERA → MOTION/PHYSICS → LIGHTING → SOUND → EDITORIAL RHYTHM
→ CONTINUITY → FEASIBILITY → GENERATION SPEC → GENERATION STRATEGY
→ MODEL-SPECIFIC PROMPT → OUTPUT CRITIQUE → REPAIR OR APPROVE
```

Two adversarial passes are load-bearing, not optional: `evals/creative-critic.md` (red-team the concept itself before spending generation budget) and `evals/audience-perception.md` (would a first-time viewer actually understand this, muted/blind, without the treatment document explaining it).

## What this package contains

- **`SKILL.md`** — primary operating rules and decision framework (the entrypoint)
- **`knowledge/`** (30 files) — discipline bibles: storytelling, cinematography, camera, camera/lens/film-stock selection (real verified equipment specs), color (creative + full professional grading pipeline), performance, motion, continuity, production design, sound, dialogue/voice, genre-specific grammars (action/horror/comedy/product), video-type taxonomy & router, project state/versioning/dependency system, human approval gates & feedback translation, governance/locks, AI-video failure patterns, and more
- **`workflows/`** (10 files) — task-specific procedures: concept development, film/narrative development, commercial, music video, social video, storyboard, casting (live-action + animation/creature/robot), professional color grading, prompt compilation
- **`schemas/`** (9 files) — JSON Schema contracts for creative brief, concept, character, scene, shot, camera, performance, continuity, generation spec
- **`libraries/`** (16 files) — YAML vocabularies and rule tables: camera movements + complexity scores, real camera/lens/film-stock registries with verified specs, shot grammar, emotional behaviors, failure patterns, color grading order/look archetypes/scopes reference, transitions, lighting setups
- **`evals/`** (10 files) — readiness and quality checks: creative-critic (red team), audience-perception, shot-feasibility (complexity scoring), continuity-check, performance-check, gap/redundancy/drift-check, output-critique-repair, color-qc, generation-readiness, creative-quality
- **`templates/`** (5 files) — reusable output templates: creative treatment, shot spec, scene state, generation spec, color grading brief
- **`examples/`** (2 files) — worked examples showing the full chain from intent to compiled prompt
- **`sources/`** — official manufacturer/technical sources backing the camera/lens/film/color registries (facts vs. directorial heuristics are labeled separately throughout)

## Explicit scope boundary

This skill makes creative and technical **decisions**. It does not execute them. Actual image/video generation, editing, VFX compositing, color-grading execution, audio mixing, and encoding require real tools (a video-gen API, an NLE, a grading application) wired up per-project — this skill produces the specs, prompts, and QC judgment that feed those tools, not the tools themselves.

## A hard-won rule this package encodes

Never paste a real camera/lens brand or model name into a generation prompt as a literal noun ("shot on Sony VENICE 2"). Confirmed failure mode: the model renders the camera itself as a physical object in frame, often with a fabricated HUD or watermark-style overlay. Use the camera/lens registries to make a *decision* about image behavior, then translate to adjectival, non-branded language in the actual prompt. See `knowledge/camera-selection-bible.md` and `knowledge/ai-video-failure-bible.md`.

## Installation

Copy this folder into your agent's skills directory (for Claude Code: `~/.claude/skills/creative-director/` or a project's `.claude/skills/`), with a `SKILL.md` frontmatter block (`name`, `description`) so the host can discover and trigger it. For other agent frameworks, point the agent at `SKILL.md` as its entrypoint and let it navigate the rest via the file references embedded throughout.

## Versioning

This package grows by accretion — new knowledge/eval/workflow files get added as gaps are found in real use, cross-referenced from `SKILL.md` and from each other. See `FILE_INDEX.md` for the current full file list.
