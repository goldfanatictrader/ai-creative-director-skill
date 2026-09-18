# Workflow — Shot Design

For each shot:

1. State the shot purpose.
2. Confirm adjacent-shot / sequence context.
3. Define start state.
4. Define one primary action.
5. Mark `performance_requirement` as `required` or `not_applicable`.
6. If required, define observable performance choreography.
7. Define camera intent and exact camera specification.
8. Define motion layers.
9. Define lighting.
10. Define sound cue if relevant.
11. Define end state.
12. Populate structured continuity state.
13. Mark `reference_requirement` as `required` or `not_applicable`; resolve canonical references when required.
14. Score generative complexity.
15. Run continuity and feasibility checks.
16. Simplify if high risk.
17. Mark the shot `READY` only if Gate A in `evals/generation-readiness.md` passes.
18. Choose generation strategy.
19. Build `schemas/generation-spec.schema.json` and mark it `READY` only when Gate B passes.

A shot being creatively ready is distinct from its generation request being executable.
