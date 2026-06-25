# Workout OS — Project README

## Project Goal

Build a holistic fitness and nutrition planning OS that can be fully configured for any user via an intake questionnaire, then regenerate a personalized HTML Training OS via a Claude skill. The system is not a generic template — it is a programmable document that encodes annual planning, block sequencing, readiness gating, recovery bias, nutrition architecture, exercise media/cues, and daily practice into structured markdown files, then renders them into an interactive single-file HTML app.

The design must support any user profile. Dustin's program is the reference implementation. Every design decision should be generalizable: the intake questionnaire controls all user-specific values; the markdown files hold the logic; the skill does the rendering.

---

## Current State

- `dustin_master_program_v4.html` — exists at `~/Downloads/`
- 115kb, 1,461 lines, monolithic single-file HTML
- Useful reference output but hard to extend, hard to version, and not regeneratable from first principles
- Contains: 6-day split, 16-week macrocycle, GYR system, nutrition plan, morning circuit, night routine, equipment guide, progression rules, benchmark tracker
- Problems with v4: generated data is embedded in the HTML, warm-up/rehab are conceptually blended, no annual roadmap, no canonical exercise library, no media/cue contract, no dual Home/Hotel substitution engine, no phase/block advancement gate, intake logic is implicit not explicit

---

## Target State

```
intake-questionnaire.md  →  program-config.md (user-specific values)
           +
annual-roadmap.md        →  12-month block direction
           +
recovery-model.md        →  recovery bias + readiness adjustments
           +
philosophy.md            →  programming principles (invariant)
           +
exercises.md             →  exercise library + media/cues/substitutions
           +
progressions.md          →  phase gates + testing + logs
           +
nutrition-system.md      →  meal templates + nutrition rules
           +
daily-practice.md        →  morning rehab/prehab + night recovery
           +
screens.md               →  UX architecture only
           
           ↓
     /build-program skill
           ↓
     [username]_program_v[N].html   ← personalized, interactive Training OS
```

The `/build-program` skill reads all MD files in this directory, takes a user config (generated from intake), and outputs a single self-contained HTML file with embedded CSS and JS. No build tools, no dependencies, no server.

---

## File Map

| File | Purpose |
|------|---------|
| `README.md` | This file. Project overview, goal, state, design decisions. |
| `screens.md` | UX/product spec. Screens, sub-screens, data shown, interactions, and gaps. Should reference source data, not duplicate it. |
| `intake-questionnaire.md` | Canonical Q&A flow for generating a personalized program for any user. 20 questions with answer types, options, Dustin's answers, and program impact. |
| `annual-roadmap.md` | 12-month planning model. Defines annual roadmap, blocks, phases, and when future blocks become detailed. |
| `program-config.md` | User-specific config shape plus Dustin reference config. All user-specific values belong here. |
| `recovery-model.md` | Recovery bias, readiness trends, Yellow/Red rules, and auto-adjustment rules. |
| `philosophy.md` | The "why" document. Periodization lineage, CNS fatigue model, recomp architecture, phase logic, deload science, bodyweight progression principles. |
| `html-design-notes.md` | Generated HTML UX/design rules. Defines Today-first flow, exercise drawers, readiness rewriting, logging, and responsive layout. |
| `influences/` | Expert/system reference pages. Extracts principles from coaches and systems without copying paid routines. |
| `daily-practice.md` | Complete morning rehab/prehab and night recovery system: breathing, ab vacuum, fixed circuit, rotating movements, ankle block, and night routine. |
| `exercises.md` | Full exercise library with tempo notation, equipment tags, travel substitutes, phase variants, coaching cues, contraindications, and media references. |
| `exercise-media-source-strategy.md` | Source strategy and schema for mapping exact exercise videos/cues to Workout OS exercise IDs. |
| `exercise-media-map.md` | Canonical per-exercise mapping from Workout OS exercise IDs to reviewed/candidate external media and cue sources. |
| `source-research-log-2026-05-23.md` | Dated source research log for exercise media/cue providers and decisions before HTML regeneration. |
| `progressions.md` | If-then progression gates, daily/weekly logs, phase review tests, block review rules, Nordic tracker, and benchmark standards. |
| `nutrition-system.md` | Template-based nutrition rules, meal timing, meal prep, travel nutrition, and Dustin reference implementation. |
| `program-audit-checklist.md` | Quality-control checklist for redundancy, intra-day/inter-day/weekly/phase cohesion, warm-up/prehab separation, and generator audit rules. |

---

## Key Design Decisions (Already Made in v4)

### Annual Roadmap + Blocks
- Workout OS plans the year directionally while detailing only the current block and next block.
- Default annual roadmap: Block 1 recomp/tissue capacity, Block 2 strength or specialization, Block 3 hypertrophy/performance/endurance/skill, Block 4 consolidation or repeat cycle.
- A block is usually 8-12 weeks. A phase is usually 3-4 weeks inside a block.
- Test/deload checkpoints determine whether the user advances, repeats, deloads, or pivots.
- Recomp is a block goal, not a permanent program identity.

### Weekly Split Options

The user chooses the split architecture at intake. The recovery-biased default separates heavy lower, push, and pull work. A hypertrophy/frequency option pairs push and pull twice weekly with alternating emphasis.

| Day | Option A: Lower First | Option B: Push First | Option C: Upper Alternating Emphasis |
|-----|----------|----------|----------|
| Sunday | Legs Power | Push Heavy | Heavy Push + Support Pull |
| Monday | Moderate Push | Legs A | Lower / Legs |
| Tuesday | Zone 2 Cardio | Zone 2 Cardio | Zone 2 / Recovery |
| Wednesday | Pull | Pull | Support Push + Heavy Pull |
| Thursday | Legs B + Isolation | Legs B + Isolation | Lower B / Posterior / Isolation |
| Friday | Skill Day | Skill Day | Skill Day |
| Saturday | Mobility / Active Recovery | Mobility / Active Recovery | Mobility / Active Recovery |

Option A rationale: Legs on Sunday allows maximum recovery before next leg-adjacent session (Thursday). Push on Monday uses CNS freshness from Sunday's lower-body focus.

Option B rationale: Push Heavy on Sunday for users who want chest/shoulder work at highest energy state. Legs Monday shifts lower body to when CNS is still high but not peak.

Option C rationale: Upper-body muscles get two weekly exposures while controlling recovery cost. Day 1 emphasizes heavy push with support pull; Day 4 emphasizes heavy pull with support push. This is not two full heavy upper days. The secondary pattern uses lower volume, lower RPE, or technique/hypertrophy work so shoulders, elbows, and connective tissue can recover.

### GYR Readiness System
- 5 inputs: sleep hours, RHR vs. baseline, joint feel (1–5), energy (1–10), motivation (1–10)
- Green: train as prescribed
- Yellow: drop accessory block, reduce top sets by 1, no new PRs
- Red: recovery session only — morning circuit + mobility + zone 2 walk

### Nutrition Protocol
- Nutrition is template-based and config-driven, not universally IF-based.
- Dustin's reference config uses 16:8 intermittent fasting, early eating window, and fasted morning training.
- Other users can use no fasting, different eating windows, or macro-only tracking.
- Day-type calorie cycling, protein anchors, meal templates, travel rules, and dietary constraints are generated from config.

### Session Time Cap
- 60-minute hard cap per session, no exceptions
- Morning rehab/prehab is a separate daily practice, not the workout warm-up.
- The immediate warm-up happens right before the main session and is specific to that day's training.
- Training session structure: Readiness Check → Immediate Warm-Up → Main Session → Post-Session Log
- Daily structure: Morning Rehab/Prehab → Training Session → Night Recovery

### Exercise Media + Cues
- Every generated exercise should reference `exercises.md`.
- Exercise details include setup cues, execution cues, breathing cues, common mistakes, substitutions, progressions/regressions, contraindications, and media references.
- Media is referenced, not embedded. Missing media should show a clear "media pending" state without blocking generation.

### Current User: Dustin
- 225 lb male
- Goal: recomp (simultaneous fat loss + muscle building)
- Training: 6 days/week, Option A (Legs Sunday)
- Equipment: home gym + travel (hotel)
- IF: 16:8, 8am–2pm eating window
- Trains fasted with pre-workout amino stack + matcha
