# Example — Performance Bible A/B Lookbook

## Purpose

Worked example of `knowledge/performance-bible.md`'s central rule — **"Direct behavior, not adjectives"** — and its §Restrained default vs §Forbidden default behaviors contrast. Two paired A/B tests, same subject:

1. An abstract emotion label ("acting nervous") vs. the bible's own §Example translation of "nervous" into observable behavior (gaze shifts once toward exit, shallow breath, lips tighten slightly, hands remain still, shoulders do not rise).
2. The §Forbidden default behaviors this skill warns generative video "often overacts" into, vs. the §Restrained default (minimal brow movement, controlled mouth, stable shoulders, small eye behavior, single clear gesture).

---

## 1. Abstract adjective only ("acting nervous")

**Prompt:** "A woman standing in a doorway, acting nervous, nervous expression, looking nervous, anxious body language."

![Adjective only](assets/performance-bible-lookbook/01-adjective-only.jpg)

QA: reads as a generic "scared movie face" — furrowed brow, clenched hands drawn up toward the chest, a somewhat theatrical fear expression. Legible, but generic rather than specific, and already trending toward the exaggerated end the bible warns about.

## 2. Behavior translation (bible's own example)

**Prompt:** "The same woman standing still in a doorway. Her gaze shifts once toward the exit behind her, a shallow breath visible in her chest, her lips tighten slightly, her hands remain still at her sides, her shoulders do not rise. Restrained, controlled physical performance, no exaggerated expression, subtle observable behavior only."

![Behavior translation](assets/performance-bible-lookbook/02-behavior-translation.jpg)

QA: hands stay down and still (not clenched/raised), gaze reads as directed off toward something behind/beside her rather than at camera, expression is subtle lip tension rather than a full fear-face — noticeably more restrained and specific than #1 despite depicting the same emotion. This is the concrete difference "direct behavior, not adjectives" produces.

## 3. Forbidden default (over-the-top / overacting)

**Prompt:** "The same woman having an emotional dramatic moment, exaggerated wide-eyed expression, wide dramatic gesture with both hands raised, head tilted dramatically, big dramatic exaggerated smile, torso twisting dramatically. Over-the-top theatrical acting."

![Forbidden overacting](assets/performance-bible-lookbook/03-forbidden-overacting.jpg)

QA: both hands thrown up, exaggerated wide-eyed grin, torso twisted and leaning in — a deliberate embodiment of the exact behaviors §Forbidden default behaviors lists (unnecessary gestures, random smile, torso twisting without motivation). Included as the negative reference.

## 4. Restrained default

**Prompt:** "The same woman having a quiet emotional moment. Minimal brow movement, controlled subtle mouth movement, stable still shoulders, small subtle eye movement, one single clear hand gesture touching her own collarbone. Restrained, believable, understated performance, no exaggerated expression."

![Restrained default](assets/performance-bible-lookbook/04-restrained-default.jpg)

QA: one clear, motivated hand gesture (touching her own throat/collarbone), shoulders relaxed and stable, quiet downward gaze, minimal facial change — the polar opposite of #3 on every axis the bible names, and a believable, film-like quiet-emotional beat. **Pass.**

---

## Takeaway

Pairing #1/#2 shows that even holding the *emotion* constant ("nervous"), translating it into specific observable behavior per §Performance components produces a visibly more restrained, specific, and believable result than naming the emotion and hoping the model infers appropriate behavior. Pairing #3/#4 shows the bible's restrained-vs-overacting distinction isn't cosmetic — the two read as fundamentally different performance registers from prompt language alone, confirming that the default failure mode ("generative video often overacts") is something the prompt actively steers away from or into, not something left to chance.
