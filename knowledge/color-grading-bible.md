# Color Grading Bible

## 1. Role of color grading

Color grading has five separate jobs:

1. **Technical normalization** — interpret the source correctly.
2. **Shot consistency** — make adjacent shots belong to the same scene.
3. **Visual hierarchy** — guide viewer attention.
4. **Creative look** — express story, world, genre, and brand.
5. **Mastering** — map the creative intent correctly to the target display.

Do not collapse these into one operation.

---

# 2. Color pipeline model

Use this conceptual chain:

SOURCE
→ INPUT TRANSFORM
→ SCENE-REFERRED WORKING SPACE
→ BALANCE
→ SHOT MATCH
→ CREATIVE GRADE
→ LOCAL / SECONDARY CORRECTIONS
→ LOOK
→ OUTPUT RENDERING / DISPLAY TRANSFORM
→ DELIVERY
→ QC

A LUT may exist inside the pipeline, but it is never the entire pipeline.

---

# 3. Source identification

Before grading, determine:

- camera / generator
- transfer function
- gamut
- bit depth
- RAW / Log / display-referred source
- white balance metadata
- exposure metadata
- expected mastering target
- whether a display transform is already baked in
- whether AI-generated imagery is already display-referred

Never blindly assign a Log transform to footage merely because it looks flat.

---

# 4. Scene-referred vs display-referred

## Scene-referred

Values represent scene-light relationships before final display rendering.

Useful for:
- camera matching
- wide-gamut grading
- HDR / SDR derivation
- VFX
- large exposure moves
- archival / remastering

## Display-referred

Values are already shaped for a target display.

Useful when:
- source is finished Rec.709 / sRGB
- working with graphics designed for a display
- final mastering adjustments are required

Do not treat display-referred material as if it still contains unrestricted scene latitude.

---

# 5. Working-space strategies

The system may use:

- ACES 2
- DaVinci Wide Gamut / Intermediate
- another properly configured wide-gamut scene-referred workflow
- a deliberate display-referred workflow for simpler projects

The choice must be explicit.

## ACES 2

Use when:
- multiple camera sources exist
- VFX interchange matters
- long-lived archival consistency matters
- multiple output targets are expected
- transform provenance should be explicit

ACES 2 uses redesigned rendering/output transforms intended to provide more consistent output behavior, gentler highlight rolloff, and improved gamut mapping than ACES 1.

## DaVinci Resolve Color Management

Useful when the production is centered in Resolve and requires:
- input assignment
- wide-gamut processing
- output mapping
- HDR workflows
- mixed-camera normalization

Do not hardcode a workflow simply because Resolve is used. Project configuration still depends on source and deliverable.

---

# 6. Order of operations

A robust default order:

### Technical
1. input interpretation
2. RAW development when applicable
3. noise / dead-pixel / technical repair if needed
4. transform into working space

### Balance
5. exposure
6. white balance
7. tint
8. neutral reference alignment when appropriate
9. black / white placement

### Match
10. scene match
11. skin match
12. practical-light continuity
13. time-of-day continuity

### Creative
14. contrast shaping
15. tonal density
16. color separation
17. saturation shaping
18. hue relationships
19. look development

### Secondary
20. face / skin
21. wardrobe
22. product
23. sky / windows
24. background
25. selective highlight / shadow control

### Texture / finishing
26. halation if desired
27. bloom / diffusion
28. grain
29. subtle sharpening / softening if required

### Output
30. display rendering / output transform
31. trim pass for alternate deliverables
32. QC

This order is a default, not an immutable node tree.

---

# 7. Primary correction

The first grade should solve basic image truth before style.

Evaluate:

- exposure
- color temperature
- tint
- luminance distribution
- clipping
- shadow visibility
- neutral objects
- skin brightness
- practical-light behavior

Do not use a creative look to conceal an incorrect balance.

---

# 8. Exposure strategy

Exposure should be judged relative to:

- story
- skin
- key subject
- environment
- display target
- highlight retention
- black-floor intent

Avoid automatically normalizing every scene to the same middle brightness.

Night should not become day.
A silhouette should not be "fixed" merely because shadows are dark.

---

# 9. Contrast design

Contrast includes more than a single contrast slider.

Control:

- toe
- shadow separation
- lower midtones
- midtone density
- upper midtones
- shoulder
- specular rolloff

## Soft contrast
- lifted or gentle toe
- less aggressive midtone separation
- softer shoulder

## Dense contrast
- stronger black placement
- defined midtones
- controlled highlights

## Hard contrast
- pronounced separation
- deep shadows
- strong highlight difference

Use contrast as narrative language.

---

# 10. Highlight behavior

The goal is not merely "prevent clipping."

Decide whether highlights should feel:

- soft
- glowing
- clean
- hard
- metallic
- creamy
- hot / aggressive

Pay attention to:
- windows
- skies
- practical bulbs
- specular skin
- metal
- product highlights
- headlights

Highlight rolloff must remain consistent across a scene unless intentionally changed.

---

# 11. Shadow behavior

Choose whether shadows are:

- open
- neutral
- cool
- warm
- dense
- crushed
- textured
- milky

Crushing blacks can remove:
- skin detail
- wardrobe texture
- environmental storytelling

Lifting blacks can reduce:
- dimensionality
- perceived contrast
- depth

Use deliberately.

---

# 12. White balance and color temperature

Separate:
- technical white balance
from
- creative warm/cool bias

A scene can be technically neutralized and then intentionally biased.

Do not continually "correct" motivated sources:
- sodium vapor
- fire
- neon
- tungsten
- green fluorescent
- blue moonlight convention

The creative director should decide whether source color is:
- preserved
- neutralized
- exaggerated
- selectively controlled

---

# 13. Saturation design

Do not think only in "more saturation / less saturation."

Design:

- global saturation
- low-luminance saturation
- highlight saturation
- skin saturation
- accent-color saturation
- background saturation

Often a premium image has selective saturation rather than uniformly high saturation.

---

# 14. Hue architecture

Build relationships between:
- skin
- environment
- wardrobe
- props
- practicals
- graphics

Useful strategies:

- complementary separation
- analogous palette
- monochromatic palette
- warm subject / cool world
- cool subject / warm world
- neutral world / single accent

Do not rotate hues randomly shot to shot.

---

# 15. Skin-tone philosophy

Skin must be judged in context, not forced to a single numeric hue.

Check:

- believable hue
- luminance
- saturation
- red-channel clipping
- makeup
- mixed lighting
- ethnicity / natural complexion
- creative source color

Do not "normalize" every person's complexion to the same peach/orange result.

## Skin continuity

Across adjacent shots, preserve:
- brightness relationship
- warmth
- saturation
- makeup appearance
- cheek / forehead highlight behavior

Use scopes as support, not as an excuse to ignore the image.

---

# 16. Shot matching

Match before stylizing.

Compare adjacent shots for:

- exposure
- black level
- white balance
- skin
- saturation
- highlight density
- background luminance
- source-color behavior
- contrast
- time of day

A match is perceptual, not merely numerical.

---

# 17. Scene matching

A scene should feel like a single environment.

Maintain:

- light direction
- source temperature
- ambient level
- weather
- time progression
- window brightness
- practical brightness
- environmental palette

Do not make every angle independently "beautiful" if they stop matching.

---

# 18. Temporal consistency

Video must be judged over time.

Watch for:

- exposure breathing
- white-balance drift
- hue pumping
- saturation pulsing
- face tone changes
- flicker
- changing blacks
- changing highlights
- color noise
- temporal denoise artifacts

A perfect still frame can still belong to a bad grade.

---

# 19. AI-generated-video grading

AI sources introduce unique failures:

- skin hue changes frame to frame
- wardrobe hue mutation
- background palette drift
- unstable practical lights
- flickering highlights
- local exposure pumping
- texture/sharpness fluctuation
- inconsistent black levels
- model-to-model color mismatch

## Repair order

1. determine whether the error is generation or grade
2. stabilize global exposure / color
3. isolate affected region
4. apply temporal correction
5. repair individual frames only if needed
6. regenerate if identity / geometry changes cannot be fixed
7. re-match into sequence

Do not grade around a fundamentally broken generated shot.

---

# 20. Look development

A look should define:

- contrast curve
- color separation
- saturation mapping
- highlight color behavior
- shadow color behavior
- skin treatment
- texture
- grain
- halation / bloom
- chromatic cleanliness or contamination
- reference-display intent

A look must survive:
- bright scene
- dark scene
- interior
- exterior
- skin close-up
- wide landscape

If it only works on one hero frame, it is not yet a show look.

---

# 21. Look vs correction

Correction answers:
> Is the image technically and perceptually coherent?

Look answers:
> What world should this image belong to?

Do not use look development as a substitute for shot correction.

---

# 22. Film-emulation concepts

Film-like behavior can involve:

- tone response
- highlight compression
- dye-like color separation
- grain
- halation
- gate / weave behavior
- print-film style rendering
- reduced digital edge harshness

Film emulation is not:
> add orange highlights + grain.

Avoid stacking multiple film-emulation processes without understanding which stage they simulate:
- negative
- development
- print
- scan
- projection / display

---

# 23. Grain

Grain can:
- unify heterogeneous sources
- reduce perceived digital sterility
- add temporal texture
- soften synthetic AI surfaces

Define:
- gauge character: 65 / 35 / 16-like
- amount
- size
- chroma behavior
- luminance response

Do not use excessive grain to hide broken AI anatomy or compression artifacts.

---

# 24. Halation and bloom

Halation:
- colored glow associated with strong highlights in film-like treatments

Bloom:
- broader optical / diffusion glow around bright sources

Use subtly unless the project intentionally stylizes them.

They should react to luminance, not appear as uniform overlays.

---

# 25. Sharpening and texture

Avoid:
- excessive digital sharpening
- edge halos
- plastic skin
- uniform AI micro-detail

Prefer:
- controlled local contrast
- selective texture
- natural skin detail
- source-consistent sharpness

Different elements can require different treatment:
face ≠ product label ≠ landscape.

---

# 26. Beauty grading

For beauty / fashion:

Preserve:
- pores
- believable texture
- dimensional face shape
- eye detail
- hair detail

Use:
- subtle skin equalization
- targeted blemish repair
- localized tonal shaping

Avoid:
- plastic smoothing
- loss of facial identity
- unnaturally white skin
- uniform face blur

---

# 27. Product grading

Product color may be legally / commercially critical.

Protect:
- brand color
- label color
- material appearance
- metallic reflections
- surface finish
- packaging white
- product black

Do not creatively shift a product into an inaccurate commercial representation.

---

# 28. VFX / CG integration

Match CG or generated elements by:

- exposure
- white balance
- black level
- contrast
- saturation
- light color
- shadow color
- haze
- depth
- grain
- blur
- chromatic aberration if present
- lens softness
- motion blur

A correct composite should share the same color pipeline as the plate.

---

# 29. Graphics and titles

Graphics may require a separate display-referred path.

Protect:
- brand colors
- UI whites
- text readability
- legal text
- logos

Do not unintentionally pass display graphics through camera transforms intended for Log footage.

---

# 30. SDR mastering

Typical SDR mastering considerations:

- target gamut
- gamma / transfer function
- calibrated monitoring
- white level
- black level
- legal range when required
- compression tolerance
- consumer-display robustness

Do not simply export a scene-referred working image as SDR.

---

# 31. HDR mastering

HDR is not "brighter SDR."

Design:
- diffuse white
- specular highlights
- shadow detail
- color volume
- viewer comfort
- scene-to-scene brightness

BT.2100 defines both:
- PQ
- HLG

The chosen system depends on delivery requirements.

---

# 32. PQ

PQ is designed for absolute-display luminance mapping over a very wide range.

Use when required by:
- HDR10-type workflows
- Dolby Vision mastering
- other PQ-based deliverables

Master using a properly calibrated HDR reference path.

---

# 33. HLG

HLG is designed with broadcast-oriented compatibility considerations and is another BT.2100 HDR method.

Do not assume PQ and HLG are interchangeable encodings.

---

# 34. Dolby Vision

A common Dolby Vision mastering workflow begins with an HDR master using PQ, then uses analysis and metadata to guide mapping to other display capabilities.

The colorist must still review:
- HDR master
- mapped SDR
- trim behavior
- shot transitions
- metadata integrity

Dynamic metadata is not a substitute for creative review.

---

# 35. Multi-deliverable strategy

Possible outputs:

- SDR Rec.709
- HDR10
- HLG
- Dolby Vision
- P3 cinema
- web / mobile
- archival master

Prefer a managed master workflow when multiple outputs are expected.

Do not independently reinvent the look for each deliverable unless requested.

---

# 36. Monitoring

Trustworthy grading requires:

- calibrated display
- appropriate viewing environment
- correct output path
- disabled unintended OS color transforms
- controlled ambient light
- periodic calibration

Laptop / phone previews are useful for consumer checks but not a replacement for reference monitoring.

---

# 37. Scopes

Use:

- waveform
- RGB parade
- vectorscope
- histogram
- HDR scopes when applicable

Scopes answer technical questions.
Eyes answer creative questions.

Use both.

---

# 38. Waveform

Useful for:
- exposure
- black level
- highlight level
- shot matching
- face luminance consistency

Do not grade entirely by predetermined IRE targets.

---

# 39. RGB parade

Useful for:
- channel balance
- color casts
- clipped channels
- neutral references

A deliberately colored scene should not be neutralized merely because RGB channels differ.

---

# 40. Vectorscope

Useful for:
- saturation
- hue relationships
- skin consistency
- brand colors
- shot matching

The so-called skin-tone line is a diagnostic reference, not a rule forcing all skin onto one exact line.

---

# 41. Color script

For long-form work, map color development across story.

Example:

ACT 1
- balanced warmth
- moderate saturation

ACT 2
- cooler environment
- reduced saturation
- denser shadows

ACT 3
- separation increases
- warm accents return

ENDING
- palette resolves without simply reverting to Act 1

Color progression should reflect narrative progression.

---

# 42. Genre heuristics

These are starting points, not laws.

## Natural drama
- restrained saturation
- believable skin
- controlled contrast
- motivated source color

## Luxury commercial
- clean blacks
- controlled specular highlights
- precise product color
- selective saturation

## Horror
- controlled underexposure
- strategic color contamination
- negative space
- selective highlight attention

## Comedy
- generally readable faces
- visual clarity
- palette may be more open or saturated

## Sci-fi
- deliberate source-color logic
- clean separation
- controlled practical color
- avoid generic cyan/orange by default

## Period
- palette tied to production design
- lens / texture / print-reference logic
- avoid arbitrary sepia

---

# 43. Brand color grading

Translate brand identity into:

- palette
- contrast
- saturation
- skin philosophy
- product treatment
- background color
- graphic color
- highlight style

Do not force a brand's HEX color into every physical object.

Brand translation should remain photographic.

---

# 44. Color consistency with production design

Color grading cannot rescue uncontrolled production design indefinitely.

Coordinate with:
- wardrobe
- art direction
- makeup
- practical lighting
- props
- location

Best color grading begins before shooting.

---

# 45. Node / layer philosophy

Whether using nodes, layers, or another structure, separate conceptual jobs:

- input
- balance
- match
- look
- secondaries
- texture
- output

This makes revisions traceable.

Avoid one giant adjustment doing everything.

---

# 46. Versioning

Record:

- grade version
- show-look version
- output transform
- monitor target
- date
- colorist / agent decision
- approved reference frames

Do not silently change a show look mid-project.

---

# 47. Approval frames

Maintain representative references for:

- day exterior
- night exterior
- day interior
- night interior
- hero skin close-up
- product shot
- high-saturation scene
- low-key scene

A revised look should be tested against all representative frames.

---

# 48. Alternate-output trim

When generating:
- vertical cut
- short-form cut
- social
- SDR from HDR
- HDR from a wide-gamut master

re-evaluate:
- face brightness
- graphics
- subtitles
- specular intensity
- color volume
- dark-scene legibility

A technically valid transform can still need creative trimming.

---

# 49. Compression-aware grading

Extreme gradients, noise, grain, and chroma detail can stress delivery codecs.

Check:
- banding
- mosquito noise
- macroblocking
- shadow breakup
- grain destruction
- chroma bleed

Judge the encoded deliverable, not only the master.

---

# 50. Final grading QA

Before approval:

### Technical
- correct input interpretation
- no unintended transform
- no illegal clipping where delivery forbids it
- correct output transform
- correct gamut
- correct transfer function
- correct bit depth
- stable temporal color

### Creative
- scene matches
- skin remains believable
- attention goes where intended
- look supports story
- brand/product color is correct
- blacks/highlights match intent
- no accidental hue drift

### Delivery
- HDR / SDR mapping reviewed
- titles / graphics reviewed
- subtitles reviewed
- compressed preview reviewed
- final platform version reviewed

---

# 51. AI Creative Director decision framework

Before asking for a grade, the agent should answer:

1. What is the story purpose of color?
2. What must remain technically accurate?
3. What is the source color state?
4. What is the working-space strategy?
5. What is the target display?
6. What is the show look?
7. How should skin behave?
8. How should blacks behave?
9. How should highlights behave?
10. How should saturation behave?
11. What color progression exists across the project?
12. Which elements are continuity-critical?
13. Which AI temporal defects must be repaired?
14. What alternate deliverables are required?

Only then compile a grading brief.

---

# 52. Golden rule

**A grade is successful when the viewer experiences the intended story and never notices that color management is fighting the image.**
