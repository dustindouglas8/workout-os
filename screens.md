# Training OS — Screen Architecture

## Screen Architecture Overview

```
ONBOARDING / INTAKE
│  └─ Generates: program config (user-specific values)
│
├─ ANNUAL ROADMAP VIEW (12-month block map)
│   └─ Click block → BLOCK PLANNING VIEW
│
├─ BLOCK PLANNING VIEW (current + next block)
│   └─ Click week → WEEKLY CADENCE VIEW
│
├─ WEEKLY CADENCE VIEW (7-day cards)
│   └─ Click day → DAILY SESSION VIEW
│
└─ DAILY SESSION VIEW (the core screen)
    ├─ 4a. Morning Rehab/Prehab Session (daily practice)
    ├─ 4b. Training Readiness Check (pre-session gate)
    ├─ 4c. Immediate Warm-Up (muscle-specific, day-specific)
    ├─ 4d. Main Session (exercise table, GYR-modified)
    ├─ 4e. Post-Session Log
    └─ 4f. Night Recovery (closing reminder)

Supporting Screens (accessible from nav or contextual links):
    ├─ PROGRESSION RULES + TESTING VIEW
    ├─ NUTRITION & MEAL PREP VIEW
    ├─ EXERCISE LIBRARY / MEDIA VIEW
    ├─ EQUIPMENT INTEGRATION VIEW
    └─ TRACKER / ANALYTICS VIEW
```

---

## Screen 1: Onboarding / Intake

**Purpose:** Collect user-specific inputs required to generate a personalized program config. The output of this screen is a structured config object (or markdown config file) that controls all subsequent screens. No user-specific value should be hardcoded anywhere else.

### Sections (in order)

1. **Goals**
   - Primary training goal: Recomp / Bulk / Cut / Performance / Maintenance
   - Timeline commitment: 8 weeks / 12 weeks / 16 weeks / 12-month roadmap
   - Top 3 priorities from list (aesthetics, strength, mobility, endurance, skill, longevity)
   - Next-block preference: Strength / Hypertrophy / Mobility-Rehab / Endurance / Skill specialization / Decide from tests

2. **Training Frequency**
   - Sessions per week: 3 / 4 / 5 / 6
   - Available training days (checkboxes: Sun/Mon/Tue/Wed/Thu/Fri/Sat)
   - Session time cap (30 / 45 / 60 / 90 min)
   - Time of day preference: Morning fasted / Morning fed / Afternoon / Evening

3. **Schedule Constraints**
   - Weekly start day preference (Sunday / Monday)
   - Split architecture: Lower First / Push First / Upper Alternating Emphasis
   - Travel frequency: Never / 1–2x/month / Weekly
   - Travel equipment typically available: Body weight only / Resistance bands / Hotel gym (cables, dumbbells) / Full gym

4. **Equipment Inventory**
   - Bodyweight (always present)
   - Pull-up bar (yes/no; mounted / doorframe / rings)
   - Gymnastic rings (yes/no)
   - Resistance bands (yes/no; light / medium / heavy / loop bands)
   - Weight vest (yes/no; fixed weight / adjustable; current load)
   - Sliders / furniture movers (yes/no)
   - Kettlebell (yes/no; weight)
   - Dumbbell set (yes/no; weight range)
   - Jump rope (yes/no)
   - Yoga mat (yes/no)
   - Stability ball / exercise ball (yes/no; size if known)
   - Foam roller / lacrosse ball (yes/no)
   - Pneumatic compression sleeves (yes/no)

5. **Travel Frequency & Hotel Availability**
   - How often do you travel: Never / 1x month / 2–3x month / Weekly
   - What's typically available when you travel (multi-select from equipment list above)

6. **Health / Rehab History**
   - Injury areas to monitor (multi-select): Shoulders/rotator cuff / Lower back / Hip flexors / Knees / Ankles / Neck/upper traps / Other (free text)
   - Any current pain or active injury: yes/no + free text
   - Movement limitations (e.g., can't fully overhead press, deep squat restriction): free text

7. **Fitness Baseline**
   - Bodyweight (lbs)
   - Pull-up reps (clean, chest to bar): 0 / 1–3 / 4–6 / 7–10 / 10+
   - Pull-up form quality: Kipping / Partial ROM / Full ROM / Weighted
   - Zone 2 cardio: None / Walk only / Run 20–30 min / Run 45+ min
   - Yoga or mobility practice: None / Occasional / Weekly dedicated practice
   - Training age (years of consistent training): 0–1 / 1–3 / 3–5 / 5–10 / 10+

8. **Preferences**
   - IF protocol: None / 12:12 / 14:10 / 16:8 / 18:6 / 20:4
   - Eating window (start time → end time)
   - Macro tracking level: None / Loose (protein only) / Moderate (protein + calories) / Strict (all macros)
   - Pre-workout stack: None / Caffeine only / Aminos + caffeine / Full stack (specify)
   - Fasted training: Yes / No
   - First intake before training (if training fasted): Nothing / Water only / Aminos/EAAs / Coffee or matcha / Other
   - Skill day preference: Boxing / Animal flow / Tai Chi / Salsa / Yoga / Other / No skill day

9. **Annual Roadmap + Program Output**
   - Based on all inputs, generates `program_config.json` or equivalent structured object
   - Config controls: annual roadmap, current block, drafted next block, split selection, session structure, equipment substitutions, macro targets, phase lengths, warm-up movements, rehab/prehab focus areas

---

## Screen 2: Annual Roadmap / Block Planning View

**Purpose:** Show the 12-month direction while fully detailing only the current block and drafted next block. The annual roadmap should answer "what are we building toward?" while the active block answers "what do I do this week?"

### Data Shown
- 12-month roadmap grouped into 4 blocks of 8-12 weeks
- Current block marked as `Full Detail`
- Next block marked as `Draft`
- Later blocks marked as `Directional`
- Current block week grid
- Each week cell in the current block shows:
  - Week number
  - Phase label (Ph1 / Ph2 / Ph3, or equivalent for block length)
  - Week type tag: Normal / Deload+Benchmark
  - Relative intensity indicator (Low / Moderate / High / Peak — derived from phase + week-in-phase position)
- Deload/test weeks highlighted with distinct color/badge
- Current week indicator: bold border or "YOU ARE HERE" badge
- Phase separators between 3-4 week loading waves

### Interactions
- Click any block → opens block summary and detail level
- Click current-block week cell → opens Weekly Cadence View for that week
- Click deload/test week → opens benchmark test summary for that checkpoint
- Phase label → opens Phase Summary panel (goals, focus, key exercises for that phase)
- Hover/tap week → shows mini-summary: days trained, primary focus, deload Y/N

### Intensity Curve Visualization
- Bar chart or sparkline below the grid showing weekly volume/intensity across the active block
- Deload dips clearly visible
- Phase ramp-ups visible
- **Missing in v4** — this is a v5 addition

### Phase / Block Gate Checklist
- Shown during each test/deload week and one week before block transition
- Pulls rules from `progressions.md`
- Returns one recommendation: Advance / Repeat / Deload / Pivot
- Allows coach/user override with required reason
- Uses benchmark results, readiness trends, pain, adherence, and body composition data when relevant
- **Missing in v4** — this is a v5 addition

---

## Screen 3: Weekly Cadence View

**Purpose:** Show the current week's full training plan at a glance. Enable quick navigation to any day's session. Surface readiness and intensity distribution for the week.

### Data Shown
- 7-day card row (Sunday–Saturday)
- Each card shows:
  - Day name + date
  - Session focus label (e.g., "Legs Power", "Heavy Push + Support Pull", "Support Push + Heavy Pull", "Zone 2", "Skill", "Mobility")
  - Time cap badge (60 min / 45 min / 30 min)
  - Intensity tag: High / Moderate / Low / Recovery (visually color-coded)
  - GYR readiness badge (Green / Yellow / Red / Not yet checked) — tappable
  - Completion checkmark (if logged)
- Current day highlighted
- Split architecture toggle at top of screen — Lower First / Push First / Upper Alternating Emphasis

### Interactions
- Click any day card → opens Daily Session View for that day
- Tap GYR badge → opens readiness check (Screen 4a) for that day
- Split toggle → reconfigures the week while preserving recovery rules and hard-day spacing
- Click week header → opens Monthly Planning View

### Intensity Distribution Bar Chart
- Shows distribution of training load across the 7 days for the current week
- Visual: stacked horizontal bars or small column chart with High/Moderate/Low/Recovery segments
- **Missing in v4** — this is a v5 addition

### Week Summary Header
- Phase indicator (Ph1 / Ph2 / Ph3)
- Week number in phase (e.g., "Week 3 of 5 in Phase 1")
- Volume target for the week (e.g., "~18 working sets")
- Deload flag if applicable

---

## Screen 4: Daily Session View

*This is the most important screen. It is where the user lives every day. The morning rehab/prehab session is separate from the training warm-up. The training portion still has a fixed order: readiness check → immediate warm-up → main session → post-session log.*

---

### 4a. Morning Rehab/Prehab Session

**Purpose:** Show the daily practice that maintains tissue quality, joint readiness, and recovery capacity. This is not the workout warm-up and should not be treated as training volume.

**Source:** `daily-practice.md`

**Includes:**
- Nasal breathing or downshift breath.
- Ab vacuum if enabled in config.
- Fixed rehab/prehab foundation.
- Rotating rehab/prehab movements based on user needs and day context.
- Ankle/foot block when appropriate.

**Rules:**
- Effort ceiling stays low.
- Morning session can still happen on Red days unless pain or medical flags say otherwise.
- This block should show exercise cue/media drawers from `exercises.md`.
- If the user trains later in the day, the morning session remains separate.

---

### 4b. Training Readiness Check (Pre-Session Gate)

**Purpose:** Surface a 5-input readiness check before any training load is shown. The output (Green / Yellow / Red) controls what version of the training session the user sees. This is not optional before main training.

**5 Inputs:**

| Input | Type | Scale |
|-------|------|-------|
| Sleep last night | Number | Hours (3–10+) |
| Resting heart rate | Number | vs. baseline (e.g., "My baseline is 58; today is __") |
| Joint feel | Slider | 1 (stiff/painful) – 5 (smooth/loose) |
| Energy level | Slider | 1–10 |
| Motivation to train | Slider | 1–10 |

**Scoring Logic:**

- Green: Sleep ≥ 7h AND RHR within +5 of baseline AND joint feel ≥ 3 AND energy ≥ 6 AND motivation ≥ 5
- Yellow: Any 1–2 inputs below threshold (not all failed)
- Red: Sleep < 5h OR RHR > +10 above baseline OR joint feel ≤ 2 OR 3+ inputs below threshold simultaneously

**Output: Day-Specific Modification Instructions**

These are not generic. Each day's modification plan is pre-written based on what that day's main session contains.

- Green: Proceed as programmed. Top sets at prescribed weight/load.
- Yellow: Drop accessory block. Reduce working sets by 1 per exercise. No new PRs. Add 90s rest between compounds.
- Red: Recovery session only. Skip the main session; use the recovery prescription from `recovery-model.md`.

*The readiness check output must load BEFORE the warm-up block renders. Do not show the main session until readiness is resolved.*

---

### 4c. Immediate Warm-Up (Muscle-Specific, Day-Specific)

**Purpose:** Prime today's specific muscles and joints for the movements in today's main session. This is not generic. It is directly informed by which muscles are being trained today.

**This block is the key missing piece in v4.** In v4, warm-up movements are buried in the morning circuit section without explicit connection to today's session. In v5, this is a distinct, named, visible block that appears immediately before the main session.

**Block Structure:**

**Morning Rehab/Prehab Reference:**
The fixed foundation from `daily-practice.md` may be shown as completed context, but it is not repeated here unless the session occurs immediately after waking and the user has not already completed the morning session.

**Duplicate guard:** No exercise that appeared in the morning circuit (F1–F4 or R1–R2) may appear again in the immediate warm-up without a documented reason (different dose, different intensity, different purpose). If the morning rotation (R1/R2) already included band pull-apart, scapular pull-up, glute bridge, or any other day-specific primer, the warm-up must use a different drill or show the morning version as completed and reduce the warm-up to the remaining unmet needs. The warm-up must own exercises that are NOT already owned by the morning circuit.

**Friday skill day — CARs rule:** The full joint CARs circuit listed as the Friday warm-up is the entire warm-up. It must not appear again as a "Mandatory Warm-Up" block at the start of the main session. If the skill session requires its own warm-up, it must be a different set of movements or labeled as ramp sets for the first skill. The CARs circuit is owned by the immediate warm-up block.

| Code | Movement | Primary Target | Why Fixed |
|------|----------|---------------|-----------|
| F1 | Band external rotation | Infraspinatus + teres minor | Shoulder joint protection before any upper body load |
| F2 | Hip flexor kneeling stretch + posterior tilt | Psoas + lumbar spine | Counteracts hip flexor dominance from sitting; pre-loads hollow body position |
| F3 | Dead bug (exhale each rep) | TVA + diaphragm | Same co-contraction needed for pull-ups, presses, and ab vacuum |
| F4 | Tibialis raise + single-leg calf raise | Tibialis anterior + soleus | Daily ankle/knee load management at 225lb |

**Day-Specific Activation Layer:**
2–3 additional movements that directly prime the muscles loaded in today's main session. These replace or extend the F1–F4 foundation.

| Day | Primary Muscles Loaded | Day-Specific Activation |
|-----|----------------------|------------------------|
| Sunday (Legs A — Option A) | Quads, glutes, hamstrings, adductors | Glute bridge × 15, Lateral band walk × 10/side, Ankle pogo × 15 |
| Sunday (Push Heavy — Option B) | Chest, anterior deltoid, triceps | Band pull-apart × 15, Scapular push-up × 10, Shoulder CARs × 5/side |
| Monday (Moderate Push — Option A) | Chest, anterior delt, triceps | Band pull-apart × 12, Scapular push-up × 8, Wall slide × 10 |
| Monday (Legs A — Option B) | Quads, glutes, hamstrings | Glute bridge × 15, Lateral band walk × 10/side, Ankle pogo × 15 |
| Tuesday (Zone 2) | Cardiovascular system, hips, ankles | Hip circle × 10/side, World's greatest stretch × 3/side, Ankle roll × 10/side |
| Wednesday (Pull) | Lats, rhomboids, biceps, scapular stabilizers | Scapular pull-up × 8, Band pull-apart × 15, Dead hang × 20–30s |
| Thursday (Legs B + Isolation) | Glutes, hamstrings, adductors, calves | Glute bridge × 15, Nordic prep (lowering only) × 3, Ankle pogo × 15 |
| Friday (Skill) | Varies by skill type | Full joint CARs circuit × 1 round (hips, shoulders, neck, ankles) |
| Saturday (Mobility) | Entire kinetic chain | 90/90 hip stretch × 60s/side, Thoracic rotation × 10/side, Pigeon prep × 60s/side |

**Target Muscle Primer Callout:**
A brief text block at the top of the warm-up block that reads:
> "Today loads: [primary muscles]. Today's activation primes: [activation target]. These movements directly transfer to: [main session exercise names]."

Example for Wednesday Pull:
> "Today loads: lats, rhomboids, biceps, scapular stabilizers. Activation primes: scapular retraction + depression, shoulder joint centration, grip endurance. These movements directly transfer to: dead hang, scapular pull-up, full pull-up, cable row."

**Phase-Specific Reps:**
Warm-up reps shown inline, adjusting by phase:
- Phase 1: Lower reps, emphasis on position and hold (e.g., "Glute bridge × 10, 3s hold")
- Phase 2: Higher reps, some tempo (e.g., "Glute bridge × 15, 2-0-1-0")
- Phase 3: Loaded where applicable (e.g., "Glute bridge × 12 with band above knees")

---

### Morning Rehab/Prehab Content Rules

**Purpose:** Systematic low-load work on connective tissue, joint health, and structural imbalances. This content belongs in the morning rehab/prehab session, separate from the immediate training warm-up. It can also appear as the Red-day recovery prescription when main training is skipped.

**Core Design Principle:** This block is labeled "maintenance infrastructure" in the UI. Copy: *"This is what keeps you training for years, not weeks. It compounds quietly. 5–8 minutes, every day."*

**Focus Areas:**

| Area | Rationale | Primary Exercises |
|------|-----------|-------------------|
| Shoulders / rotator cuff | High injury rate, often the first thing to fail as load increases; 225lb overhead pressing requires daily cuff maintenance | Band ER (F1 from circuit) + shoulder CARs |
| Lower back / hip flexors | Hip flexors chronically shortened from sitting, driving anterior pelvic tilt and lumbar compression; core of rehab stack | Hip flexor stretch (F2) + McGill curl-up or cat-cow |
| Knees / ankles | Daily load at 225lb; tibialis raise manages patellar tendon load; soleus raise addresses Achilles | Tibialis raise (F4) + terminal knee extension (band) |
| Neck / upper traps | Chronically loaded from desk posture and pull-up grip; often the source of referred shoulder pain | Chin tuck × 10, cervical rotation × 5/side, trap release (lacrosse ball if available) |

**Block Format:**
- 3–4 exercises
- 5–8 minutes total
- Sets are 1–2 only; intensity is 30–40% max; no failure, no fatigue
- Coaching note on each: "You are not training these. You are maintaining them."

**Day-Specific Rehab/Prehab Adjustments:**
- After heavy lower body (Sunday Legs, Thursday Legs B): add hip flexor release + glute med work
- After heavy pull (Wednesday): add extra band ER sets + thoracic extension
- After heavy push (Monday or Sunday Option B): add pec minor stretch + serratus activation
- Rest days: extend block to 10 minutes, add foam rolling protocol

---

### 4d. Main Session

**Purpose:** The primary training stimulus for the day. Fully structured, with GYR-gated modifications, phase selectors, and travel mode toggle.

**Exercise Table Format:**

| Exercise | Sets × Reps | Tempo | Equipment | Note |
|----------|-------------|-------|-----------|------|
| [Name] | [e.g., 3 × 8] | [e.g., 4-2-1-0] | [vest / slider / home-only / travel-ok / rings] | [coaching cue or load note] |

*Tempo notation: eccentric-pause-concentric-pause (seconds). 0 = no pause / explosive.*

**Exercise Detail Drawer:**
Every exercise name opens a drawer populated from `exercises.md`:
- Setup cues, execution cues, breathing cues, and common mistakes.
- Primary and secondary muscles.
- Progression and regression.
- Home/hotel/bodyweight substitutions.
- Contraindications and caution flags.
- Video/photo reference when `media.status = approved` or `needs_review`.
- "Media pending" state when no media exists yet.

**Block Structure within Main Session:**

1. **Ankle Stiffness Block** (always first, 4 min)
   - Pogo hops × 15 (or single-leg balance × 30s/side on rest days)
   - Tibialis raise × 20
   - Single-leg soleus raise × 10/side
   - Runs before every main session.
   - **Completed-context rule:** If the user completed the morning ankle block (Section 4 of `daily-practice.md`) before this session, the generator must display it as completed context and omit the tibialis raise and single-leg soleus raise from this block. Pogo hops may be kept as a session-specific elastic primer if the day is lower-body dominant. Tibialis and soleus volume must not appear three times in one day.

2. **Primary Compound Block**
   - 2–3 primary exercises (e.g., pull-up progression, squat variation, hinge)
   - Full prescribed sets × reps
   - Tempo and rest as specified
   - These do NOT get dropped on Yellow (only top set count reduces by 1)

3. **Accessory / Isolation Block**
   - 3–5 supporting exercises (e.g., face pull, lateral raise, Nordic, slider curl)
   - These ARE dropped on Yellow
   - Entirely skipped on Red

**GYR Auto-Modification:**

| GYR Status | Compound Block | Accessory Block | Load |
|------------|---------------|-----------------|------|
| Green | As programmed | As programmed | Full |
| Yellow | −1 working set per exercise | Dropped entirely | −10% or bodyweight only |
| Red | Skip main session | Skip | Recovery only |

*GYR status is set in Screen 4a. The main session block renders the correct version automatically based on that selection — the user should not have to remember what "Yellow" means while looking at the exercise table.*

**Phase Selector:**
- Inline phase toggle (Ph1 / Ph2 / Ph3) adjusts:
  - Rep ranges (Ph1: higher reps, Ph2: moderate, Ph3: lower reps + tempo)
  - Set counts (Ph1: 2–3, Ph2: 3, Ph3: 3–4)
  - Tempo notation (Ph1: controlled, Ph2: moderate tempo, Ph3: strict tempo or 1.5-rep)
  - Notes column (Ph1: technique focus, Ph3: load/complexity focus)
- Default: current phase from program config
- User can manually select a different phase (useful for deload or testing)

**Travel Mode Toggle:**
- Switches equipment tags from home-configured to travel-available
- Replaces home-only exercises with pre-written travel substitutes
- Travel mode does NOT remove exercises — it substitutes them
- All substitutes maintain the same movement pattern (e.g., pull-up → TRX row or band pull-apart)
- Visual indicator: orange "TRAVEL MODE" banner across top of main session block

**Intensity Wave Badge (new in v5):**

Displayed as a persistent banner at the top of Screen 4d, above the exercise table:

> **Week 2 of Phase 1 · Moderate load · RPE target: 7–8 · RIR target: 2–4**

- Calculated from `current_week_in_phase` in program config + the Intra-Phase Intensity Wave table in `progressions.md`
- Updates automatically each week — the user never needs to calculate this
- On deload weeks: banner reads "**Deload week · RPE target: 4–5 · Stop every set with 6+ reps in reserve**"
- Explosive/skill exercises show a different badge: "**Quality 1 — Pattern focus**" / "**Quality 2 — Expression**" / "**Quality 3 — Performance**" depending on phase

**Ramp Set Rows (new in v5):**

Before the first working set of each primary compound exercise, two greyed-out rows appear labeled "Ramp":

| Ramp 1 | ~50% weight · 5 reps | — | — | Feel the pattern. Confirm joint readiness. |
| Ramp 2 | ~75% weight · 3 reps | — | — | Prime the path. Stop 6+ RIR. |

- Ramp rows are not logged as working volume
- Styled visually distinct (greyed out, no set counter)
- Only appear on primary compound exercises (tagged in the block structure)
- On deload weeks, ramp rows only — no working sets for accessory block

---

### 4e. Post-Session Log

**Purpose:** Capture session completion and notes. Brief — 60 seconds to complete.

**Fields:**

| Field | Type |
|-------|------|
| Did you complete the session? | Yes / Modified / No |
| GYR status used | Green / Yellow / Red |
| Session RPE | 1–10 slider |
| Any form notes or observations | Free text (optional) |
| Link: Sunday Benchmark Log | Shown only on Sunday of deload week |

**Auto-saved locally.** History viewable in Screen 8 (Tracker / Analytics).

---

### 4f. Night Recovery (Closing Reminder)

**Purpose:** Surface the 7-movement parasympathetic wind-down sequence as a closing block at the bottom of every daily session view. This is shown after the post-session log. It is not interactive — it is a reminder card.

**Label:** *"Night Recovery — 7 movements, 7 minutes. Not optional for recovery."*

**Content:** The full 7-movement sequence (detailed in daily-practice.md).

**Design note:** This block should be visually distinct (low-contrast, calm color palette) to signal a gear-shift from training to recovery. It is the last thing the user sees before closing the app for the day.

---

## Screen 5: Progression Rules + Testing View

**Purpose:** Display the if-then gates from `progressions.md` that govern when to add reps, sets, load, complexity, repeat a phase, deload, or pivot the next block. Users should consult this view during normal progression and formal test weeks.

### Primary Lift Progression Gates

Each primary exercise has a defined progression standard. Format:

> **[Exercise]**
> Gate: [minimum standard to advance]
> Next step: [what changes — reps, load, tempo, variation]
> Regression (if stuck): [what to back off to]

**Pull-Up Progression (example):**
- Gate: 3 × 5 clean reps (full ROM, dead hang start, chest approaches bar, no kipping)
- Next: Add 1 rep per set per week until 3 × 8
- Then: Add tempo (3-1-1-0) until tempo reps hit 3 × 6
- Then: Introduce vest or Ring pull-ups
- Regression: Band-assisted or eccentric-only (5s lowering) until gate is met

### Nordic Curl Progression Tracker
- Phase 1: Eccentric only (5s lowering, assisted return) × 3 sets × 4 reps
- Phase 2: 4s lowering, self-return allowed × 3 sets × 5 reps
- Phase 3: Full Nordic + band assist for concentric × 3 sets × 5 reps
- Full Nordic (no assist): program graduation milestone
- Gate to advance: 2 consecutive weeks at current phase standard without form breakdown

### Ankle Stiffness Progression
- Phase 1: Pogo hops (bilateral) × 15 + tibialis raise × 20 + soleus raise × 10
- Phase 2: Add single-leg pogos × 10/side; increase tibialis raise to 3 × 20
- Phase 3: Single-leg pogo on slight incline or uneven surface × 10/side; add depth drop landing mechanic
- Gate: Heel-toe separation clean at landing (no heel collapse), no knee valgus, no Achilles soreness

### Phase Benchmark Tests

| Metric | Phase 1 Target | Phase 2 Target | Phase 3 Target | All-Program Goal |
|--------|---------------|---------------|----------------|-----------------|
| Max clean pull-ups | 5 | 8 | 10 | 12 |
| Single-leg balance (eyes closed, seconds) | 20s | 30s | 40s | 45s |
| Pogo hops (bilateral, reps before form breaks) | 20 | 30 | 40 | 50 |
| Ab vacuum hold (seconds) | 10s | 20s | 30s | 45s |
| Bodyweight (lbs) | Trending ↓ | Trending ↓ | Stable or ↓ | Net −10–15 from start |
| HRV trend (subjective or measured) | Stable | Improving | Consistently improving | — |

---

## Screen 6: Nutrition & Meal Prep

**Purpose:** Full nutritional architecture for the user's selected eating pattern, day-type calorie cycling, meal templates, meal prep system, and travel protocols. Dustin's reference program uses IF, but IF is not universal.

### Daily Nutrition Timeline

```
FASTED WINDOW (2am → 8am training window)
│
├── Wake: Nasal breathing 2min → Ab vacuum × 3
├── Pre-training: Matcha + pre-workout amino stack
│   └── Stack: [populated from user config — aminos, creatine, electrolytes]
│
├── TRAIN (fasted, protected by amino stack)
│
└── 8:00am: EATING WINDOW OPENS
    ├── Meal 1A — 8:00–8:30am: Immediate post-training
    │   └── High protein + fast carbs (e.g., protein shake + fruit, or eggs + rice)
    ├── Meal 1B — 10:00–11:00am: Second feeding
    │   └── Balanced macros (protein + complex carb + vegetable + healthy fat)
    └── Meal 2 — 1:30–2:00pm: Closing window
        └── High protein + fat, minimal carb (e.g., salmon + avocado + leafy greens)

FASTING RESUMES at 2:00pm → next day 8:00am
```

If the user does not use intermittent fasting, the generated timeline should instead show normal meal timing around training, protein distribution, hydration, and any dietary constraints from `program-config.md`.

### Day-Type Calorie & Macro Targets

| Day Type | Calories | Protein | Carbs | Fat | Notes |
|----------|----------|---------|-------|-----|-------|
| Heavy training (Sun/Mon/Wed/Thu) | Higher | 1g/lb BW min | Moderate-high | Moderate | Carbs timed around training |
| Moderate training (Fri/Sat) | Moderate | 1g/lb BW min | Moderate | Moderate | |
| Zone 2 / Skill (Tue/Fri) | Moderate-low | 1g/lb BW min | Lower | Moderate-high | Fat-adapted support |
| Rest day | Lower | 1g/lb BW min | Low | Higher | Protein anchor maintained |

*All targets populated from user config based on bodyweight and goal (recomp / bulk / cut).*

### Ab Vacuum Protocol
- Timing: fasted, first thing, before eating window opens
- Position progression by week:
  - Weeks 1–4: Standing (hands on knees, slight forward lean)
  - Weeks 5–10: All-fours (tabletop position, gravity assists visceral draw)
  - Weeks 11–16: Hanging (dead hang from pull-up bar, maximum gravity assist)
- Hold target: Phase 1: 10s × 3 / Phase 2: 20s × 3 / Phase 3: 30s × 3
- Connection to pull-up: same TVA contraction required for hollow body position

### Sunday Meal Prep Timeline

```
Sunday (after training session):
├── 10:00am: Protein cook (batch chicken, ground turkey, or eggs)
├── 10:30am: Carb cook (rice, sweet potato, or oats batch)
├── 11:00am: Vegetable prep (leafy greens, cruciferous, roasted)
└── 11:30am: Portion and container → 5–6 meals for Mon–Fri
```

### Travel Nutrition Protocol
- Priority 1: Maintain protein anchor (1g/lb BW) — carry protein powder if needed
- Priority 2: Maintain fasting window (negotiable ± 1 hour)
- Priority 3: Carb quality drops (accept processed options rather than skipping)
- Red lines: Do not break fast with pure fat/sugar; do not skip post-training protein window
- Hotel options: eggs + fruit (breakfast bar), Greek yogurt + nuts, protein shake in room

---

## Screen 7: Exercise Library + Equipment Integration

**Purpose:** Maximize use of available equipment and expose exercise details. Show the value hierarchy, phase integration schedule, substitution map, and media/cue drawer for each exercise.

### Exercise Media / Cue Drawer
- Search or browse exercises from `exercises.md`.
- Each exercise shows setup cues, execution cues, breathing cues, common mistakes, progressions, regressions, substitutions, contraindications, and media status.
- Approved video/photo media appears inline or as a link.
- Missing media displays "media pending" while still showing cues.
- Draft external media is marked `needs_review`.

### Vest ROI Ranking
Priority order for when to add vest:
1. Pull-ups (highest ROI — adds progressive overload without changing movement pattern)
2. Push-ups (close second — increases chest/tricep demand significantly)
3. Dips (if rings or dip station available)
4. Walking lunges or step-ups (lower body option on travel or home)
5. Pogo hops (Phase 3 only — adds tendon loading for advanced ankle stiffness work)

Phase integration:
- Phase 1: No vest (movement quality first; vest masks technique flaws)
- Phase 2: Vest introduced for pull-ups only (after 3×8 gate met)
- Phase 3: Vest for pull-ups + push-ups; optional for lower body

### Sliders — 4 Gap-Fix Movements
Sliders address movements that have no clean bodyweight substitute:

| Movement | Gap Fixed | Phase Introduced |
|----------|-----------|-----------------|
| Slider hamstring curl | Prone hamstring isolation | Phase 1 |
| Slider pike | Ab + hip flexor compound (no bar needed) | Phase 1 |
| Slider lateral lunge | Adductor + quad (single-leg, no split squat) | Phase 2 |
| Slider body saw | Plank → anti-extension overload | Phase 2 |

### Rings Guide
- Dead hang + scapular pull-up: Phase 1 (stability and shoulder health)
- Ring row: Phase 1–2 (scalable horizontal pull)
- Ring push-up: Phase 2 (instability adds rotator cuff demand)
- Ring dip: Phase 2–3 (after pressing base established)
- Ring muscle-up: Phase 3 goal (if applicable to user)

### Full Inventory with Upgrade Paths

| Equipment | Current | Next Upgrade | Unlock Criteria |
|-----------|---------|--------------|-----------------|
| Pull-up bar (mounted) | Have | Rings | Phase 2, 3×8 pull-ups |
| Sliders | Have | Weighted vest | Phase 2 complete |
| Resistance bands (multiple levels) | Have | KB or DB set | Phase 3 or travel need |
| Weight vest | Have | Adjustable vest (heavier plates) | Phase 3, current vest maxed |
| Yoga mat | Have | Foam roller + lacrosse ball | Anytime — low cost, high rehab ROI |
| Stability ball | Have | Keep if correctly sized | Core rehab, hamstring curl, wall squat, supported mobility |
| Jump rope | Have | Weighted jump rope | Phase 2 — adds upper body demand |

---

## Screen 8: Tracker / Analytics

**Purpose:** Log daily execution, weekly trends, phase tests, block reviews, and annual progress. The tracker is what lets the next block be adjusted from real data instead of assumptions.

### Daily Training Log

Captured after each training session:

| Field | Input Type |
|-------|-----------|
| Date | Auto-populated |
| Planned session | Auto-populated |
| Completed status | Completed / Modified / Skipped |
| Readiness color | Green / Yellow / Red |
| Session RPE | Slider 1-10 |
| Pain score | 0-10 |
| Pain location | Text |
| Main lift result | Text or structured input |
| Notes | Optional free text |

### Weekly Sunday Baseline Log (9 Fields)

Captured every Sunday (or first training day of the week):

| Field | Input Type |
|-------|-----------|
| Date | Auto-populated |
| Bodyweight (lbs) | Number |
| Sleep average (last 7 days, hrs) | Number |
| RHR average (last 7 days, bpm) | Number |
| Subjective energy average (1–10) | Slider |
| Pull-up max reps (single set, clean) | Number |
| Pogo hop reps (bilateral, clean form) | Number |
| Ab vacuum hold (seconds) | Number |
| Training days completed this week | Number (0–6) |

### Block History Table
- Rows: weeks in the active block
- Columns: daily adherence summary, weekly baseline fields, readiness distribution, and benchmark results
- Deload/test weeks highlighted
- Phase boundaries marked

### Benchmark Test Results

Captured on phase test weeks:

| Metric | Test 1 | Test 2 | Test 3 | Block Review |
|--------|--------|--------|--------|--------------|
| Max clean pull-ups | | | | |
| Single-leg balance (s) | | | | |
| Pogo hops or ankle test | | | | |
| Block-specific strength test | | | | |
| Bodyweight / waist trend | | | | |
| Readiness trend | | | | |

### Phase / Block Review
- Shows system recommendation: Advance / Repeat / Deload / Pivot.
- Lists the objective reasons behind the recommendation.
- Allows coach/user override with a required reason.
- Writes the decision back into the annual roadmap and next-block draft.

### Progress Visualization
Simple text-based sparklines or ASCII bar charts — no charting library required.

Example:
```
Pull-ups over active block:
Test 1: ████░░░░░░ 5
Test 2: ███████░░░ 7
Test 3: ████████░░ 8
Review: ██████████ 10
```

---

## Screen Gaps — v4 → v5 Improvements

The following are explicitly absent from v4 and must be built in v5:

1. **Block intensity curve visualization** — A visual representation of training load across the active block. Currently you cannot "see" where the peaks and valleys are without reading every week individually.

2. **Phase transition checklist** — Concrete criteria for advancing Phase 1→2 and Phase 2→3. Currently implied but not stated. Users should not guess when to progress.

3. **Daily warm-up as a distinct, named block** — Currently buried inside the morning circuit section without explicit connection to today's session muscles. Must be pulled out as a dedicated screen block with day-specific content and a muscle primer callout.

4. **Daily rehab block as explicitly separate from warm-up** — These serve different purposes (prep vs. maintenance). Merging them obscures the intent of each. In v5 they are separate visual blocks with separate labels.

5. **Equipment substitution wizard** — A simple if-then lookup: "If [equipment X] is not available, substitute [exercise Y]." Currently notes are scattered in exercise descriptions.

6. **Dual-mode: Home vs. Hotel** — Not just a note in the travel row, but a full toggle that restructures the exercise table: swaps equipment tags, substitutes exercises, adjusts volume targets for reduced equipment.

7. **Progress photos / body comp tracking section** — Body composition milestone logging (optional). Not caliper or DEXA — just a structured way to note subjective observations at deload weeks.

8. **Supplement timing integrated into daily timeline** — Pre-workout stack, creatine, protein timing all shown in the daily schedule view, not just in the nutrition screen.

9. **Pre-session warm-up intensity visualization** — A simple muscle diagram or text callout showing: which muscles are primary today, which are secondary, which are being activated in warm-up. Bridges the warm-up block to the main session visually.
