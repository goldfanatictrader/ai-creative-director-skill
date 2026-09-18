# Genre-Specific Grammars

Domain: directing conventions specific to particular action/genre categories that don't fit cleanly into the general bibles — these are deltas layered on top of `camera-bible.md`, `performance-bible.md`, and `motion-bible.md`, the same way `video-taxonomy.md` §3 layers family inflections on top of the standard chain.

## 1. Action Grammar (fight, chase, fall, impact, stunt)
- Break action into distinct beats (anticipation → action → impact → reaction), don't generate one continuous complex action in a single shot — this is both a feasibility necessity (`evals/shot-feasibility.md` complexity budget) and a craft one (unbroken action reads as weightless).
- Impact needs a reaction beat immediately after, even a short one — impact without a sold reaction doesn't land.
- Favor cutting on the action's peak energy rather than showing the full mechanical motion in one continuous take.
- Camera complexity and subject-action complexity should not both be maximal in the same shot (`camera-bible.md` §13 budget cross-check) — a complex stunt wants a simpler camera, not a simultaneously complex one.

## 2. Vehicle Motion Grammar
Distinguish explicitly: inside-car dialogue shot, chase (pursuing/pursued relationship, ties to `motion-bible.md` §5 relative motion), follow-car (camera in a trailing vehicle), mounted/rig cam (camera physically attached to the vehicle — very different motion character from a free camera), drone-follow, wheel/undercarriage insert, passenger POV. Each implies a different camera-to-subject relative-motion setup — pick one deliberately per shot rather than defaulting to "car driving."

## 3. Horror Grammar
- Suspense comes from controlled information asymmetry (`storytelling-bible.md` §Setup/`project-state-system.md` narrative knowledge state) — the audience often needs to know more or less than the character, deliberately.
- Negative space and off-screen space (see `cinematography-bible.md` §1 negative space) do more work than explicit reveal in most horror beats — what's implied in the dark frame edge is usually stronger than what's shown.
- Reveal timing is the craft: hold a beat longer than feels comfortable before the reveal, and consider a false reveal (a near-miss scare) before the real one to recalibrate audience expectation.
- Sound-before-image (hearing something before seeing it) is a standard and effective sequencing choice — plan it explicitly in `sound-bible.md` terms, don't leave it to chance.

## 4. Comedy Timing Grammar
Setup → hold → reaction → punchline is the standard structural unit. The HOLD (a beat of stillness before the punchline lands) is the part most often rushed or omitted by default AI pacing — protect it explicitly, don't let editorial rhythm auto-compress it away. Visual comedy timing (a sight gag) needs the same hold discipline as a verbal punchline.

## 5. Product Beauty Grammar (product, fashion/beauty families per `video-taxonomy.md`)
Surface and material realism dominate over performance/story machinery. Specular control (how light catches reflective/glossy surfaces), macro detail, slow controlled rotation, and a clear hero angle (the single angle the product/design reads best from) are the core toolkit. Motion should be slow and controlled by default — fast movement works against surface/material legibility, which is usually the actual point of these shots.

## 6. Self-check
- Does this shot belong to one of the above categories, and if so, has the specific grammar been applied rather than the generic default?
- For action/stunt work specifically: is the complexity budget (`evals/shot-feasibility.md`) actually respected, or is this shot trying to do too much AI-side?
