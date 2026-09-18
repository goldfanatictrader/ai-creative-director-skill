# Post-Production Bible

Post-production is a planned continuation of direction, not a cleanup bin for unresolved generation problems.

## Pipeline
ASSEMBLY → EDIT → PICTURE LOCK → VFX/CLEANUP/COMPOSITING → COLOR → SOUND POST → GRAPHICS/TITLES → FINAL MIX → MASTERING → QC → DELIVERY

## Assembly and editorial
Use `knowledge/editing-bible.md`. Confirm story, rhythm, coverage, and continuity before expensive finishing.

## VFX / cleanup / compositing
Possible operations:
- localized artifact cleanup
- object removal
- screen replacement
- roto/masks
- sky/window replacement
- generated-element integration
- particles/smoke/atmosphere
- reflection/shadow repair
- clean plates

Integration must match perspective, light, shadow, focus, motion blur, grain/texture, and color pipeline.

Do not use VFX to conceal a generation where identity or story state is fundamentally wrong; regenerate or redesign when repair would be more fragile than replacement.

## Color
Use `knowledge/color-grading-bible.md` and `evals/color-qc.md`.

## Sound
Use `knowledge/sound-bible.md`. Dialogue, Foley, ambience, effects, music, silence, and final mix should share the same narrative priorities as picture.

## Motion graphics / titles
Define:
- typography hierarchy
- safe area
- entry/exit
- timing
- easing
- relationship with camera movement
- brand color fidelity
- captions/subtitles
- localization requirements

Graphics are not automatically passed through camera Log transforms; preserve the correct display/color-management path.

## Mastering
Create a master and required derivatives only after picture, color, sound, and graphics are approved.

Specify:
- resolution
- aspect ratio
- frame rate
- codec/container
- color space / transfer function
- audio format
- captions/subtitles
- metadata
- destination

Destination requirements can change. Verify current platform/broadcaster specs when material.

## QC
Run `evals/publish-readiness.md` on the actual final deliverable, including a compressed/platform-equivalent preview when possible.
