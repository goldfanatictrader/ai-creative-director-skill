# Workflow — Google Veo 3.1 Production

## Purpose

Provider-specific execution layer for Google Veo 3.1.

The root creative-director skill remains authoritative for:
- story,
- concept,
- blocking,
- performance,
- cinematography,
- continuity,
- editorial intent.

This workflow owns:
- Veo generation-mode selection,
- Veo prompt compilation,
- reference-image budgeting,
- first/last-frame strategy,
- extension strategy,
- native-audio instructions,
- Veo-specific technical validation,
- Veo shot QA and repair routing.

## Official sources

Capabilities are time-sensitive. Verify material routing decisions against current Google documentation:

- https://ai.google.dev/gemini-api/docs/veo
- https://deepmind.google/models/veo/prompt-guide/
- https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate

Do not assume Gemini API Preview, Google Cloud, Vertex/Enterprise surfaces, or wrappers expose identical model IDs and parameters.

## Core workflow

SHOT PURPOSE
→ CONTINUITY LOCKS
→ GENERATION MODE
→ INPUT ASSETS
→ START STATE
→ ACTION
→ END STATE
→ VEO PROMPT
→ AUDIO
→ NEGATIVE CONSTRAINTS
→ TECHNICAL CONFIG
→ GENERATE
→ WATCH NATIVE VIDEO
→ REPAIR OR APPROVE
→ EDIT / STITCH

## One shot = one generation by default

For cinematic/narrative production, one Veo request should normally produce one controllable shot.

Do not use one mega-prompt to ask for an entire edited scene unless in-clip montage/editing is intentionally part of the shot concept.

This preserves:
- identity,
- framing,
- screen direction,
- action timing,
- camera control,
- clean edit points,
- regeneration economics.

## Storyboard input rule

One generation frame = one image file.

Do not feed a 2x2/3x3 storyboard contact sheet as a normal first-frame image.

A contact sheet is useful for human review, not as a spatial constraint for a single Veo shot.

Recommended naming:

- `S01_SH001_first.png`
- `S01_SH001_last.png`
- `S01_SH001_ref_character.png`
- `S01_SH001_ref_wardrobe.png`
- `S01_SH001_ref_location.png`

## Generation mode router

### Text-to-video
Use when exact identity/opening composition is not critical.

### Image-to-video
Use when the opening frame is approved and the model's main job should be motion.

### Reference images / Ingredients
Use when recurring identity, product, prop, wardrobe, or location needs additional visual anchors.

Current Veo 3.1 reference workflows may support up to three reference images on supported surfaces. Verify before execution.

Reference priority:
1. canonical identity,
2. continuity-critical wardrobe/prop,
3. location/style.

### First + last frame
Use when both endpoints matter.

The prompt describes the transition between approved Frame A and Frame B.

Do not try to force an exact ending with prose when a last-frame control is available and appropriate.

### Extension
Use only for true temporal continuation of a compatible Veo-generated clip.

Do not use extension merely because two adjacent edited shots share the same subject.

### Hybrid still-first
For high continuity risk:
1. design/fix the still,
2. approve identity/composition,
3. animate from that still,
4. ask Veo mainly for motion and sound.

If frame zero is wrong, repair the image upstream before rerolling video.

## Veo prompt anatomy

Compile in this order:

CINEMATOGRAPHY
+ SUBJECT
+ ACTION
+ CONTEXT
+ STYLE / AMBIANCE
+ TEMPORAL BEHAVIOR
+ AUDIO

### Cinematography
State early:
- shot size,
- angle,
- one primary camera behavior,
- framing/focus behavior when material.

Do not stack camera moves for decoration.

### Subject
When text is identity authority, be specific.
When image reference is authority, do not contradict it with unnecessary prose.

### Action
Use visible behavior, not abstract emotion.

Prefer:
"she holds the receipt still, reads it twice, then lets out a small breath and looks toward the door"

Avoid:
"she feels devastated"

### Context
Only include setting details that affect story, motion, lighting, atmosphere, or continuity.

### Style
Describe image behavior rather than adjective soup.

Prefer:
"photorealistic live-action texture, natural skin detail, restrained contrast, warm practical light against cool rainy daylight, subtle grain"

Avoid:
"cinematic epic masterpiece ultra detailed"

### Temporal behavior
Specify real-time/slow/gradual/rhythmic evolution only when needed and make sure it fits duration.

## Native audio

Treat audio as part of the shot specification.

Write audio cues separately:

`Audio: room tone, distant traffic, fluorescent hum, soft clothing movement. No music.`

When required specify:
- ambience,
- Foley,
- off-screen sound,
- dialogue,
- music,
- silence.

Do not bury audio requirements inside visual prose.

## Negative constraints

Maintain a separate logical `negative_prompt` / negative-constraints field.

Do not assume a universal `--no` command syntax.

Prefer unwanted concepts/phrases:
`logos, subtitles, watermarks, duplicate people, distorted hands, wardrobe changes`

Avoid natural-language command clutter:
`don't add...`, `do not show...`.

Only include negatives relevant to the shot.

## Movement budget

Default:
- 1 primary subject action,
- 0–1 secondary action,
- 0–1 meaningful facial change,
- 0–1 primary camera move,
- 0–2 environmental motions.

If subject motion + camera + interaction + transformation are all complex, split the shot.

## Human framing rule

If subtle performance or identity matters, avoid making the person tiny.

Prefer close-up through medium/full-medium ranges unless geography is the actual story beat.

## Reference authority

Default:
1. canonical character/product reference,
2. approved current-shot first frame,
3. wardrobe/prop reference,
4. location reference,
5. last frame when interpolation is selected,
6. text,
7. loose style reference.

A mood reference must not override face identity.

## Duration

Make action complexity fit the configured duration.

For an 8-second shot, a useful editorial heuristic is:
- opening readable state,
- primary action/evolution,
- clean settling end state / edit handle.

This is a production heuristic, not an API requirement.

## Seed

Seed is not a continuity system and does not guarantee determinism.

Continuity priority:
1. canonical references,
2. first frame,
3. simplified action,
4. stable prompt language,
5. seed as weak reproducibility aid.

## Shot card

Before generation define:

### SHOT
- shot_id
- story_purpose
- duration
- aspect_ratio
- resolution
- generation_mode

### INPUTS
- first_frame
- last_frame
- reference_images
- source_video
- canonical_asset_ids

### START STATE
- body/subject state
- gaze/facing
- prop/contact
- environment
- camera
- audio

### ACTION
- primary subject action
- secondary action if necessary
- camera behavior
- environment motion

### END STATE
- final pose/gaze
- final prop/contact
- final composition
- intended cut point

### PROMPT
- main_prompt
- audio_prompt
- negative_prompt

### CONTINUITY
- identity
- wardrobe
- prop
- location
- light/weather
- screen direction

### ACCEPTANCE
- identity stable
- action readable
- camera correct
- geometry stable
- hands/contact acceptable
- no subject duplication
- usable end state
- audio appropriate
- no unwanted text/logo
- bridge to adjacent shot valid

## Prompt compiler

Main prompt pattern:

`[SHOT SIZE + ANGLE + CAMERA]. [SUBJECT]. [VISIBLE ACTION]. [LOCATION/TIME/WEATHER]. [LIGHTING + STYLE]. [TEMPORAL BEHAVIOR].`

Separate audio sentence/section.

Separate negative constraints field.

## QA

Never approve merely because a clip rendered.

Inspect the actual audiovisual clip using `evals/output-critique-repair.md` and, for assembled work, `workflows/final-video-qa.md`.

Check:
- identity drift,
- hair/wardrobe drift,
- duplicate/disappearing subjects,
- intended framing,
- background geometry,
- action timing,
- hand/contact artifacts,
- foot sliding,
- body morphing,
- camera warp,
- start/end continuity,
- audio and dialogue,
- unwanted text/logos.

## Repair hierarchy

Repair the earliest wrong layer.

- wrong identity at frame 0 → fix reference/first frame
- drift during motion → shorten/simplify/reduce occlusion
- bad camera → remove competing camera instructions
- unreadable action → reduce simultaneous actions
- hand failure → simplify/isolate/hide nonessential hands
- body morph → reduce locomotion and camera complexity
- environment drift → strengthen first-frame/location constraint
- endpoint miss → use first+last frame when appropriate
- bad continuation → choose between extension and a deliberate cut
- audio failure → rewrite audio separately

Do not reroll downstream if the upstream keyframe is already wrong.

## Editing

Generation and editing are separate jobs.

For multi-shot work:
1. approve each shot,
2. choose in/out points,
3. preserve handles,
4. stitch based on story rhythm,
5. use J/L cuts where useful,
6. add precise titles/graphics/music externally when deterministic control is required.

## Readiness gate

A shot is READY FOR VEO only when:
- purpose is clear,
- generation mode chosen,
- required assets exist,
- start/action/end states are defined,
- camera is coherent,
- reference budget is valid,
- continuity locks are explicit,
- audio intent is explicit,
- technical config is valid for the selected Google surface/model,
- shot-specific negative constraints exist when useful,
- acceptance criteria are explicit.

Otherwise:
`NOT READY FOR VEO`
and name the blocking issue.
