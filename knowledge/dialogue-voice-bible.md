# Dialogue & Voice Bible

Domain: everything specific to characters who speak — shot strategy for dialogue, lip-sync method choice, voice direction, and interaction choreography for multiple speaking characters. Builds on `performance-bible.md` (silent acting) and `storytelling-bible.md` §10 (dialogue writing craft) — this file is the execution layer once dialogue exists.

## 1. Lip-Sync Strategy — Choose Deliberately, Don't Default
| Approach | When to use |
|---|---|
| Native speech generation (model generates mouth+voice together) | short lines, when the target model's lip-sync quality is proven reliable for this project (check `model-capabilities.md`) |
| Separate voice track + lip-sync pass | longer dialogue, when native generation quality is unreliable, when voice casting (§3) needs independent iteration from visual |
| Avoid visible dialogue entirely (off-screen voice, reaction-only coverage, text/caption instead) | when lip-sync reliability is poor for the target model/duration, or when the shot's real job is the reaction not the line itself |

Default to whichever option has an established track record in THIS project (`generation-strategy.md` §5) — don't re-litigate this choice per shot.

## 2. Dialogue Shot Strategy
Standard coverage vocabulary for a dialogue scene: close-up, profile, over-the-shoulder (clean or dirty, see `blocking-bible.md`), two-shot, off-screen dialogue (hearing a voice while seeing a reaction), reaction coverage. Choosing among these is a `camera-bible.md` decision informed by whose emotional state matters most in this beat — the closer/tighter shot goes to whoever's internal reaction the audience needs to read.

## 3. Voice Direction
Define per character (part of the canonical asset, `workflows/casting.md` §14):
- tempo (fast/measured/halting)
- resonance (chest/head voice, deep/light)
- breathiness
- articulation (crisp/loose)
- emotional intensity range
- accent — and its CONSISTENCY requirement across every line/session (accent drift is a continuity failure, same tier as visual identity drift)

## 4. Natural Dialogue Performance
Real speech is not clean back-and-forth. Direct for:
- **interruption** — one character starts before the other finishes
- **hesitation** — incomplete or restarted sentences
- **overlap** — brief simultaneous speech
- **subtext** — what's said vs. what's meant (see `storytelling-bible.md` §10) — direct the ACTING toward the meant thing, not the said thing
- **silence** — a pause is a valid beat, not a gap to fill
- **reaction before reply** — a listening character responds physically before speaking, not simultaneously with the other character finishing

Avoid generic "clean" back-and-forth delivery by default — it reads as scripted/AI-generated (see `ai-video-failure-bible.md` overacting pattern, which extends to dialogue delivery too).

## 5. Multi-Character Interaction Framework
For any scene with 2+ speaking characters, define explicitly:
- who is looking at whom, and when it shifts
- who is speaking, and the listening character's behavior while not speaking (not blank — some micro-reaction, per `performance-bible.md` §9 eye behavior)
- proximity (ties to `blocking-bible.md` interpersonal distance)
- any physical hand-off/touch — apply `performance-bible.md` §6 contact constraints
- reaction timing — does the reaction land immediately or with a believable delay (ties to `performance_dna.reaction_latency`, `workflows/casting.md` §15)

## 6. Crowd / Background Character State
Background characters/extras should not visually reset between shots (different random people, different positions) unless the scene genuinely calls for a crowd change. Where a project reuses background figures across shots in the same space, track them as lightweight canonical assets too (even a rough position/action note is enough — full casting treatment is usually overkill for background figures, see `workflows/casting.md` §10).

## 7. Self-check
- Has a lip-sync approach been chosen deliberately per §1, not defaulted?
- Does the dialogue read as natural (interruption/hesitation/subtext) rather than clean scripted exchange, unless clean delivery is the deliberate choice for this character/scene?
- For multi-character scenes, is listening-character behavior directed, not left blank?
