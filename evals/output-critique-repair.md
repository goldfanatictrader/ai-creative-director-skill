# Eval — Output Critique & Repair Loop

Domain: what happens AFTER a shot is generated — closing the loop from raw output back to a decision, instead of treating "it generated" as "it's done." This is the step the chain in `SKILL.md` doesn't cover explicitly (the chain ends at MODEL-SPECIFIC PROMPT) — this file is what happens next, every time.

## 1. Video Critique — Check Output Against Spec, Not Against Vibes
Compare the generated result to the shot's own `generation-spec`/`shot-spec` (see `templates/shot-spec.md`), not to a general sense of whether it "looks cool":
```
identity: does it match the reference (face/object/location)?
acting: does performance match the choreographed spec (performance-bible.md), not just "looks natural"?
anatomy: hands, limbs, proportions correct throughout the DURATION (sample multiple timepoints — see ai-video-failure-bible.md)?
motion: matches intended speed/acceleration/path?
camera: matches specified angle/height/lens/movement — did it drift mid-clip?
lighting: matches intended source/direction/continuity with adjacent shots?
continuity: wardrobe/props/position match scene state (continuity-bible.md)?
physics: plausible weight, contact, secondary motion?
editability: does it have usable in/out points, or is the useful part awkwardly framed at the edges?
```
A shot that "looks great" but fails identity or continuity is a REJECT, not a "keep and fix in edit."

## 2. A/B Evaluation — Against Intent, Not Against Each Other
When comparing two candidate generations, don't just pick "the better-looking one." Score both against the shot's stated purpose (`creative_intent`, `storytelling-bible.md`) and the emotional beat it's meant to hit. A technically cleaner take that reads the wrong emotion loses to a rougher take that reads correctly — technical polish is fixable in post to a point; wrong emotional read usually isn't.

## 3. Shot Approval Memory
Once a shot is marked APPROVED (see `generation-spec.schema.json` → `generation_status`), it does not get silently regenerated or swapped later just because a new attempt "looks a bit better." Changing an approved shot is a deliberate decision, not an automatic upgrade — if a later pass produces something better, present it as a proposed change, don't substitute it silently.

## 4. Repair Decision Tree
On a failed/rejected shot, decide the repair path before touching the generator again:
```
Is the FAILURE MODE diagnosed? (per ai-video-failure-bible.md — not diagnosed = diagnose first, don't retry blind)
  → known simple fix (reframe / lock body part / add negative constraint) → apply fix, regenerate same shot
  → complexity too high → split into 2+ shots (per evals/shot-feasibility.md)
  → keyframe/reference itself was wrong → fix the keyframe first, don't regenerate video from a bad keyframe
  → provider/infra issue, not creative issue → diagnose per ai-video-failure-bible.md §3, don't change the creative approach at all
  → repeated failure (3-5x) on the same approach → change generation method/model (generation-strategy.md §3), don't keep retrying identically
```

## 5. Learning Within a Project
If a specific failure mode recurs across multiple shots in the same project (e.g. every macro shot involving this character's hands drifts), that's a pattern, not a coincidence — update the project's working notes (`generation-strategy.md` §5 convention) so later shots avoid the same setup proactively instead of rediscovering the failure each time.

## 6. When a Shot Passes
Record what worked (method, model, framing choices) in the same lightweight per-project note as failures — a working pattern is just as worth remembering as a failing one, especially for a recurring character/prop/location that will need more shots later.

## 7. Self-check
- Was the output checked against the shot's own spec, or just eyeballed?
- If rejected, is the failure mode named (per `ai-video-failure-bible.md`), and does the repair choice match that specific mode?
- If approved, is anyone about to silently swap this shot out later without flagging it as a change?
