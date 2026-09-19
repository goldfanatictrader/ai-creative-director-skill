# Example — Comedy Hold-Beat Timing Lookbook

## Purpose

Worked example of `knowledge/genre-grammars.md` §Comedy Timing Grammar: *"Setup → hold → reaction → punchline is the standard structural unit. The HOLD (a beat of stillness before the punchline lands) is the part most often rushed or omitted by default AI pacing — protect it explicitly, don't let editorial rhythm auto-compress it away."*

A minimal, silent visual gag (a man discovers his coffee cup is empty mid-sip) was rendered twice as a 10-second text-to-video clip: once with no pacing direction at all (just the sequence of events), and once with the hold beat explicitly written into the prompt. Same premise, same event order — the only variable is whether the hold was asked for.

---

## 1. No explicit hold (default pacing)

**Prompt:** "A man sitting at a kitchen table reaches for his coffee mug, picks it up, brings it to his mouth to drink, realizes it's empty, and looks confused. Camera static."

<video src="assets/genre-timing-lookbook/01-no-hold.mp4" controls width="480"></video>

**Observed pacing:** by the time the cup reaches his lips, his expression is already shifting toward confusion — the "realizes it's empty" reaction reads as starting *while* the drinking motion is still happening, not as a separate beat after it. Setup and reaction blend into one continuous motion rather than reading as distinct story beats.

## 2. Explicit hold beat

**Prompt:** "A man sitting at a kitchen table reaches for his coffee mug and picks it up. He brings it toward his mouth to drink, then pauses and holds perfectly still for a beat with the cup near his lips, sensing something is off, before glancing down into the empty cup. A brief still beat of silence follows. Then his face shows surprised disappointment. Camera static."

<video src="assets/genre-timing-lookbook/02-with-hold.mp4" controls width="480"></video>

**Observed pacing:** four distinct, separable beats are visible in sequence — (1) a neutral sip with eyes closed, (2) a held pause with the cup still near his lips and eyes now open, brow tensing (the protected HOLD), (3) a separate look-down-into-the-cup reveal beat, (4) the cup lowered and a distinct disappointed-reaction beat. Setup, hold, reveal, and reaction read as four beats, not one blended motion.

---

## QA

Both clips are a single continuous take (this bot's generation mode doesn't support multi-shot editorial cutting within one job), so this tests whether the model's *within-shot* pacing honors an explicitly requested hold — not editorial rhythm across a cut. Per the bible's own framing, the concern named is specifically that a default AI generation "rushes or omits" the hold; that is what's visible in clip 1, and clip 2 shows the same premise with the hold surviving when it's written in explicitly rather than assumed.

Both are **observed** findings (per `knowledge/video-qa-bible.md`'s taxonomy) from reviewing the actual video playback and 2fps frame sampling — not a measured/deterministic timing metric, and comedic timing is inherently a subjective judgment call even for a human editor. Note also that the two clips used different generated actors/kitchens (no reference image was used to hold identity constant across the two separate generations) since the variable under test was pacing, not identity continuity — see [`continuity-bridge-lookbook.md`](continuity-bridge-lookbook.md) for identity-anchored continuity testing.

---

## Takeaway

The bible's specific warning — that AI pacing defaults toward compressing the hold — held up in clip 1's blended setup/reaction, and explicitly writing the hold, the sensing-something's-off beat, and the separate reveal into the prompt (rather than just listing the plot events) produced four legible beats instead of one rushed motion in clip 2. This is a concrete illustration of why `SKILL.md`'s prompt-compilation stage treats timing/pauses as something to specify deliberately (`SKILL.md` §Performance components: "pauses," "reaction delay") rather than something the model will infer correctly from a bare sequence of events.
