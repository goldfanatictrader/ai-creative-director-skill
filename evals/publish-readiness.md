# Eval — Publish Readiness

A rendered or edited video is not publish-ready until all six gates pass. When an actual assembled/master-candidate file exists, run `evals/final-video-qa.md` first and feed its cross-validated findings into these gates.

## 1. Creative gate
- brief objective is still satisfied
- intended audience can understand the core message
- emotional/narrative arc works without treatment-document explanation
- opening and ending work
- no approved creative lock was silently lost

## 2. Continuity gate
- character identity / voice / wardrobe consistent
- prop lifecycle valid
- location/world state valid
- screen direction / eyelines valid where applicable
- time/weather/light progression valid
- no unresolved continuity issue is hidden by editing

## 3. Technical gate
- no unacceptable anatomy / morph / flicker / geometry artifact
- no broken lip sync where visible dialogue matters
- no unexpected dropped/duplicate/black/flash frames
- color is temporally stable
- audio has no unintended clipping/distortion
- subtitles/graphics render correctly

## 4. Editorial gate
- pacing and shot order communicate the intended information
- cuts have usable motivation
- reactions land
- audio transitions are intentional
- no redundant shot remains solely because it looks impressive
- picture lock state is respected

## 5. Delivery gate
Verify against the actual destination:
- resolution
- aspect ratio
- frame rate
- codec / container
- bitrate or mezzanine requirement
- color space / transfer function
- audio codec / sample rate / channel layout
- subtitle/caption format
- safe areas / platform crops
- HDR/SDR variant requirements

Do not invent platform specifications; verify current requirements when material.

## 6. Legal / brand gate
This skill may flag but does not independently clear legal risk:
- likeness / releases
- music / footage / asset rights
- trademark use
- claims / regulated content
- brand guidelines
- required disclosures / credits

## Verdict
- all six pass → `PUBLISH READY`
- any creative/continuity/technical/editorial/delivery gate fails → `NOT PUBLISH READY`
- legal/brand clearance unresolved → `CREATIVELY READY / AWAITING CLEARANCE`

Record unresolved items explicitly. Do not silently downgrade a blocking issue into a note.
