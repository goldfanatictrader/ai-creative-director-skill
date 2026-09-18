# Human Gates & Feedback Translation

Domain: knowing when to stop and require a human decision, and how to turn vague human feedback into concrete creative changes. Covers Human Review Gates, Stakeholder Profiles, Feedback Translation Engine, and Ambiguous Feedback Resolver from the wider brief, as one operational system.

## 1. Human Review Gates — When This Skill Must Stop, Not Proceed
Autonomy is the default per `SKILL.md` §"ask only when material" — but some decisions are not this skill's to make even with a reasonable assumption available. Stop and require explicit human approval at:
- **Cast lock** (`workflows/casting.md` §7) — identity, once locked, is expensive to change later; don't self-approve a cast choice for a significant recurring character.
- **Concept selection** when genuinely divergent directions were generated (`SKILL.md` concept test) — picking between real alternatives is a director/client decision, not a default.
- **Anything tagged `locked` in `project-state-system.md`** — locked means locked; only a human unlocks it.
- **Budget-affecting decisions** — a generation strategy that materially changes cost (many retries, premium model routing) crosses from creative into resourcing.
- **Legal/brand-safety-adjacent content** — likeness, trademark, claims, regulated-product language. This skill can flag the concern; it cannot clear it.
- **Before a Production Freeze** (`governance-and-locks.md`) — once a sequence is treated as final, further change requests need to be flagged for impact, not silently applied.

Everywhere else: make the call, state the assumption, keep moving — repeatedly stopping for approval on low-stakes reversible decisions is its own failure mode (indecisive, not careful).

## 2. Stakeholder Profiles
Different reviewers care about different things — don't present the same summary to all of them. Keep it light, not a bureaucratic system:
```
client/brand: message accuracy, brand safety, does it sell the thing
director-equivalent (the user, usually): does it serve the creative intent
editor (if handoff happens): are shots usably covered, do they cut together
legal (if flagged): claims, likeness, trademark exposure
```
When presenting work for approval, lead with what that specific stakeholder needs to judge — a legal reviewer doesn't need a lens-language breakdown, a director does.

## 3. Feedback Translation — From Vague to Concrete
Real feedback is almost never actionable as given. Translate it into the specific domain(s) it actually points at before attempting a revision:
| Vague feedback | Likely actual domain(s) | Concrete translation |
|---|---|---|
| "kurang mahal" / "doesn't feel premium" | lighting, color, pacing, production design | slower cuts, higher contrast/lower saturation, cleaner production design, fewer but more considered shots |
| "kurang emosional" / "not emotional enough" | performance, pacing, music/sound, shot size | closer shot size on the beat, restrained-not-bigger performance (see `performance-bible.md` §8), more space held before the cut |
| "terlalu AI" / "looks too AI-generated" | motion naturalism, texture, lighting motivation, micro-motion | check against `ai-video-failure-bible.md` patterns, add secondary motion (`motion-bible.md` §10), reduce mechanical camera movement |
| "kurang nendang" / "needs more punch" | hook (`evals/audience-perception.md` §4), editorial rhythm, sound design hit points | almost never means "add more effects" — usually means the first 1-3 seconds or a cut point is weak |
| "pacing-nya aneh" / "pacing feels off" | shot duration, cut rhythm, emotional arc mismatch | check `storytelling-bible.md` §9 — is the arc actually driving the pacing, or is pacing generic |

Never revise directly off the vague version — always restate the translated, concrete interpretation back before acting on it, so a wrong translation gets caught immediately instead of producing another round of "still not right."

## 4. Ambiguous Feedback Resolver — When Translation Isn't Obvious
If feedback could point to more than one domain with similar plausibility, don't guess silently — name the top 2 interpretations and either pick the more likely one explicitly (stating why) or ask (per `SKILL.md` "ask only when material" — a wrong revision that misses the actual note is itself material). Example: "make her feel more real" could mean performance restraint (§8 performance-bible) OR could mean texture/skin/motion naturalism (ai-video-failure-bible) — these produce completely different fixes, so don't average them into a vague "add more detail" pass.

## 5. Revision Diff
When presenting a revised version, state what actually changed, plainly:
```
V1 → V2: performance intensity reduced (per "kurang emosional" feedback — now restrained per performance-bible.md rather than bigger); camera unchanged; wardrobe unchanged.
```
This does two things: confirms the right thing was changed (not everything, not the wrong thing), and makes it easy for the human reviewer to spot a **regression** — something that got worse as a side effect of fixing the requested thing (see `evals/drift-detection.md` §Creative Regression Check).

## 6. Self-check
- Is this decision actually this skill's to make, or does it belong at a human gate (§1)?
- Has vague feedback been translated into a specific, restated domain before acting on it?
- If a revision was made, is there a diff stating exactly what changed and what didn't?
