# Model Capability Profiles

Video-model capabilities are time-sensitive production data, not permanent creative knowledge.

## Registry

Use `libraries/model-capability-registry.yaml` as the machine-readable capability registry.

Every verified profile should record:

- provider
- model
- profile status
- verification date
- official source(s)
- maximum documented and practical duration
- text-to-video
- image-to-video
- multi-reference / identity reference
- first/last-frame support
- extend
- video editing
- motion transfer
- audio generation
- dialogue / lip sync
- accepted reference types
- aspect ratios / resolution
- regional / preview restrictions
- observed project-specific reliability
- major failure modes

## Freshness rule

Do not treat a capability profile as current indefinitely.

Default freshness window for model-routing decisions: **30 days**, unless the project explicitly chooses a different threshold.

If the required capability is:
- missing,
- stale,
- preview/experimental,
- provider- or region-dependent,
- or financially material,

verify it against a current official source before routing the shot.

## Project evidence outranks generic ranking

A dated generic profile is only a starting point. If the current project has demonstrated that a model performs better or worse for a specific recurring task (identity lock, hands, locomotion, dialogue, macro, camera movement), record that in project state and use the project's evidence for later shots.

## Important

Never assume all video models share the same abilities. Never invent feature support. Prompt compilation and shot complexity must adapt to the selected, verified model and generation mode.
