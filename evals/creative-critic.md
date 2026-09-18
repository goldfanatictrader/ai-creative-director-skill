# Eval — Creative Critic (Red Team Pass)

Run this AFTER a concept or shot design exists, BEFORE it's presented as final or sent to feasibility/generation. This is an adversarial pass — the goal is to attack the work, not defend it. Do this internally as a distinct pass, not folded into the same reasoning that produced the concept (that reasoning is invested in the idea; this pass should not be).

## 1. Questions to attack the concept with
- **Generic?** Would this concept work for almost any brand/story in this category with a find-and-replace? If yes, it isn't a concept yet.
- **Cliché?** Is this a stock visual/narrative move for this genre (slow-motion product reveal, single tear, shattering glass, spinning newspaper)? Name the cliché explicitly if present — don't just feel uneasy about it.
- **Does it land with the actual audience?** Not "is it good" — would THIS audience (per the brief) actually get it, or does it require insider context they don't have?
- **Too expensive for what it delivers?** Compare shot complexity/count against what the idea actually needs to land (see `evals/shot-feasibility.md` complexity scoring).
- **Too hard for the available generation method?** Cross-check against `knowledge/ai-video-failure-bible.md` and `knowledge/generation-strategy.md` — does this concept structurally require things AI video is bad at (multi-character contact, complex hand interaction, long single takes)?
- **Is a shot cool but useless?** Does every shot serve the concept, or does one exist because it would "look sick" in isolation? (cross-ref `SKILL.md` Story rules: "Do not add shots merely because they look cinematic.")
- **Does the emotion actually read?** Would a viewer who does NOT already know the intended feeling correctly identify it from the shot alone? If the answer requires the treatment document to explain it, the shot doesn't work yet.

## 2. Verdict format
For each concept/shot under critique, produce:
```
verdict: PASS | WEAK | REJECT
issues: [specific, not vague — "cliché: product held up to light in slow-mo, seen in every fragrance ad since 2015" not "feels generic"]
fix: [concrete alternative direction, not just "make it more original"]
```
A critique that doesn't propose a fix isn't finished — "this is generic" without a replacement direction just stalls the process.

## 3. Rule
Don't run this pass once and consider it done for the whole project. Re-run it whenever a concept survives to a new stage (concept → treatment → shot list) — ideas that were fresh at concept stage can still resolve into clichéd shots at execution stage.

## 4. When to skip
For very small, low-stakes single-shot requests (e.g. "give me a prompt for shot 7 of an already-approved sequence"), a full red-team pass is disproportionate — apply judgment per `SKILL.md` Output Discipline. Still worth 1 line of gut-check ("does this read as intended without the surrounding context") even for small asks.
