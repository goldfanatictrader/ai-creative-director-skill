# AI Video Color Repair & Temporal Consistency

## Purpose

Generated video often contains color instability that does not exist in conventionally captured footage.

## Failure classes

### Global
- exposure pumping
- white-balance drift
- global hue drift
- saturation pulsing
- contrast breathing
- black-level changes

### Character
- skin hue drift
- eye-color changes
- hair-color changes
- makeup mutation
- wardrobe hue mutation

### Environment
- sky color shift
- practical-light color shift
- wall/furniture hue mutation
- inconsistent time-of-day color
- weather color shift

### Local temporal
- highlight flicker
- moving color patches
- chroma noise
- texture hue crawling
- local tone instability

## Diagnosis

Ask first:
- Is geometry/identity stable?
- Is the problem color only?
- Is the error global or localized?
- Is it stable enough for tracking?
- Does fixing it create a worse temporal artifact?

## Repair hierarchy

1. global match
2. tracked secondary
3. temporal smoothing
4. selective frame repair
5. composite replacement
6. regenerate shot

## Reject conditions

Regenerate rather than grade when:
- face identity changes materially
- wardrobe changes shape/design
- geometry morphs
- object changes identity
- lighting direction changes implausibly
- local color instability follows broken anatomy

Color grading must not be used to conceal generation failure that changes story information.
