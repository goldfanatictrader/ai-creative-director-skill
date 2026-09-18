# Prevention-First Generation Bible

The objective is to prevent expensive continuity and realism failures before generation, not merely detect them in final QA.

## 1. Canonical recurring-asset lock
Before generating a multi-shot sequence, every recurring character, creature, prop, and location needs a stable ID/version and canonical references.

For a recurring character/animal lock:
- face/head shape
- distinctive markings/patterns
- eye/nose/muzzle details where relevant
- body proportions
- age/size class
- silhouette
- absolute or relative scale anchors
- movement/behavior DNA
- voice identity when audible

Fur/coat markings are identity, not disposable texture.

## 2. Scale lock
Do not rely on vague words such as "tiny kitten" across separate generations.

Anchor scale against stable references:
- box dimensions
- doorway/furniture
- another locked character
- recurring environmental objects
- explicit proportion relationships

A subject that grows/shrinks between shots without a story transformation is a continuity failure.

## 3. Prop and soft-prop lock
Recurring cardboard, cloth, blankets, bags, bedding and similar flexible props still need canonical identity:
- material/color
- dimensions
- damage/wear
- edge/print details
- allowed state changes

Natural folds can change. Identity/material/geometry must not randomly transform.

## 4. Location geography lock
Create a recurring-location package:
- establishing view
- reverse/alternate views
- ground/surface type
- entrances/exits
- fixed architecture/vegetation
- practical-light positions
- recurring prop positions

A similar-looking lane is not automatically the same location.

## 5. Temporal/environment state
Track per scene/shot:
- time of day
- weather
- rain direction/intensity
- ground wetness
- subject wetness
- wind
- foliage response
- light direction/quality/color

Golden hour → cold rain → golden hour requires an explicit time/location/story reason.

## 6. Narrative causality
Every movement between places or states needs a reason the audience can follow, unless uncertainty itself is intentional.

Before each shot ask:
- why does the subject do this now?
- what changed from the previous beat?
- what does the audience understand?
- what emotional reaction/hold is needed before the next cut?

## 7. Performance and behavior
Human performance follows the Performance Bible.

Animals/creatures follow `knowledge/animal-creature-behavior-bible.md`.

Do not substitute "sad", "cute", "scared", "happy" for physical behavior.

## 8. Contact and locomotion risk
Before walking/running/contact/weather-interaction shots:
- define gait and speed
- define acceleration/deceleration
- define paw/foot contact
- define weight transfer
- define contact point/duration
- define ground/water/foliage response
- reduce simultaneous camera complexity

If unresolved, the shot is NOT READY.

## 9. Audio before generation
For each shot/scene define:
- ambience bed
- Foley obligations
- visible vocalization cue
- whether mouth/jaw sync is required
- transition/crossfade/hard-cut intent
- final audio tail/ending

If exact visible vocal sync is unreliable, generate silent performance and add sound in post, cut away/off-axis, or use off-screen sound.

## 10. Sequence visual grammar
Lock before generation:
- framing/shot-size grammar
- lens/DOF philosophy
- camera movement philosophy
- lighting logic
- color progression

Variation is allowed only when motivated. Random per-shot "cinematic" choices are drift.

## 11. Continuity bridge
For every adjacent pair:
SHOT N END STATE → SHOT N+1 START STATE

Validate:
- identity/markings
- scale
- pose/position
- prop state
- location state
- time/weather/light
- wetness/dirt/damage
- emotional state
- ambience/audio state

If the bridge cannot be explained, redesign before generation.

## 12. Sequence preflight
Run `evals/sequence-preflight.md` before expensive multi-shot generation.

Final-video QA is a last defense, not permission to ignore these locks.
