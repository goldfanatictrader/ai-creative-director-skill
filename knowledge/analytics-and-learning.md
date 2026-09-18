# Analytics & Learning

Domain: using real-world performance data and project experience to inform future creative decisions — with an explicit boundary on what this skill can and can't do here. Covers Creative Analytics, Performance Feedback Loop, A/B Test Design, Experiment Logging, and Learned Project Preferences.

## 1. Honest Boundary
This skill cannot itself read platform analytics (retention, CTR, completion rate, comments) — that requires actual API/tool access to a specific platform, which is project-specific integration, not creative-direction knowledge (same boundary as the execution stack, see `SKILL.md`). What this file defines is what to DO with that data once a human or a connected tool supplies it, and how to design experiments properly so the data is actually usable.

## 2. A/B Test Design — Isolate the Variable
A test comparing "two videos" is usually not a usable test — comparing two videos that differ in five ways at once can't attribute a performance difference to any one of them. Design tests around ONE clear variable at a time:
```
variable: hook (first 3 seconds) — everything else identical
variant A: character close-up open
variant B: object/product open
```
Common isolatable variables: hook/first-frame, length, voiceover presence/absence, pacing, CTA placement/wording. Log which variable was actually isolated — a test that accidentally changed two things invalidates the read even if the data looks clean.

## 3. Experiment Logging
Record what was tested and the result, in the same `project-state/` convention as everything else (`project-state-system.md` §1) — not just in a stakeholder's head:
```
test: hook variant (character-open vs. product-open)
result: character-open retained +18% at 3s
applied: default to character-open for this campaign's future cuts
```

## 4. Performance Feedback Loop — Without Breaking Brand Consistency
When real audience data suggests a change (e.g. faster pacing performs better), apply it carefully against `creative-direction.md` visual grammar and any locked brand rules (`governance-and-locks.md` §2) — data justifies iteration within the established creative system, it doesn't unilaterally override a locked brand decision. Surface the tension to a human if data and brand lock genuinely conflict, same as any other conflict (`project-state-system.md` §6).

## 5. Learned Project Preferences — Per Project, Not Universal
If a specific project consistently prefers certain choices (a particular pacing, a particular restraint level, a particular camera grammar), note it as a project-specific preference (`project-state-system.md`), not a universal rule this skill applies to every future unrelated project. A preference learned on one branded-content project should not silently leak into a narrative short for a different client.

## 6. Self-check
- Is an A/B comparison actually isolating one variable, or comparing two videos that differ in several ways?
- Is a data-driven change being checked against locked brand/creative rules before being applied?
- Is a learned preference being scoped to the project it came from, not generalized silently?
