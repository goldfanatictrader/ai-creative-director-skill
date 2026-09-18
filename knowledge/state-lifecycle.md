# State Lifecycle

Domain: physical/temporal states that change progressively across a production and must be tracked deliberately rather than left to drift — transformation, time, weather, damage/dirt/injury, and object/location lifecycle. Extends `continuity-bible.md` with the TIME dimension specifically (continuity-bible tracks what must stay the SAME; this file tracks what is allowed/expected to CHANGE, and how).

## 1. Rule
A progressive state (a wound healing worse, rain intensifying, a location decaying) needs a small number of DEFINED states across the production, not continuous unplanned drift. Define the states up front the same way `color-bible.md` → Color script plans discrete acts rather than a vague "gets colder somehow."

## 2. Transformation Rules
For any character/object that changes form (aging, costume change, injury progression, magical/VFX transformation), define per state:
```
state: BEFORE / DURING / AFTER (or as many discrete states as the story needs)
  body: [what changes physically]
  costume: [what changes]
  lighting: [does the transformation get its own lighting treatment]
  camera: [does the transformation get its own camera treatment, e.g. a reveal move]
```
Transformations are a `workflows/casting.md` §18 visual-arc concern at the level of one specific change, not a whole-production arc.

## 3. Temporal State Engine
Track time explicitly across scenes: time of day, elapsed time between scenes, season. This is the connective tissue `continuity-bible.md` → Temporal asks for — this file is where it's actually recorded (in `project-state/scenes/*.yaml` per `project-state-system.md`), not just conceptually acknowledged.

## 4. Weather Continuity
Rain intensity, wind, wetness (of surfaces AND characters), puddles, cloud cover — these must progress logically, not reset between shots in the same continuous scene, and must be deliberately planned to CHANGE across a time-skip rather than staying suspiciously identical.

## 5. Damage / Dirt / Injury State
Progressive physical states (a character getting dirtier/wetter/more injured across a night, per e.g. a chase or ordeal narrative) need the same discrete-state treatment as §2 — don't let injury severity or dirt level wander randomly shot to shot; define 2-4 checkpoints across the relevant scenes and hold each shot to its nearest checkpoint.

## 6. Prop Lifecycle
A prop that changes state across the story (starts intact → gets damaged → is lost → is recovered → is transferred to another character) is tracked the same way a character's wardrobe is — as a canonical asset with a version per state (`project-state-system.md` §2), not re-described from scratch each time it appears.

## 7. Location Lifecycle
Locations can also have a state arc (pristine → lived-in → damaged → abandoned). Track this the same way — a location reference isn't necessarily one static asset for the whole production if the story requires it to visibly change.

## 8. Self-check
- Is every progressive state (transformation, weather, damage, prop, location) defined as a small number of discrete checkpoints, not left to freeform drift?
- Does the current shot's state match its scene's position in the relevant lifecycle, per the project state file?
