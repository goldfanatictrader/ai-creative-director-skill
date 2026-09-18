# AI Video Failure Bible

## Camera/lens named as literal object
Symptoms:
- a specific real camera or lens brand/model named as a noun in the prompt ("shot on Sony VENICE 2", "ARRI Alexa 35") gets rendered as a physical object inside the frame
- fabricated HUD, false on-screen readouts, or watermark-style overlays appear, invented by the model to go with the "camera" it just drew

Mitigation:
- never paste a brand/model name into the generation prompt as a literal noun — see `knowledge/camera-selection-bible.md` §Critical guard
- use the registry (`libraries/camera-registry.yaml`, `libraries/lens-registry.yaml`) only to decide the look, then translate to `directorial_inference.character` adjectival language (dynamic range, color, lens character, exposure) in the actual prompt
- same rule applies to any technical-sounding proper noun a model could mistake for a drawable object, not just cameras

## Temporal color instability (AI-generated video specific)
Symptoms: skin hue drift frame to frame, wardrobe hue mutation, background palette drift, flickering highlights, local exposure pumping, inconsistent black levels, model-to-model color mismatch across shots.
Mitigation: full diagnosis/repair hierarchy (global match → tracked secondary → temporal smoothing → selective frame repair → composite replacement → regenerate) lives in `knowledge/ai-color-repair.md` — check there before attempting a color fix. Critical distinction: if the color instability follows broken anatomy/geometry (not color-only), that's a generation failure to regenerate, not a grading problem to fix — color grading must never be used to conceal a generation failure that changes story information (identity, wardrobe shape, object identity).

## Face drift
Symptoms:
- identity changes
- facial proportions drift
- age changes

Mitigation:
- reduce head rotation
- reduce duration
- strengthen reference
- avoid occlusion
- simplify camera motion

## Hands
Symptoms:
- extra fingers
- finger fusion
- changing hand shape

Mitigation:
- lock hand pose
- hide nonessential hands
- isolate important manipulation in insert shots
- reduce simultaneous body motion

## Foot skating
Mitigation:
- specify heel-to-toe transfer
- maintain ground contact
- reduce walking duration
- crop feet if not needed

## Body morphing
Mitigation:
- reduce simultaneous rotation
- lock torso or pelvis
- simplify camera
- shorten shot

## Prop mutation
Mitigation:
- canonical prop reference
- fewer handoffs
- visible uninterrupted contact
- avoid temporary disappearance

## Camera instability
Mitigation:
- one primary movement
- lock horizon
- define start/end position
- reduce geometry proximity

## Background mutation
Mitigation:
- approved location reference
- less camera parallax
- fewer background actors
- consistent scene state

## Overacting
Mitigation:
- replace emotional adjectives with observable micro-actions
- lock shoulders / hands
- define one facial change

## Phantom second limb / second person
Symptoms:
- a second arm, hand, or figure appears from off-frame partway through the clip
- keyframe and opening frames look correct — the defect only appears mid-duration

Mitigation:
- for any single-subject shot showing an arm/hand, state explicitly: "only ONE arm/hand visible throughout, no second person, no second arm or hand ever appears anywhere in frame"
- QC must sample multiple points spread across the full duration (e.g. ~20/40/60/80%), not just the first frame — this failure mode reliably passes a first-frame-only check

## Impossible mechanical geometry from extreme macro
Symptoms:
- a shot of a mechanical joint/cluster (e.g. where a mirror, housing, and grip meet) resolves into a connection that could not physically exist
- happens even with a correct reference image — the reference locks identity/texture, not structural proportion, once framing is tight enough to remove context

Mitigation:
- avoid extreme macro on more than one mechanical junction at once
- extreme macro is safe only for a single simple contact point (one hand on one lever, one foot on one pedal)
- if a result reads as "no object like this exists in the real world," retreat to a wider framing rather than adding more descriptive detail at the same crop

## Camera angle ambiguity producing an impossible position
Symptoms:
- a close shot of hand/object interaction renders from a physically impossible camera position (e.g. floating in front of a vehicle facing back toward the operator) because no explicit horizontal angle was given
- user feedback like "this angle doesn't exist in reality" without further detail is a strong signal for this specific failure

Mitigation:
- always state horizontal camera position explicitly (true side profile / first-person POV / three-quarter) — see camera-bible.md — never leave it to be inferred from a plain size+subject description

## Aspect ratio not honored despite parameter
Symptoms:
- an explicit aspect-ratio API parameter is set correctly but the model still composes toward a different ratio because the prose content of the prompt implies a different framing (e.g. "standing full body corridor shot" pulls toward portrait even when the parameter is landscape)

Mitigation:
- restate the aspect ratio explicitly in prose too, redundant with the parameter: "WIDE 16:9 HORIZONTAL LANDSCAPE (wider than tall)"

## Infrastructure failures mistaken for model failures
These are not generative-model defects but are routinely misdiagnosed as such — costly because the "fix" attempted is usually wrong.
- **Timeout ≠ failure**: a queued provider/bot job can keep processing after a local script gives up. Check the job's actual last-known status before resubmitting — resubmitting or restarting the session prematurely can cancel a job that was about to succeed.
- **Healthcheck before claiming outage**: on a generic server error, run a trivial healthcheck job first. Healthcheck fails → real outage, stop retrying, file a report. Healthcheck succeeds → the problem is in this specific request (expired asset URL, oversized prompt, bad parameter), not the provider.
- **Zombie background process holding a lock**: a process launched outside the platform's tracked-background mechanism can keep running and holding a session/lock file after its call appears to have ended, causing every subsequent call to fail with an unrelated-looking lock error. Check for and kill the process holding the lock before retrying.
- **Working-directory module shadowing**: a debug/probe script run from a shared scratch directory can be shadowed by an unrelated same-named file in that directory (e.g. a file coincidentally matching a standard-library module name), producing confusing unrelated tracebacks. Run scripts from an isolated working directory.
