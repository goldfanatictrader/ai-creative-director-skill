# Generation Strategy

Domain: choosing HOW a shot gets made — which generation method, which model, and what to do when it fails — as a deliberate decision, not a default reflex to whatever tool was used last. Sits between FEASIBILITY and GENERATION SPEC in the SKILL.md chain.

## 1. Generation Method Selection
Not every shot should be text-to-video by default. Choose per shot:
| Method | Best for | Weak for |
|---|---|---|
| Text-to-video (T2V) | shots with no identity-lock requirement, establishing/environment shots, quick exploration | anything needing consistent character/prop identity across shots |
| Image-to-video (I2V) | identity-locked shots from an approved keyframe | shots where the keyframe itself is wrong — garbage in, garbage out |
| Reference-to-video (multi-image) | shots needing character + location + prop consistency simultaneously | providers with weak multi-reference support; can dilute identity fidelity vs single strong reference |
| First/last-frame interpolation | controlled transitions between two specific approved states | organic mid-shot performance nuance — tends to interpolate mechanically |
| Motion transfer | performance-critical shots where a real reference performance exists | no reference performance available |
| Video edit / extend | continuing an existing approved clip seamlessly | starting fresh shots — extend inherits any drift already in the source |
| Compositing (generate elements separately, combine in post) | shots exceeding single-generation complexity budget (see `evals/shot-feasibility.md`) | anything where seams would be visible under scrutiny |
| Traditional footage / stock | when no generative method can plausibly deliver it, or cost/time doesn't justify trying | project style consistency if mixed with generated material — flag this explicitly |

## 2. Model Routing
Don't force one model to carry an entire project. Route per shot requirement:
- Identity-critical shots → whichever available model/provider has demonstrated the strongest reference-image fidelity for this project so far (track this — see §5).
- Physically complex motion (running, multi-character contact) → prefer the model with better track record on locomotion/contact, even if it's not the "default" one.
- Cheap/fast iteration (exploring an idea before committing) → cheapest/fastest available, don't burn premium generations on unresolved concepts.
- When uncertain, and stakes are low: try the default first; when stakes are high (hero shot, expensive to reshoot): consider a small test generation on the cheaper/faster model first to de-risk the approach before spending on the primary one.

## 3. Fallback Strategy — Don't Retry Blindly
If a shot fails 3-5 generation attempts with the same approach, STOP retrying the identical prompt. Change one of:
- **Framing** — pull back from extreme macro, change angle (see `ai-video-failure-bible.md` for the specific patterns this fixes)
- **Staging** — simplify what's happening in the shot (see `evals/shot-feasibility.md` complexity budget)
- **Duration** — shorter clips have less room to drift
- **Camera** — reduce movement complexity, or switch to locked
- **Generation method** — switch from T2V to I2V with a stronger keyframe, or vice versa
- **Provider/model** — if the current provider/model is having an infra-level bad day, diagnose per `ai-video-failure-bible.md` §3 before assuming the creative approach is at fault

Repeating the exact same failing prompt more than once or twice is a strategy failure, not persistence.

## 4. Automatic Failure Diagnosis
After a failed or rejected generation, don't just say "regenerate" — say WHY it failed, using the categories in `ai-video-failure-bible.md` (face drift / hand failure / foot sliding / body morphing / camera warp / impossible geometry / camera angle ambiguity / text-decal drift / wrong object identity / aspect ratio ignored / infra issue). Naming the specific failure mode is what makes §3's fallback choice non-arbitrary — "framing fix" only makes sense as a response to "impossible geometry from extreme macro," not to "foot sliding."

## 5. Track What's Working (lightweight, per-project)
Keep a running note (in the project's own state file — see continuity conventions) of which generation method/model has worked for which shot type in THIS project so far. This doesn't need to be elaborate — a short running list is enough:
```
identity-lock shots: NexaBot ingredient (image edit then i2v) — reliable this project
text-only fallback: SimpleNGAT t2v — usable but requires very precise physical description, verify against reference once identity pipeline is available again
macro mechanical detail: keep to single-contact-point framing regardless of provider
```
This prevents relearning the same lesson shot after shot within one project, without requiring a formal cross-project analytics system.

## 6. Self-check before generating
- Has a deliberate method been chosen per §1, not just defaulted to whatever was used last?
- If this is a retry, has something concrete changed per §3 (not the same prompt again)?
- If a previous shot in this project already found a working approach for a similar shot type, is that approach being reused (§5)?
