# Video Taxonomy & Type Router

There is no single count of "how many kinds of video exist" — one video is often several types at once (branded + documentary + vertical + educational, simultaneously). Treat video type as a **classification along independent dimensions**, not a single label. This file is the router: classify the request first, then pull only the relevant modules — never enumerate a workflow file per subtype.

## 1. Classification Dimensions

Classify every brief along these 8 axes before designing anything. Not all axes need a definitive answer immediately — resolve the ones that materially change direction, assume the rest (state the assumption, per SKILL.md "ask only when material").

| Axis | Typical values |
|---|---|
| **Purpose** | sell, inform, entertain, persuade, document, express, train, evidence/record |
| **Format** | narrative, documentary, commercial, explainer, performance, vlog, interview, montage, immersive |
| **Genre / mood** | drama, comedy, thriller, sensory/aspirational, observational, satirical, inspirational, procedural, abstract |
| **Platform** | cinema, broadcast, YouTube, TikTok/Reels/Shorts, website, in-app, livestream, installation |
| **Duration** | micro (<15s), short (15-60s), mid (1-5min), long (5-20min), feature (20min+) |
| **Audience** | mass/general, niche/enthusiast, B2B/professional, internal/employee, investor, regulator, general public (PSA) |
| **Realism level** | photoreal live-action, stylized live-action, animation (2D/3D/stop-motion), motion graphics, hybrid |
| **Production mode** | fully controlled (scripted, blocked, lit), semi-controlled (directed documentary), observational/run-and-gun, UGC/native, live/broadcast |

A brief like *"buat iklan parfum 30 detik untuk Instagram"* classifies as:
```
purpose: sell
format: commercial (product beauty film)
genre: sensory / aspirational
platform: instagram (vertical 9:16)
duration: short (30s)
audience: mass/general, beauty-interested
realism: photoreal live-action
production_mode: fully controlled
```
This IS the routing output — it determines which knowledge/workflow modules matter (here: `workflows/commercial.md` + composition/lighting geared toward sensory macro work + minimal performance complexity, per §3 below), not a search through 100 named subtypes.

## 2. Video Families (reference — ~15 families, 100+ named subtypes live under them)

Use this table to recognize what family a request belongs to and to borrow vocabulary — not as 15 separate procedures.

| Family | Example subtypes |
|---|---|
| Narrative / Fiction | feature, short, micro-short, drama, comedy, thriller, horror, sci-fi, musical |
| Documentary | observational, participatory, investigative, biographical, essay film, docudrama, mockumentary |
| Commercial / Advertising | TVC, digital ad, testimonial, comparison, direct-response, brand film, launch film |
| Branded Content | branded documentary, founder story, manifesto, customer story, culture film, ESG film |
| Corporate / Business | company profile, investor video, internal comms, onboarding, training, recruitment |
| Product | demo, explainer, reveal, unboxing, walkthrough, beauty film, 360 product |
| Music | official MV, performance, lyric video, visualizer, live session, concert film |
| Social Media | TikTok/Reels/Shorts, POV, GRWM, trend/challenge, talking-head |
| Creator / Influencer | vlog, storytime, commentary, challenge, reaction |
| Educational | lecture, tutorial, how-to, animated explainer, masterclass, case study |
| News / Journalism | package, field report, interview, explainer, investigative report |
| Interview / Conversation | one-on-one, roundtable, podcast video, vox pop, testimonial |
| Event | wedding, conference, concert, festival, launch event, recap/highlight |
| Sports / Fitness | match coverage, highlight, athlete profile, training, tactical analysis |
| Entertainment Format | reality, variety, game show, sketch, talent show, web series |
| Animation / Motion | 2D, 3D, stop-motion, motion graphics, kinetic typography, infographic |
| Art / Experimental | video art, abstract, non-narrative, installation, loop film |
| Fashion / Beauty | fashion film, lookbook, campaign, runway, fragrance film |
| Food / Hospitality | food film, recipe, restaurant profile, hotel/destination film |
| Travel / Tourism | destination film, travel diary, itinerary video |
| Real Estate / Architecture | property tour, architectural film, drone tour |
| Automotive | commercial, driving film, review, walkaround, motorsport |
| Technology / SaaS | software demo, UI walkthrough, feature launch, AI product film |
| Gaming | trailer, gameplay, cinematic, machinima, lore video |
| Film/TV Marketing | teaser, trailer, character promo, featurette, title sequence |
| Political / Public Comm. | PSA, civic explainer, government info, policy explainer |
| Nonprofit / Advocacy | awareness campaign, fundraising film, impact story |
| Religious / Spiritual | sermon, devotional, event coverage |
| Scientific / Medical | procedure explainer, research visualization, patient education |
| Industrial / Engineering | process film, machinery demo, safety training |
| Legal / Evidence | deposition, inspection, compliance recording |
| Immersive | 360°, VR, AR, spatial, branching/interactive |
| Live / Broadcast | livestream, multicam, webinar, live commerce |
| UGC / Commerce | UGC ad, before-after, demo UGC, shoppable video |
| AI-native | generative short, AI character film, synthetic commercial, virtual influencer |

## 3. Genre Inflection Notes (what actually changes per family)

Everything in `knowledge/` and the core SKILL.md chain still applies to every family — these notes are deltas, not replacements. Where a family already has a full procedure in `workflows/`, use that; otherwise apply the standard chain with these inflections layered on top.

| Family | Has dedicated workflow? | Key inflections vs. default |
|---|---|---|
| Narrative/Fiction | `workflows/film-development.md` | Full story/character machinery applies at full weight |
| Commercial/Advertising | `workflows/commercial.md` | Single-minded proposition dominates; performance restrained; CTA/brand-visibility constraints |
| Branded Content | none — use commercial + narrative blend | Story truth matters more than sales proposition; slower pacing than TVC; avoid overt CTA |
| Corporate/Business | none — use commercial (lighter) | Very restrained performance; low camera complexity; clarity over style; talking-head-heavy |
| Product | none — use commercial (product-forward) | Macro/beauty-lighting emphasis; hero object treated like a character; motion slow/controlled |
| Music | `workflows/music-video.md` | Motion synchronized to beat overrides normal camera-motivation rule; performance can be heightened if genre calls for it |
| Social Media | `workflows/social-video.md` | Hook in first 2s overrides normal pacing rules; vertical-safe composition; caption-safe zones |
| Creator/Influencer | none — use social-video, lighter structure | Production mode often UGC/native — deliberately imperfect camera, direct-to-camera address allowed |
| Documentary | none (see note below) | **Production mode is observational, not controlled** — do not over-direct blocking/performance; camera follows rather than composes for the actor; coverage-heavy, story found in edit not pre-planned |
| Educational | none — use commercial (informational) | Clarity over style; deep focus/high-key default; minimal camera movement; pacing tied to comprehension, not emotion |
| News/Journalism | none | Similar to documentary but faster turnaround; interview coverage standard (clean OTS); minimal stylization |
| Interview/Conversation | none | Coverage-first: master + reaction + insert; eyeline/180° rule is the dominant camera concern, not movement |
| Event | none | Run-and-gun; plan coverage types (wide/medium/reaction/detail) rather than individual shot specs; heavy reliance on editorial to find structure post-capture |
| Sports/Fitness | none | Action choreography and tracking dominate; camera complexity budget is higher than default by necessity |
| Entertainment Format | none — use film-development (lighter) | Multi-cam coverage logic; format/segment structure over three-act |
| Animation/Motion | none | Physical realism constraints in `performance-bible.md`/`ai-video-failure-bible.md` relax or don't apply — style-consistency replaces photoreal-plausibility as the QC concern |
| Art/Experimental | none | Deliberately may break camera/continuity rules — state which rules are broken and why (intentional, not failure) |
| Fashion/Beauty | none — use commercial (sensory) | Similar to Product; performance is presentational not naturalistic; slow-motion and macro common |
| Food/Hospitality, Travel/Tourism, Real Estate | none — use commercial/documentary blend | Sensory/observational blend; location/production-design fidelity matters more than performance |
| Automotive | none — use commercial | Vehicle treated as hero subject — apply same object-consistency rigor as character reference (see `continuity-bible.md`) |
| Technology/SaaS | none — use commercial (informational) | Interface/product-truth accuracy is a hard constraint; restrained performance |
| Gaming | none | Realism level frequently stylized/animated; engine-capture conventions may override live-action camera grammar |
| Film/TV Marketing | none — use film-development (compressed) | Extreme compression of story into hook beats; withholding information is often the point |
| Political/Public Comm., Nonprofit/Advocacy | none — use commercial/documentary blend | Message accuracy and tone-appropriateness override stylistic ambition; legal/claim sensitivity high (flag to user, out of this skill's scope — see SKILL.md boundaries) |
| Religious/Spiritual | none | Similar to Event/Documentary blend depending on content |
| Scientific/Medical, Legal/Evidence | none | Accuracy and neutrality override style entirely; treat as documentation, not direction, in the evidentiary case |
| Industrial/Engineering | none | Process clarity over style; safety/technical accuracy is a hard constraint |
| Immersive | none | Spatial/360 composition rules replace standard framing — camera-bible.md's frame-based vocabulary partially doesn't apply; flag as a gap if requested (not yet covered) |
| Live/Broadcast | none | No regeneration/iteration possible — feasibility checking must happen in rehearsal/rundown, not per-shot before generation |
| UGC/Commerce | none — use social-video | Deliberately imperfect/native aesthetic is the goal — do not "improve" it toward cinematic polish unless asked |
| AI-native | none — this skill's home turf | The full chain applies most literally here since there is no physical production to defer to |

## 4. Router Procedure

1. Read the brief. Fill in as many of the 8 axes (§1) as the brief supports.
2. For unresolved axes that don't materially change direction, assume the most common value for that Purpose/Platform combination and state it in one line.
3. Identify the family (§2) — usually obvious from Purpose+Format together.
4. Check §3: does the family have a dedicated workflow? If yes, follow it. If no, run the standard SKILL.md chain and apply the listed inflections at the relevant steps (most inflections land at PERFORMANCE, CAMERA, or EDITORIAL RHYTHM).
5. Proceed into CREATIVE PROBLEM / CONCEPT as normal — routing is a pre-step, not a replacement for creative thinking.

## 5. When nothing fits well
If a request genuinely doesn't map to any family/inflection here (e.g. a fundamentally new format), don't force it into the nearest table row silently — name the mismatch to the user in one line and proceed with the closest applicable default from the standard chain.
