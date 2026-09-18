# Governance & Locks

Domain: the rules governing this skill's own authority — when it must defer to a human decision, when a decision becomes immovable, and how to handle change requests against something already considered final. This is the meta-layer that makes every other "lock" mechanism in the package (cast lock, concept lock, `locked` uncertainty tag) actually mean something.

## 1. Skill Boundary Control
Know when a task has left this skill's competence and needs handoff:
- legal/brand-safety questions → flag, don't resolve (see `human-gates-feedback.md` §1)
- actual sound engineering/mixing, color grading execution, VFX compositing, encoding → these are execution-stack tooling, not creative-direction knowledge (see `SKILL.md` boundary note) — this skill can SPECIFY what's needed, not perform it
- a decision explicitly reserved for a human gate (`human-gates-feedback.md` §1) → present the decision clearly, don't make it

## 2. Human Override Priority
A decision a human has explicitly locked cannot be overridden by this skill just because a "better idea" occurs to it later. If a locked decision seems to be causing a problem downstream, surface the tension explicitly and let the human decide whether to unlock it — never quietly work around a lock.

## 3. Reversible vs. Expensive-to-Reverse Decisions
Tag decisions by how costly they are to change later:
- **Reversible / cheap**: a shot's exact camera movement before generation, a color-grading adjustment, an unlocked assumption
- **Expensive**: a cast lock after canonical assets exist, a location choice after many shots reference it, a concept choice after a full treatment is built on it
Spend more deliberation (and more explicit human confirmation, per `human-gates-feedback.md` §1) on expensive-to-reverse decisions; move fast and default-assume on cheap ones. Treating every decision with the same weight either stalls trivial choices or rushes expensive ones — both are failures of judgment, not caution.

## 4. Preproduction Lock
Before expensive generation begins (many shots, premium-tier generations), certain states should be explicitly locked: cast (`workflows/casting.md` §7), core concept, key location/production-design references, project grammar (`camera-bible.md` §12, `creative-direction.md` §Visual grammar). Generating expensively against an unlocked cast/concept risks having to redo everything downstream.

## 5. Production Freeze
Once a sequence is treated as final/near-final, further change requests must be flagged for impact (`project-state-system.md` §4 dependency/change-impact) before being applied — a "small" late change can silently invalidate several already-approved shots. State the impact explicitly and let the human decide if it's worth it, rather than applying the change and discovering the fallout later.

## 6. Final Master Audit
Before anything is called done, this is broader than technical QC — see `evals/publish-readiness.md` for the full 6-gate check (creative, continuity, technical, editorial, delivery, legal/brand). Governance's specific job in that audit: confirm every `locked` decision in `project-state-system.md` is still honored in the final cut, and that no unresolved/unconfirmed assumption from `assumptions.yaml` made it into the final version unflagged.

## 7. Self-check
- Is this decision within this skill's authority, or does it belong at a human gate?
- Is a `locked` decision anywhere being quietly worked around instead of surfaced?
- Before a late change to a near-final sequence, has its downstream impact actually been checked?
