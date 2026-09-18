# Eval — Generation Readiness

Generation readiness has two separate gates. A valid shot is not automatically an executable generation request.

## Gate A — Shot readiness

A shot may be marked `READY` only when all applicable items pass:

- creative purpose clear
- story / sequence context clear
- start state defined
- observable action defined
- end state defined
- performance requirement explicitly marked required or not applicable
- if performance is required: performance choreography defined
- camera specified
- motion specified
- lighting specified
- continuity object populated
- reference requirement explicitly marked required or not applicable
- if references are required: canonical references resolved
- complexity score acceptable
- relevant constraints selected
- recurring identity/markings/proportions/scale locked
- recurring prop/location references resolved
- previous end-state → current start-state bridge is valid
- time/weather/wetness/light transition is motivated
- story motivation/emotional beat is legible
- animal/creature behavior rules validated when applicable
- visible vocalization sync strategy defined when applicable
- ambience/Foley obligations identified
- final shot/sequence ending behavior is planned

This gate maps to `schemas/shot.schema.json`.

## Gate B — Generation-spec readiness

An executable generation spec additionally requires:

- deliberate generation method selected
- target provider/model selected
- capability support verified when material
- prompt compiled from the approved shot spec
- duration set
- aspect ratio set
- negative constraints set
- required references supplied for the chosen mode
- first/last-frame mode has at least two references
- generation status marked `READY`

This gate maps to `schemas/generation-spec.schema.json`.

## Verdict

If Gate A fails: `SHOT NOT READY`.

If Gate A passes but Gate B fails: `SHOT READY / GENERATION SPEC NOT READY`.

Only when both pass: `READY FOR GENERATION`.
