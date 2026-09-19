# Continuity Bible

Continuity is state carried deliberately across shots, scenes, versions, and generated assets.

## Character
Track:
- face / identity
- hair
- wardrobe
- makeup
- body proportions
- injuries
- wetness / dirt
- emotional state
- voice state when dialogue exists

Read a character's **identity** (stable facts that don't change shot-to-shot: face, backstory, relationships, default wardrobe) and their **current state** (this scene's wardrobe/injury/emotional state, and — critically — what they currently know) as two separate lookups, not one merged file. A fact belonging to identity is not automatically something the character presently knows or that currently applies: "she has an older brother" is identity; "she doesn't yet know the letter came from him" is state. Conflating the two is how a character ends up reacting to information they haven't been given yet in the story.

## Prop
Track:
- identity / canonical asset ID
- owner
- hand / contact point
- position
- orientation
- damage or lifecycle state

## Spatial
Track:
- actor position
- body orientation
- screen direction
- eyeline
- camera side
- location geometry
- entrances / exits

## Temporal
Track:
- time of day
- elapsed story time
- season
- weather progression
- wetness / damage progression
- lighting progression

Progressive changes should use defined lifecycle states from `knowledge/state-lifecycle.md`, not random drift.

## Narrative
Track:
- what the audience knows
- what each character knows
- unresolved setup/payoff
- completed actions
- relationship state when relevant

## Shot-to-shot rule
The end state of shot N must be a valid start state for shot N+1 unless a time/space discontinuity is explicit and motivated.

## Continuity map
For sequence work, maintain a continuity record that links each shot's start/end state to:
- canonical character version
- wardrobe state
- prop state
- location state
- temporal/weather state
- light state
- camera side / screen direction
- adjacent-shot dependencies

Use `schemas/continuity.schema.json` for structured state.

## Reference Authority Hierarchy
When references conflict, use this default authority order unless the project explicitly overrides it:

1. explicit locked user/director decision
2. brand/client rule
3. approved canonical character / wardrobe / prop / location reference
4. approved keyframe or approved prior shot state
5. established project grammar
6. descriptive text interpretation
7. generic defaults

A lower-authority style reference must not silently override identity or continuity-critical facts.

## Validation
Continuity is not "looks similar." Validate identity, object state, geography, screen direction, time, light, and narrative knowledge separately. A visually attractive shot that breaks a locked continuity state is a failed shot unless the discontinuity is intentional.
