# Constraint & Priority System

Domain: resolving competing requirements (short duration, many messages to fit, small budget, premium visual expectation) and knowing which requirements actually matter most. Covers Creative Constraint Solver, Priority System, Requirement Traceability, and Coverage Completeness as one system.

## 1. Priority Tiers
Not every brief requirement carries equal weight. Tag each one:
- **P0** — the video fails its purpose without this (the core message, the mandatory legal disclaimer, the one shot the whole concept depends on)
- **P1** — materially strengthens the work but the video still functions without it
- **P2** — nice-to-have, first to cut under any constraint pressure

When constraints collide (see §2), P2 items are cut before P1, P1 before ever touching P0. This is the actual mechanism that resolves "short duration + many messages + small budget + premium visual" — you don't average the pressure across everything, you cut by tier.

## 2. Constraint Solving Procedure
When constraints conflict (e.g. brief wants 5 messages delivered in 15 seconds at a visual bar that needs breathing room):
1. List every requirement with its priority tier (§1).
2. Identify the actual hard constraint (usually duration or budget) vs. soft aspiration (usually "premium feel").
3. Cut P2 requirements first, fully, don't dilute everything by 20% instead.
4. If still over-constrained after cutting P2, question whether a P1 can be delivered implicitly (through production design/color rather than a dedicated beat) instead of dropped outright.
5. Never silently drop a P0 — if a P0 genuinely cannot fit, that's a brief-level conflict to raise explicitly, not something to quietly solve by cutting corners.

Cramming five P0-tier messages into 15 seconds isn't solved by faster cuts — it's usually solved by admitting not all five are actually P0, and re-tiering honestly.

## 3. Requirement Traceability
Every P0/P1 requirement in the brief should be traceable to the specific scene/shot that delivers it:
```
requirement: "must show product in use" (P0)
  → delivered by: SC02_SH01, SC02_SH02
requirement: "convey warmth of brand" (P1)
  → delivered by: color/lighting treatment throughout, not a single dedicated shot
```
If a P0 requirement has no shot delivering it, that's a coverage gap (see §4) that must be caught before generation, not discovered at final review.

## 4. Coverage Completeness Check
Before finalizing a shot list, verify every P0 (and ideally P1) requirement is traced (§3) to something in the sequence. Do this as an explicit pass, not an assumption — it's easy to design an appealing sequence of shots that collectively forgets one of the brief's stated requirements.

## 5. Self-check
- Does every requirement have a priority tier, not just an implicit "everything matters" list?
- If constraints are in genuine conflict, was the fix a P2 cut (correct) or an across-the-board dilution (usually wrong)?
- Does every P0 trace to a specific place in the sequence?
