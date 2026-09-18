# Final Video QA Bible

Final-video QA combines temporal/semantic review with deterministic technical verification.

## Evidence classes
- observed: directly perceived in audiovisual content
- measured: established by technical tooling/signal analysis
- inferred: explanation derived from evidence

Never present inferred as measured.

## Native-video review
Prefer whole-video native inspection for story, pacing, inter-shot continuity, identity/scale drift, behavior, motion/physics, camera, color/light progression, and AV sync when audio is actually available.

Record reviewer/model, whether the entire video was reviewed, and whether audio was available.

## Deterministic QA
Where tools exist measure duration, resolution/aspect, codec/container, encoded frame-rate metadata, audio codec/sample rate/channels, loudness/true peak, and relevant black/freeze/flash/color-metadata checks.

## Cross-validation
"Motion looks choppy" is observed.
"File is 24 fps" is measured.
"Choppiness is likely generated cadence/ghosting, not an FPS drop" is inferred.

"Audio sounds distorted" is observed.
"True peak remains below clipping" is measured.
"Distortion may be in the generated source/spectral balance" is inferred.

Stereo channel count does not prove spatialized sound design.

## Timecodes and severity
Use timecodes where possible.
Severity: BLOCKER / MAJOR / MINOR / NOTE.

## Repair routes
EDIT / REGENERATE / VIDEO_REPAIR / COMPOSITE_VFX / COLOR / SOUND / MASTERING / STORY_REDESIGN.
