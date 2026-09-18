# Reference Analysis Engine

Domain: how to actually READ a reference image, video, storyboard, film still, or moodboard — not label it "cinematic" and move on. Used whenever a user attaches a reference, at BRIEF/VISUAL LANGUAGE steps, and whenever `continuity-bible.md`'s Reference Authority Hierarchy needs a reference actually interpreted.

## 1. Rule
A reference is not "vibes" — it decomposes into the same parameters this skill already uses elsewhere. Extract each dimension explicitly, then translate into this project's vocabulary (don't just say "make it like the reference").

## 2. Extraction Checklist
For any single reference frame/image:
- **Lens language**: apparent focal length (wide distortion vs compressed telephoto?), depth of field, perspective
- **Composition**: rule-of-thirds vs center, headroom, negative space, foreground layering (see `cinematography-bible.md`/`composition-bible.md`)
- **Lighting**: source count/type guess, hard vs soft, direction, key:fill ratio impression, color temperature, practicals visible
- **Color**: palette (2-4 dominant hues), saturation level, contrast, skin treatment, warm/cool bias
- **Production design**: era, material palette, density of set dressing, wear/aging level
- **Acting/performance** (if people present): intensity level (restrained vs heightened), pose naturalism, gaze behavior
- **Camera position**: angle, height, distance — same vocabulary as `camera-bible.md` §2-4

For video references, add:
- **Movement**: type, speed, stabilization character (see `camera-bible.md` §8-10)
- **Pacing**: average shot length if multi-shot, cut rhythm
- **Motion character**: organic vs mechanical (see `motion-bible.md` §9)

## 3. Output Format
Don't hand back a paragraph of adjectives. Produce a short structured read:
```
reference: <file/description>
lens: ~35mm equivalent, shallow-moderate DOF
lighting: single soft key from camera-left, motivated window, low fill (contrast-heavy)
color: desaturated teal shadow / warm skin highlight, low overall saturation
composition: subject left-third, negative space right, slight low angle
camera: eye-level, three-quarter ~30° right, static
performance: restrained, minimal gesture
applicable to this project: lighting ratio + color bias — yes. Camera height — no (our subject needs eye-level, not low-angle hero treatment)
```
The last line matters: state explicitly what transfers to the current project and what doesn't — a reference is rarely 100% adoptable wholesale.

## 4. Multiple References
When several references are given, don't average them into mush. Assign each one a specific job:
```
REF_01 (film still): lighting ratio + color palette authority
REF_02 (character photo): face/wardrobe identity authority (see continuity-bible.md Reference Authority Hierarchy)
REF_03 (moodboard): production-design texture reference only, NOT composition
```
Conflicting references need an explicit authority decision, not silent blending.

## 5. Style vs Identity — Never Confuse
A style/mood reference (grading, composition, lighting) must never override an identity reference (a specific character's face, a specific product's shape, a specific location's layout). If a style reference and identity reference conflict, identity wins — see `continuity-bible.md` §Reference Authority.

## 6. Common Extraction Failure
The most common mistake is naming a reference's *genre* ("this looks like a Denis Villeneuve film") instead of naming its *parameters* (35mm, desaturated teal-orange, hard side light, symmetrical wide compositions). Genre-naming doesn't translate into an executable spec; parameter-naming does. Always push past the genre label to the parameters underneath it.

## 7. Self-check
- Have I named parameters (lens/light/color/composition/camera/performance), not just a mood word or director name?
- If multiple references, does each have an assigned job/authority?
- Have I stated what does and doesn't transfer to this project?
