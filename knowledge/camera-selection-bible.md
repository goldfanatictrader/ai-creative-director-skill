# Camera Selection Bible

## Camera is not the look by itself
Final image = camera + sensor/film + lens + filtration + exposure + lighting + movement + color pipeline + finishing.

Never stop at “shot on ARRI”. Define the visual consequence: format, highlight behavior, skin rendering, micro-contrast, focus falloff, motion rendering, lens family, filtration, and finishing.

## Selection axes
- Capture format: 15/65 film, 65mm digital, VistaVision/full-frame, Super 35, Super 16, medium-format still.
- Image priority: skin, highlights, shadows, resolution, texture, global shutter, low-light, fps, VFX precision.
- Production priority: studio, handheld, gimbal, drone, car rig, high-speed, virtual production, documentary, still, fashion, commercial, narrative.

## Format behavior
- Medium-format still: extreme detail, tonal separation, product/fashion/landscape/architecture/hero portrait.
- 65mm digital: scale, dimensionality, wide field with selective depth, premium large-format language.
- Full-frame cinema: flexible large-format cinematography, shallow depth when desired, modern premium work.
- Super 35: classic cinema geometry, broad lens choice, deeper focus at equal framing, action-friendly.
- Film: organic grain, photochemical highlight behavior, temporal texture.

## Shutter behavior
Global shutter is especially useful for fast pans, vehicle work, strobes, VFX plates, rotating objects, and fast action. Rolling shutter is not automatically inferior.

## Resolution rule
Higher resolution does not automatically mean a better image. Use it for VFX extraction, reframing, large-format exhibition, product detail, or archival needs.

## Lens rule
The lens can affect perceived look as much as or more than the body: contrast, flare, focus falloff, field curvature, breathing, distortion, bokeh, edge behavior, anamorphic artifacts.

## Recommended decision order
1. narrative purpose
2. capture format
3. movement/rig requirement
4. dynamic range
5. low-light
6. frame rate
7. shutter
8. lens family
9. filtration
10. color workflow
11. finishing

## AI prompting rule
If an image is AI-generated, do not falsely claim it was literally captured by a real camera. Prefer descriptive language such as “large-format digital-cinema behavior, soft highlight roll-off, natural skin, organic micro-contrast”.

## Critical guard — real camera/lens names in generation prompts (confirmed production bug, not theoretical)
Naming a specific camera/lens/film model as a literal noun in a text-to-image/video generation prompt ("shot on Sony VENICE 2", "ARRI Alexa 35, CineAlta") has caused models to render the camera itself as a physical object inside the frame — complete with a fabricated HUD, false on-screen readouts, or watermark-style overlays — because the model treats the brand/model name as a describable object to draw, not a pure style descriptor. This is a confirmed failure mode from real production use of this skill's underlying knowledge (see `ai-video-failure-bible.md`), not a hypothetical caution.

**Rule: use this registry (`libraries/camera-registry.yaml`, `libraries/lens-registry.yaml`, `libraries/film-stock-registry.yaml`) for internal DECISION-MAKING only — selecting which image behavior fits the story — never paste the resulting `brand`/`model`/`family` field into the final generation prompt as a literal noun.** Translate the selected entry's `directorial_inference.character` list into the prompt instead:
```
selected: ARRI_ALEXA_35 + COOKE_S8_I_FF  (internal decision, not spoken in the prompt)
prompt language: "filmic highlight behavior, natural skin rendering, high dynamic-range latitude, organic film-inspired lens character, smooth natural focus falloff, humanistic rendering" (no brand/model names, no camera-as-object risk)
```
This mirrors the exact fix already required for camera-body/rig terminology more broadly in `camera-bible.md` — technical terms must stay pure style descriptors (dynamic range, color, lens character, exposure), never a product/brand noun that a model could mistake for a physical object to draw. The registry's own `sources/official-sources.md` and `verified_specs` fields exist to inform *decisions* (what look does this actually behave like) — they are reference data, not prompt copy.

## Where this fits the decision chain
Use this bible + registry at the CINEMATOGRAPHY/CAMERA step (`SKILL.md`), after `cinematography-bible.md` has established the visual language and before `camera-bible.md` §2-4 pins down shot-specific angle/height/lens/movement. The registry answers "what real-world image system would produce this look" (informs `directorial_inference` → prompt character language); `camera-bible.md` answers "where exactly is the camera for this shot." Both matter; only the second one's vocabulary (angle/height/distance/movement) is safe to state numerically in a prompt — the registry's output is always translated to adjectival character language per the guard above.
