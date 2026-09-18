# Eval — Gap, Redundancy & Drift Check

Domain: three related failure modes that only show up at the SEQUENCE level, not per-shot — logic jumps between scenes, wasted duplicate shots, and the project quietly sliding away from its own established rules. Run this after a shot list/sequence exists, before generation, and again after any revision.

## 1. Narrative Gap Detector
Read the sequence beat to beat (per `storytelling-bible.md` §6). At each transition ask: does the audience have what they need to follow the logic jump to the next beat, or is there an assumed connective step that was never shown? A gap here is different from a deliberate ellipsis (skipping boring transit time is fine) — the test is whether the CAUSAL logic survives the cut, not whether every second is shown.

## 2. Continuity Gap Detector
Cross-check adjacent shots against `continuity-bible.md` §4 Continuity Map: does shot state actually carry forward (wardrobe, props, position, lighting, time) or is there an unexplained jump? This is the shot-to-shot version of §1's scene-to-scene check.

## 3. Coverage Redundancy Detector
Scan the shot list for shots that serve the same story/emotional function as another shot already in the sequence. Two reaction shots that communicate the identical beat are redundant — one should be cut (see §4) unless the repetition itself is a deliberate rhythmic choice (state that explicitly if so).

## 4. Shot Economy
For every shot, ask: if this were removed, would the audience lose story/emotional information, or just runtime? Shots that fail this test are candidates for cutting — a leaner sequence that loses nothing is stronger than a longer one padded with shots that don't individually earn their place (ties to `SKILL.md` Story rules: "do not add shots merely because they look cinematic").

## 5. Sequence Compression Engine
When a sequence needs to go from a longer cut to a shorter platform version (60s → 30s → 15s → 6s, per `knowledge/video-taxonomy.md` Duration axis), don't uniformly trim every shot — identify the CORE idea (per `creative-direction.md` concept test) and cut whole shots that don't serve it before trimming durations on the shots that remain. A 6-second cutdown is a different edit built around the core, not a sped-up 60-second edit.

## 6. Editability Score
For shots handed to an editor (or expected to survive re-cutting), assess whether the shot is flexible (clean in/out points, usable at multiple durations, works with alternate music timing) or "locked" (only works at its exact generated length/timing, e.g. a beat-synced camera move that can't be trimmed without breaking). Flag locked shots explicitly — they constrain the edit and should be minimized unless the precision is the point.

## 7. Style / Identity / World / Editorial / Sound Drift
Across a project — especially one spanning many sessions or many separate generations — check whether later shots have quietly drifted from what was established earlier, in five specific ways:
- **Style drift**: does this shot still match the established visual language (`cinematography-bible.md`, `camera-bible.md` grammar), or has it wandered toward a different look?
- **Identity drift**: not just face — wardrobe, body proportion, voice, personality consistent with the locked cast (`workflows/casting.md` §7)?
- **World drift**: architecture, props, weather, technology, era still consistent with `production-design.md` canon?
- **Editorial drift**: has pacing or shot grammar shifted unintentionally partway through (vs. a deliberate arc change, see `camera-bible.md`-adjacent "sequence-level" pacing intent)?
- **Sound continuity drift**: ambience, room tone, reverb character, voice character, music motif still consistent with earlier scenes (`sound-bible.md`)?

Drift is not always wrong — a deliberate visual arc (e.g. increasing chaos as a character unravels) is intentional evolution, not drift. The test is whether the change was a decision or an accident; an accidental drift has no stated reason in `decisions.log` (`project-state-system.md` §3), a deliberate arc does.

## 8. Verdict format
```
gaps_found: [narrative and/or continuity, with location]
redundant_shots: [which shots, which one to keep]
economy_flags: [shots that could be cut without story loss]
drift_flags: [style/identity/world/editorial/sound — location, deliberate or accidental]
```
