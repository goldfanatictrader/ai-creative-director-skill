# Project State System

Domain: how project memory, versioning, dependency, and uncertainty actually persist across a long project with many assets and revisions — not as abstract theory, but as an actual file convention this skill follows every time, since a markdown file describing "maintain a dependency graph" does nothing unless something concrete is read and written. Covers what the earlier 90-point brief called Project Memory Architecture, Decision Provenance, Version Control, Approval Graph, Change Impact Analysis, Dependency Graph, Conflict Resolver, and Uncertainty Management/Assumption Register as ONE coherent system rather than six separate ones.

## 1. Where State Actually Lives
Do not rely on chat/conversation memory for anything that must survive to the next session. For any project running more than a single sitting, maintain a `project-state/` directory alongside the project's assets:
```
project-state/
  project.yaml          # top-level: brief, concept, taxonomy classification, locked decisions
  scenes/SC_01.yaml      # one file per scene — scene-state (continuity-bible.md schema)
  shots/SC01_SH03.yaml   # one file per shot — shot-state (start/end, per templates/shot-spec.md)
  assets/CHAR_01.yaml    # one file per canonical asset — see workflows/casting.md #8
  decisions.log          # append-only decision log, see §3
  assumptions.yaml        # see §5
```
This mirrors what real productions already do with continuity binders and script supervisor notes — the point is not novelty, it's that the convention is actually followed every session, not just described once.

## 2. Versioning Convention
Every creative artifact that can change gets a version tag and only one is "active" at a time:
```
CONCEPT_V1, CONCEPT_V2 (active)
STORYBOARD_V3 (active)
CHAR_01_V4 (active), CHAR_01_V1-V3 (superseded, kept for reference not deleted)
SHOT_12B (a shot that branched from SHOT_12, not simply "the second attempt")
```
Never overwrite a versioned file in place — write a new version and mark the previous superseded. This is what makes change-impact analysis (§4) and revision diffing possible at all; without discrete versions there's nothing to diff.

## 3. Decision Provenance
Every locked creative decision worth remembering gets one line in `decisions.log`, tagged with WHY it exists:
```
2026-09-18 | CHAR_01 wardrobe locked to gray t-shirt | source: reference_image REF_BRIDGE_01 | by: director_decision
2026-09-18 | max shot duration 8s | source: technical_constraint (model reliability drops past ~10s this project)
2026-09-18 | no orbit camera moves | source: brand_rule (client brief explicitly restrained)
```
Source categories: `user_request`, `reference`, `brand_rule`, `director_decision`, `technical_constraint`, `model_limitation`. When a later decision seems to contradict an earlier one, check provenance first — a `technical_constraint` can be revisited if the constraint changes (e.g. a better model becomes available); a `brand_rule` usually can't be overridden by a creative preference alone.

## 4. Dependency Tracking & Change Impact
Keep dependencies explicit, not implied. A minimal dependency note per asset is enough — this does not need graph-database tooling, a flat list is sufficient at the scale this skill operates at:
```
CHAR_01_V4 (wardrobe change) affects:
  - all shots referencing CHAR_01 generated from CHAR_01_V3 or earlier keyframes
  - SC07_SH03, SC07_SH04, SC09_SH01 (already-generated, now stale)
```
When an upstream asset changes (a character's wardrobe, a location's layout, a locked color palette), check this list before assuming only the immediately-edited shot is affected — this is the mechanism that answers "if I change the wardrobe, which shots need regenerating," which otherwise gets discovered too late (after publish, or after paying for more generations than necessary).

## 5. Uncertainty Levels — Don't Let Assumptions Become Facts
Tag every non-trivial piece of project knowledge with one of five states, and keep tags visible rather than letting everything flatten into "known":
| State | Meaning |
|---|---|
| `known` | confirmed by user/reference, not going to change |
| `assumed` | a reasonable default was made per SKILL.md "ask only when material" — has NOT been confirmed |
| `inferred` | derived from other known/assumed facts, not stated directly by anyone |
| `unresolved` | flagged as needing an answer, blocking something downstream |
| `locked` | explicitly finalized and must not be silently changed (see `governance-and-locks.md`) |

Keep an `assumptions.yaml` register for anything tagged `assumed` or `inferred` that materially shapes direction:
```
- assumption: "protagonist is understood to be financially stressed based on brief tone, not explicitly stated"
  state: inferred
  affects: [wardrobe choices, apartment production design]
  confirm_by: before locking production design
```
The point of the register is that an assumption can be found and corrected cheaply before it propagates into ten locked shots — silently treating an assumption as fact is how a small misread becomes an expensive continuity problem later.

## 6. Conflict Resolution
When two sources of truth disagree (a brand bible says "clean, minimal" but a supplied reference is chaotic/gritty), don't quietly average them or silently pick one. Name the conflict and resolve by the authority order already established in `continuity-bible.md` → Reference Authority Hierarchy, extended here to non-visual conflicts:
```
1. explicit locked user/director decision
2. brand/client rule
3. approved canonical reference (character/location/prop)
4. established project grammar (knowledge/video-taxonomy.md inflections, camera-bible.md grammar)
5. generic best practice / this skill's defaults
```
If the conflict is between two things at the SAME authority level (e.g. two director decisions that contradict), that's a real unresolved conflict — flag it to the user rather than picking silently, since neither side of this skill can outrank the other.

## 7. Self-check
- Is anything load-bearing sitting only in conversation memory that should be in `project-state/`?
- Does every changed asset have a version tag, with the previous version kept, not overwritten?
- If an upstream asset just changed, has the dependency list been checked for downstream stale shots?
- Is anything currently being treated as `known` that's actually only `assumed` or `inferred`?
