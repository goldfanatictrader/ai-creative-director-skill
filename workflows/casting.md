# Workflow — Casting

Domain: deciding WHO plays a character before locking identity, not just describing what they look like. Run this whenever a project introduces a new significant character (not needed for pure product/beauty/corporate work with no character, or for a background/incidental figure).

## 1. Pipeline
```
ROLE ANALYSIS → CASTING BRIEF → CASTING OPTIONS → SCREEN TEST → CHEMISTRY TEST
→ CAST SELECTION → CHARACTER LOCK → WARDROBE/HAIR/MAKEUP → PERFORMANCE TEST
→ CANONICAL CHARACTER ASSETS → PRODUCTION
```

## 2. Role Analysis
Before any face is chosen, define the role's STORY FUNCTION: protagonist, antagonist, mentor, love interest, witness, background/incidental. Function shapes casting more than physical preference does — a mentor role and a love-interest role want different screen presence even if age/gender match.

## 3. Casting Brief (not a physical-description shortcut)
Don't write "man, 35, handsome." Write a casting brief covering:
- narrative function
- apparent age
- physical presence (petite / athletic / broad / fragile-looking / imposing / ordinary / elegant / awkward)
- face character (angular / soft / weathered / youthful / distinctive / approachable)
- silhouette, posture, movement language
- screen presence
- voice character, speaking rhythm (if dialogue exists — see `dialogue-voice-bible.md`)
- performance range needed
- baseline emotional energy
- wardrobe compatibility with the world
- required chemistry with co-cast (if any)

Example (from a real brief): *"A man in his mid-30s, face not too polished, eyes tired but calm, lean rather than muscular build, posture slightly closed off, economical movement, low voice without excessive weight. He should look like someone who has been holding something back for a long time, not like a fashion model."* That is a casting brief; "handsome 35-year-old man" is not.

## 4. Casting Options — Generate Distinct Candidates, Not Variations
Produce 2-4 genuinely different candidates for the role, not near-duplicates. For each, note the tradeoff against the brief:
```
ROLE: <name>
Candidate A — more conventionally attractive, strong screen presence, reads too heroic for this role
Candidate B — more ordinary face, stronger subtle expression, more believable as someone worn down
Candidate C — most visually distinctive, but reads too intimidating for the intended warmth
```
Select based on story function match, not which candidate is individually most striking.

## 5. Screen Test — A Still Portrait Is Not Enough
A face that works beautifully as a single still image can lose identity when animated, turned, or emotionally activated. Before finalizing a candidate, generate a screen-test set:
1. neutral portrait
2. front / three-quarter / profile
3. neutral full body
4. speaking close-up (if dialogue)
5. subtle sadness
6. restrained anger
7. walking
8. interaction with a prop
9. bright/high-key lighting
10. low-key/dim lighting

Evaluate identity stability across all ten, not just #1. A candidate that drifts badly on profile angle or under low-key lighting is a casting risk even if the neutral portrait was the strongest of the options.

## 6. Chemistry Test (two or more lead characters)
Individually strong candidates don't guarantee visual chemistry together. Test the combination:
- standing side by side
- eye contact
- conversation over-the-shoulder
- two-shot
- walking together
- physical distance variations (close/mid/far — ties to `blocking-bible.md` interpersonal distance)

If two individually approved candidates don't read well together, that's grounds to recast one of them — don't force a pairing that fails chemistry test just because both passed individually.

## 7. Character Lock
Once selected, the identity is LOCKED. **Do not redesign the face just because a later shot needs a different angle** — that's what the screen test in §5 was for. Any deviation from a locked identity is a continuity failure, not a creative refinement (see `continuity-bible.md` Reference Authority Hierarchy — the locked canonical reference outranks any later generative interpretation).

## 8. Canonical Character Package
After lock, produce the durable reference set (naming convention, ties to `knowledge/project-state-system.md` asset IDs):
```
CHAR_01/
  identity-master.<ext>
  front.<ext>  left-3q.<ext>  right-3q.<ext>  profile-left.<ext>  profile-right.<ext>
  full-body.<ext>
  expressions/          (from the screen-test set, §5)
  wardrobe/
  hair/
  makeup/
  performance-profile   (baseline posture, gesture range, expression range, movement style, forbidden mannerisms — see character.schema.json)
  voice-profile         (if dialogue — see dialogue-voice-bible.md)
  CHARACTER_BIBLE.md    (role, casting brief, locked traits, what must never change)
```

## 9. Three Distinct Questions — Don't Collapse Them
- **Character Designer** asks: what does this character look like?
- **Casting Director** asks: who should play this character?
- **Performance Director** asks: how does this character live and react?
This skill's Creative Director hat is responsible for all three, in that order — don't jump straight to "generate a woman, 25" (designer-only thinking) when the role actually needs a casting decision first.

## 10. When to Skip This Workflow
Skip for: products, pure voiceover/no-visible-character content, background/incidental figures with no recurring appearance, or any project where `knowledge/video-taxonomy.md` routing indicates no meaningful character (e.g. most Product, Technology/SaaS, Real Estate families). Run it for any character that recurs across multiple shots/scenes or carries narrative weight.

---

## 11. Casting Beyond Live Action
Everything above applies to animation, anime, stylized 3D, stop-motion, and non-human characters too — the underlying question is universal: **what design, voice, and movement best plays this story function, and can it hold its identity through an entire production?** Live action asks "who is the actor"; every other format asks "what is the design + voice + movement, and does the whole package survive being animated." Same discipline, different casting pool.

| Production type | What is actually being cast |
|---|---|
| Live action | actor: face, body, voice, chemistry |
| 2D cartoon | character design, silhouette, proportions, expression system, voice |
| Anime | design archetype, face language, hairstyle, costume, acting style, voice |
| 3D animated | model design, proportions, rig behavior, facial range, movement personality, voice |
| Stop-motion | puppet design, material, articulation, animator performance, voice |
| Animal / creature film | species/design, physical behavior, anthropomorphism level, voice if speaking |
| Robot / mecha | body design, motion mechanics, personality expression, voice/sound identity |
| Children's series | readability, friendly silhouette, expressive range, memorable shape/color, voice |
| Long-running series | all of the above, plus the design's ability to survive dozens/hundreds of episodes |

Design candidates get the same §4 treatment (distinct options, not variations), e.g.:
```
Candidate A — round proportions, large expressive eyes, soft silhouette, reads innocent
Candidate B — angular silhouette, longer limbs, more kinetic, reads mischievous
Candidate C — compact body, oversized costume element, strong visual identity, reads comedic
```

## 12. Animation Screen Test
Replaces §5 for non-photoreal characters. A design that looks great as concept art may fail once animated — a face too intricate for a clean profile read, eyes too small for expression to register, wardrobe too detailed to stay consistent across generations, or a silhouette too close to another cast member's. Test across:
- expression: neutral / happy / sad / angry / afraid / confused
- angle: front / three-quarter / profile / back
- action: standing / walking / running / sitting / jumping
- vocal state: speaking / shouting / whispering / silent reaction

## 13. Generation Survivability Test (AI-specific — no live-action equivalent)
The AI-pipeline-specific risk beyond a normal animation screen test: does the design hold identity across the transformations the production will actually put it through?
```
front → profile
close-up → full body
day → night
happy → angry
static → running
single character → group shot
```
A design that is striking but drifts every time it's animated is not a good cast for an AI generation pipeline, regardless of how good it looks as a single still — this is a casting disqualifier, not a later fix.

## 14. Voice Casting Is Its Own Casting Pass
Voice is not a downstream detail — the same design reads completely differently depending on delivery (high-energy / soft-timid / dry-sarcastic / deep-calm / raspy-chaotic). Run voice as its own candidate/selection pass, then confirm the pairing: does this voice match this visual design, the same way §6 checks chemistry between two visual casts? A `CHARACTER_BIBLE.md` (§8) needs a **VISUAL CAST** section and a **VOICE CAST** section, and the two must be validated together, not assumed compatible.

## 15. Movement Casting & Performance DNA
For a full animated cast (Pixar/Disney/DreamWorks-style or any project with several recurring characters), movement itself is part of what's being cast — two characters can be visually distinct and still move identically, which wastes the distinction. Define a `performance_dna` per character so they're recognizable from silhouette/movement alone, without seeing the face:
```yaml
performance_dna:
  posture: slightly_forward
  locomotion: quick_light_steps
  gesture_amplitude: medium_high
  reaction_latency: low
  facial_intensity: high
  head_motion: frequent_small
  hand_behavior: expressive
```
This extends `schemas/character.schema.json` → `performance_profile` and feeds directly into `performance-bible.md` choreography for every shot involving this character — the acting choreography order (initial pose, primary action, etc.) gets filled in per-character using this DNA as the baseline, not reinvented shot to shot.

## 16. Ensemble Casting & Differentiation
For a cast of several characters (typical in series/ensemble work), cast them AGAINST each other, not independently. Two tests:
- **Silhouette differentiation**: could each character be told apart in silhouette alone, with no face/color visible? (e.g. short-and-round vs. tall-and-narrow vs. large-and-heavy vs. small-with-extreme-hair)
- **Ensemble palette**: design the cast's color relationships as a set — not each character given an independently "favorite" color — so that when several appear in one frame, each remains individually readable (ties to `color-bible.md` §Color Script, applied to characters instead of scenes)

## 17. Cast Role Types (series/ensemble work)
Not every character needs the same visual "weight." Distinguish role types explicitly when casting an ensemble: lead, second lead, supporting, comic relief, mentor, rival, antagonist, recurring, guest, background archetype. A common failure is giving every character equally strong visual personality, which flattens the hierarchy the story actually needs.

## 18. Character Design as Story — Visual Arc
Design is not static for characters with a real arc across the production — it should carry the story the same way `color-bible.md` §Color Script carries it for the whole film. Example:
```
Act 1: closed posture, clean costume, controlled hair
Act 2: more open movement, damaged costume, increasing visual disorder
Act 3: upright posture, simplified costume, more confident movement
```
Plan this explicitly at casting/lock time (as a small number of defined states, not continuous drift) rather than letting costume/posture wander shot to shot.

## 19. Creature & Non-Human Casting
For creatures, animals, or non-human characters, establish the physical rule set BEFORE thinking about acting:
```
biological rules: skeleton, number of limbs, joint limits, center of gravity
locomotion, breathing, eyes, mouth, communication style, social behavior
```
A dragon should not move like a human in a dragon costume — unless that's a deliberate stylistic choice for the project, in which case say so explicitly as a locked decision, not a default drift.

For robots/mecha, the equivalent rule set is mechanical, not biological:
```
servo speed, joint constraints, mechanical inertia, head articulation, eye/light-based expression, sound cues
```
These constraints ARE the character's performance vocabulary — treat them with the same rigor as `performance-bible.md`'s human biomechanics constraints, adapted to the actual body plan.

## 20. Series Longevity Test
For long-running series specifically, add one more check beyond a single production: can this design/voice/movement package stay recognizable and reproducible across dozens or hundreds of episodes, likely across changing tools/models/seasons? A design that only barely holds together for one generation pass is a longevity risk for a series in a way it isn't for a single film/short.

## 21. Full Casting System Summary
```
Human Casting · Character Design Casting · Voice Casting · Movement Casting
· Creature Casting · Ensemble Casting · Chemistry Casting
· Generation Survivability Test · Performance Test · Series Longevity Test
```
All feed the same lock sequence regardless of production type:
```
CAST LOCK → CHARACTER BIBLE → MODEL SHEET → EXPRESSION SHEET → POSE SHEET
→ MOVEMENT DNA → VOICE DNA → WARDROBE/VARIANTS → CANONICAL ASSETS
```
The underlying question never changes across live action, anime, 3D animation, stop-motion, children's series, or creature/robot work: **what design best plays this story function, and can it hold its identity and performance across the whole production?**
