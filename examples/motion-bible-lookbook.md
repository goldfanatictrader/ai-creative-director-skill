# Example — Motion Budget Video Lookbook

## Purpose

The first **video** example in this skill's lookbook series (all prior lookbooks tested still-image domains). Worked example of SKILL.md's §"Movement budget" rule — *"Default rule: 1 primary subject action, 0–1 secondary subject action, 0–1 facial action, 0–1 primary camera movement, 0–2 environmental motions... If complexity is too high, split the shot"* — and `knowledge/motion-bible.md`'s §Motion layers/§Motion budget, which names the same constraint from the craft side: reduce simultaneous motion layers when faces must stay consistent or the camera path is complex.

Two 10-second text-to-video clips, same general subject and setting family, one respecting the budget and one deliberately violating it by stacking every layer at once:

1. **Low complexity** — one subject action, static camera, no secondary/environmental motion.
2. **High complexity** — primary + secondary + facial action, complex camera movement (orbit + push-in), and multiple environmental motion layers (crowd, wind, blowing leaves), all simultaneously.

Per `knowledge/video-qa-bible.md`'s observed/measured/inferred split: the finding below is **observed** (perceived directly in video playback by the reviewer), not measured by deterministic tooling — a real limitation of this test method, noted honestly in the QA section.

---

## 1. Low complexity (within budget)

**Prompt:** "A woman walks in a straight line across a plain sunlit courtyard, natural steady walking gait, weight transferring naturally between feet, arms swinging gently. Camera is completely static, locked off. No other movement in the environment. Simple, clean, restrained shot."

<video src="assets/motion-bible-lookbook/01-low-complexity.mp4" controls width="480"></video>

Motion layers present: 1 primary subject action (walking). Camera: static (0 movement layers). Secondary/environmental: none.

**QA:** clean, consistent walking gait for the full 10s, static locked-off camera exactly as specified, no visible foot sliding, limb warping, or body-proportion drift across the clip. **Pass.**

## 2. High complexity (deliberately over budget)

**Prompt:** "A woman walks quickly while rapidly turning her head to look behind her, waving one hand energetically at someone off-camera, her hair whipping in strong wind, while the camera simultaneously orbits around her and pushes in fast, with a crowd of people also moving rapidly in the background and leaves blowing everywhere in all directions."

<video src="assets/motion-bible-lookbook/02-high-complexity.mp4" controls width="480"></video>

Motion layers present, all at once: primary subject action (walking) + secondary subject action (hand wave) + facial/head action (turning to look back) + complex camera movement (simultaneous orbit + push-in) + multiple environmental layers (crowd, wind, blowing leaves) — five to six layers stacked simultaneously, directly against the "reduce simultaneous motion layers" rule.

**QA (observed during playback, not caught by the 1fps still-frame extraction used for this write-up):** the subject's head rotation reads as unnaturally fast/exaggerated at points in the clip — the kind of joint/rotation-speed implausibility `SKILL.md`'s Physical Realism section names ("plausible joint limits," "no abrupt unmotivated acceleration"). This is exactly the class of failure the movement-budget rule exists to prevent, and it appeared specifically in the shot that stacked every motion layer at once — not in #1.

---

## Takeaway

The two clips isolate the same variable the bible names: number of simultaneous motion layers. The low-complexity clip (1 layer) stayed clean for its full duration; the high-complexity clip (5-6 layers stacked) produced a visible physical-plausibility artifact in exactly the area — head/neck rotation — under the most simultaneous demand (subject turning while camera also rotates around her). This is a working demonstration, not a formal statistical claim (n=1 per condition) - but it's consistent with the bible's own stated reasoning for the budget, and is a concrete example of why `evals/output-critique-repair.md`'s failure-repair logic recommends *reducing camera complexity* and *reducing simultaneous limb/torso actions* rather than treating every generation as equally reliable regardless of how much is asked of it in one shot.

## Method note

Native whole-video review (per `knowledge/video-qa-bible.md`) is preferred over frame sampling for exactly this reason: a fast rotational glitch can fall between sampled frames. This lookbook's write-up combines a human's real-time video observation with 1fps frame extraction as supporting context - the two are kept separate per the observed/measured/inferred distinction, not blended into one claim.
