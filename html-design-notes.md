# HTML Design Notes

## Core Principle

The app is used in 2-minute intervals between sets in a gym, on a phone, with sweaty hands. Every screen decision should answer: **what does the athlete look at during their rest period?**

Not: what does a nice dashboard look like. Not: how do we display all the program data. Every screen should answer one question immediately without navigation. If it takes more than one tap to get to the next relevant thing during a session, the design is wrong.

Secondary principle: the app is a daily operating tool, not a reference document. The philosophy lives in the MD files. The app answers five questions only:

1. What do I do right now?
2. How hard should I push this week?
3. What do I skip if recovery is bad today?
4. How do I do this movement correctly?
5. Is the program working — should I advance or adjust?

---

## Mental Model: The App Lives Between Sets

Most fitness apps are designed to be read before training. This app is designed to be used *during* training. The difference changes every layout decision.

**Before-training UX** (what other apps optimize for): readable paragraphs, full exercise descriptions, program overviews. Good for the first time you see it.

**Between-sets UX** (what this app optimizes for): current set status, next set instruction, rest timer, one-tap log. Used 3–5 times per session, every session.

Design rule: anything the athlete needs between sets must be visible without scrolling from the current position. Anything they need before training can require a tap.

---

## Navigation Structure

### Mobile (primary)

Sticky bottom bar, always visible:

```
[ Today ] [ Log ] [ Exercises ] [ Roadmap ]
```

- **Today** — the daily flow screen. This is where the athlete lives.
- **Log** — session history, weekly check-in, benchmark results.
- **Exercises** — searchable exercise library.
- **Roadmap** — annual block map and phase gate reviews.

Today is the default screen on every open.

### Desktop (secondary)

Two-column layout:

```
[ Left: Today flow — full width scrollable ]   [ Right: sticky context panel ]
```

Right panel (sticky, never scrolls away):
- Block / Phase / Week in phase
- Readiness status (color-coded)
- Mode: Home / Hotel / Bodyweight
- Today's primary and support focus
- Time cap countdown (once session starts)
- Next test week date

The right panel answers "what's the context" so the left column can focus entirely on "what's the action."

---

## Today Screen

Opens to today's session summary. Never opens to a blank state.

**Header row (always visible, sticky on mobile):**

```
Thursday · Legs B + Isolation          Home ▾        60 min
Week 2 of Phase 1 · Moderate load · RIR 2–4
```

The RIR/RPE target line is the most important piece of information on the screen. It tells the athlete how hard to push on every set without thinking. Make it prominent — same size as the session title, not a footnote.

**Mode toggle** (Home / Hotel / Bodyweight) lives in the header. Changing it immediately swaps all exercise substitutions inline. No navigation to a separate travel tab.

**Session type badge:**
- On heavy days: `Primary: Legs Power` or `Primary: Heavy Push + Support Pull`
- On Zone 2 days: `Zone 2 + Yoga`
- On deload weeks: `Deload Week · RPE 4–5 · All sets stop at 6+ RIR`
- On test days: `Benchmark Test Day · Fresh · Log all 6 metrics`

**Start session button** launches the timer and locks the mode (Home/Hotel). Once started, the daily flow sections become active.

---

## Session Pacing Model

Every session has a time budget broken across blocks. Show it above the main session:

```
Ankle block      4 min  ████
Warm-up          5 min  █████
Primary          28 min ████████████████████████████
Accessory        18 min ██████████████████
Log              2 min  ██
Total            57 min
```

This is a bar chart or compact row. It updates in real time once the session starts — greying out completed blocks. If the athlete is behind pace, the remaining blocks compress visually with a "⚠ 8 min behind" indicator.

The purpose: athletes consistently underestimate rest time. Making the time budget visible prevents the 70-minute "60-minute session."

---

## Daily Flow Sections

The day is divided into six sections. Sections do **not** auto-collapse after completion. Completed sections are visually muted (reduced opacity, green checkmark, title struck through) but remain scrollable. The athlete may need to re-read a cue mid-session. Hiding completed work creates friction.

The only exception: completed sections collapse on deliberate long-press to clean up if the athlete wants.

### Section 1: Morning Rehab / Prehab

This is the daily practice that runs before training and is independent of readiness status. It never changes based on GYR — it runs on rest days, deload weeks, and travel days equally.

Display: a compact vertical checklist.

```
Morning Rehab / Prehab                              [ 14 min ]

□  Nasal breathing — 2 min
□  Ab vacuum — 3 × hold progression
□  F1 Band external rotation — 12/side
□  F2 Hip flexor stretch + posterior tilt — 30s/side
□  F3 Dead bug — 8/side (exhale each rep)
□  F4 Tibialis raise + calf raise — 15 + 10/side
□  R1 [rotating movement for today] — [reps]
□  R2 [rotating movement for today] — [reps]

Ankle stiffness block ──────────────────────────────
□  Pogo hop — 15 reps (or single-leg balance 30s/side — rest days)
□  Tibialis raise — 20 reps
□  Single-leg soleus raise — 10/side
```

Each item is a tap-to-check checkbox. No expansion needed — these are done from memory by Phase 2.

R1 and R2 are populated from the rotating movement table in `daily-practice.md` based on today's day and current phase.

The ankle stiffness block renders as a sub-section inside Morning Rehab, separated by a line. It is always last in the morning sequence, before matcha.

The app should infer morning day and phase from the active program state. Do not show normal-use selectors for Morning Rehab phase or day. Display read-only context instead:

```
Saturday · Phase 1 · 14 min
```

Manual overrides belong behind an `Advanced override` control. The default flow should be checkboxes only.

### Section 2: Training Readiness Check

A pre-session gate. Cannot be skipped. Runs after morning rehab, before the immediate warm-up.

Five inputs, each on its own row with a simple slider or tap:

```
Training Readiness Check

Sleep last night        [ < 6h ] [ 6–7h ] [ 7+ h ]
RHR vs baseline         [ +5 bpm ] [ +2–4 ] [ Normal ]
Joint feel (1–5)        ● ● ● ○ ○
Energy (1–10)           [ slider ]
Motivation (1–10)       [ slider ]

                        [ Check readiness ]
```

Output banner, full-width, color-coded:

```
🟢 GREEN — Full session. Execute as written.
```
or
```
🟡 YELLOW — Accessories hidden. Top sets reduced by 1. No PRs today.
```
or
```
🔴 RED — Main session replaced. Recovery protocol only.
```

After the check, the main session section rewrites itself immediately. The athlete does not need to remember what Yellow means when they get to the exercise table — they see only what they should actually do.

Until readiness is completed, the main session stays locked and displays only:

```
Complete readiness check to load today's session.
```

Do not render the full session with an assumed Green state before the readiness gate is complete.

### Section 3: Immediate Warm-Up

Day-specific. Exercise-specific. This is not the morning circuit — it is the final bridge to working sets.

**Activation sequence block** (pulled from `exercises.md` for today's first primary exercise):

```
Immediate Warm-Up — Legs B · 5 min

Before KB goblet squat and Bulgarian split squat:

Mobility unlock:  Hip flexor kneeling stretch — 60s/side
                  Opens the range you're about to load.

Neural prime:     Glute bridge — 10 reps, 2s hold at top
                  Fires the glutes before they're loaded.

Ramp set 1:       KB goblet squat — 5 reps @ 50% weight
                  (not logged · pattern feel only)

Ramp set 2:       KB goblet squat — 3 reps @ 75% weight
                  (not logged · stop 6+ RIR)
```

The activation sequence and ramp sets are pulled from the first primary exercise of today's session. They appear here, not buried in the exercise drawer. The athlete does not need to open any exercise card to complete the warm-up.

Ramp set rows are visually distinct — grey background, no set counter, labeled "not logged."

After completing the warm-up section, the main session becomes active.

If the morning session already handled part of the warm-up need, the warm-up renders completed context instead of repeating the exercise:

```
Already handled this morning:
✓ Hip flexor reset
✓ Tibialis / soleus maintenance

Do now:
□ Glute bridge — 10 reps
□ Ramp: Goblet squat — 5 reps @ 50%
```

Ramp sets are attached visually to the first main exercise pattern and labeled as ramp work, not as duplicate exercises.

Ramp rows must be expandable cue cards, not plain text. Each ramp set needs:

- Purpose: rehearse the first working-set path without fatigue.
- Exact dose: reps, load/effort target, and RIR ceiling.
- Setup cue for the main pattern.
- Execution cue for what the user should feel or check.
- Failure/adjustment rule: what to do if the ramp feels unstable, painful, or too hard.
- Media action resolved through `exercise-media-map.md`, using the same exact/close-variant/media-pending rules as working sets.

Ramp sets are not logged as working volume. The UI must state this because otherwise users treat ramp work as extra sets.

Timed mobility prescriptions must be explicit. Do not display ambiguous rows like `Pike stretch — 4 min` or `Pancake stretch — 3x60s` without defining the unit and total time. Use `total`, `holds`, `rounds`, or `cycles`.

Example:

```
Pike active/passive sequence — 4 min total
Cycle: 20s active leg lift attempts + 40s passive fold x 4 rounds

Pancake stretch — 3 min total
3 holds x 60s total: center, left bias, right bias
```

If the prescription uses sides or rounds, show the calculated total time in the row.

### Section 4: Main Session

The intensity wave banner appears at the top of this section, sticky while scrolling through the exercise table:

```
Week 2 of Phase 1 · Moderate load · RIR 2–4 · RPE 7–8
```

On deload weeks:
```
Deload Week · Stop every set with 6+ reps in reserve
```

For explosive or skill exercises:
```
Quality 2 — Expression · Pattern is solid. Push precision within form.
```

**Exercise card — compact (default view):**

```
┌─────────────────────────────────────────────────────┐
│  KB Goblet Squat                     [  Primary  ]  │
│  4 × 10    4-2-1-0    Vest Phase 2+                 │
│                                                      │
│  Set 1  ○   Set 2  ○   Set 3  ○   Set 4  ○          │
│  [ Start rest timer ]                                │
└─────────────────────────────────────────────────────┘
```

- `[Primary]`, `[Support]`, `[Accessory]`, `[Drop if Yellow]` badges on every card — never ambiguous about priority
- Set circles: empty → tap to log → filled with checkmark
- `[ Start rest timer ]` button appears after any set is tapped. This is the most-used element in the whole app
- No RPE shown on the card by default. The wave banner above the table covers that globally

**Set logging — inline, one tap:**

Tapping a set circle opens a minimal inline log (does not navigate away):

```
Set 2 complete
Reps:   [ 10 ] ±
Load:   [ 50lb ] ±
RPE:    ● ● ● ● ● ● ● ○ ○ ○  (tap to rate)
[ Save ]
```

Reps and load default to the programmed values. The athlete only taps Save or adjusts if different. This takes 5 seconds, not 30.

**Rest timer:**

After tapping Save on a set, the rest timer starts automatically:

```
Rest
  1:45
[ Skip ] [ +30s ]
```

The default rest timer is a persistent bottom dock / mini-player, not a full-screen overlay. It stays visible while the athlete scrolls, checks cues, or previews the next exercise. On mobile it sits above the bottom nav. On desktop it sits in the sticky context area or bottom-right.

Default dock:

```
Rest · Ring Push-Up · Next: Set 2        1:23     [-15] [+30] [Skip]
```

An expanded timer view may exist, but the normal rest state must not block page scrolling.

Prescribed rest time is pulled from the phase and exercise data. Short rest for conditioning days, 90s for hypertrophy, 2–3 min for strength.

**Set log carry-forward:**

Set logging must optimize for repeated sets with the same load. Set 2 defaults to Set 1's saved load. Set 3 defaults to Set 2's saved load, falling back to Set 1. If no previous set exists, use the programmed load when available; otherwise use `BW`. The athlete should only tap `+` or `-` when the load changes.

For Set 2+, show previous set context:

```
Previous: 10 reps · 50 lb · RPE 7
```

Add a `Same as last set` shortcut where useful. RPE should not auto-fill by default because it is an observation, but it may remain one tap away.

**Exercise card — expanded (tap the card title):**

Opens a detail drawer from the bottom (mobile) or right side (desktop):

```
KB Goblet Squat

Muscles:  Quads, glutes, adductors (primary)
          Hamstrings, core (secondary)

Setup:    KB held vertically at chest, elbows pointing down.
          Feet shoulder-width, toes out 10–30°.

Execution: Squat deep, push knees out. Elbows track
           inside knees at bottom. Tall chest throughout.

Breathing: Inhale down, exhale at top.

Common mistakes:
  ✗ Heels rising — needs ankle mobility work
  ✗ Chest caving forward
  ✗ Not reaching full depth

Regression:  Bodyweight squat with pause
Progression: Add vest (Ph2+) → 1.5-rep at bottom (Ph3)

Travel sub:  Dumbbell goblet squat

Media:       [ Media pending ]
```

External media links come from `exercise-media-map.md`, not generic provider links. If the mapped source is exact and reviewed, show one primary action such as `Watch demo`. If the source is a close variant, label it as `Close variant`. If no exact reviewed source exists, show `Media pending` and the local cues from `exercises.md`.

Active workout cards should not send the user to a provider homepage or search page. Those links belong in source research, not in the workout flow.

The drawer stays open until the athlete dismisses it. They can read the cue, close the drawer, execute the set, and re-open if needed. No navigation.

**Block structure within the main session:**

```
── Ankle Stiffness Block ──────────────  4 min  (always first, runs even on Yellow/Red)
── Primary Compound Block ─────────────  25–30 min
── Accessory / Isolation Block ────────  15–20 min  (hidden on Yellow, skipped on Red)
```

On Yellow: the accessory block is hidden entirely with a visible callout: `"Accessories hidden — Yellow day. Add them back only if you feel better mid-session."`

On Red: the entire main session is replaced by:

```
🔴 Recovery Session

Today is a Red day. Main training is replaced.

□  Morning circuit (already done)
□  15 min Zone 1 walk — nasal breathing only
□  10 min passive mobility — hips and thoracic
□  Pneumatic sleeves if available

No compounds. No RPE. This is not optional rest — it is active recovery.
```

**GYR auto-modification is the page, not instructions on the page.** The athlete should never see a Yellow day and have to decide what to skip. The app has already made that decision.

**Home / Hotel / Bodyweight mode:**

Mode toggle is in the header (sticky). When switched:
- Home-only exercises swap to their travel substitutions inline in the card
- Equipment badges update
- An orange `TRAVEL MODE` banner appears above the exercise table

The swap happens in the card row itself — the athlete never navigates to a substitution list.

### Section 5: Post-Session Log

Appears after the last working set. Brief — completes in under 60 seconds.

```
Session complete

How did it go?
  ○ Full session     ○ Modified     ○ Skipped

Session RPE:    [ 1 ──────●──── 10 ]  7

Any pain?       [ 0 ──────────── 10 ]  0
Location:       [                    ]  (only if pain > 0)

Notes:          [                    ]  optional

[ Save and close ]
```

Inline per-set logs (collected during the session) are already saved. This form captures the session-level summary only.

On Sunday of a deload week, an additional prompt appears:
`[ Log benchmark results → ]` — links to the benchmark entry form.

### Section 6: Night Recovery

A guided sequence, not a reading list. Appears at the bottom of the Today screen and as a standalone state when opened at night.

```
Night Recovery                                  7 min

[ Begin guided sequence ]

  Or check off manually:

□  Physiological sigh — 3 reps
□  Passive hip flexor stretch — 40s / side
□  Supine thoracic release — 2 min
□  Dead bug (exhale-led) — 6 / side
□  Supine twist — 30s / side
□  Crocodile breathing — 2 min
□  4-7-8 breath — 4 cycles
```

`[ Begin guided sequence ]` starts a timed flow: each movement is displayed full-screen with its cue and a countdown. Auto-advances to the next. The athlete does nothing except breathe.

Manual checklist mode for athletes who already know the sequence and want to move faster.

---

## Phase Gate / Test Week Mode

During test weeks (Week 4, 8, 12, 16), the app shifts from **train mode** to **review mode**. The Today screen header changes:

```
Deload + Benchmark Week                           Week 4
[ 📊 Review mode active ]
```

The Phase Gate screen (accessible from Roadmap tab):

```
Phase 1 Review

Benchmarks ─────────────────────────────────────────
  Pull-ups (clean)           Start: 6    Now: 8    ↑
  Ring push-up max           Start: 12   Now: 15   ↑
  Zone 2 nasal pace          Start: —    Now: 4.2 mph ●
  KB swing density / 10 min  Start: —    Now: 88   ●
  Suitcase carry duration    Start: —    Now: 52s  ●
  Resting HR                 Start: —    Now: 58   ●

Recovery ────────────────────────────────────────────
  Yellow days this phase:    3 / 15 sessions     ✓
  Red days:                  0                   ✓
  Average sleep:             7.2 hrs             ✓
  Pain trend:                Stable              ✓

Adherence ───────────────────────────────────────────
  Sessions completed:        13 / 15  (87%)      ✓

Recommendation ──────────────────────────────────────
  ✅ ADVANCE to Phase 2

  Reason: Benchmarks improving, recovery stable,
  adherence above 80%, no pain flags.

  [ Advance ] [ Repeat ] [ Deload ] [ Pivot ]

  Override reason: [                              ]
                   (required if not following recommendation)
```

Recommendation is computed, not shown as a static label. The system calculates from the actual logged data. If it says Advance, the athlete taps Advance. If they disagree, they type a reason and override.

---

## Exercise Library

Tab: `Exercises`

```
Search: [                    ]

Filter:  [ All ] [ Push ] [ Pull ] [ Squat ] [ Hinge ]
         [ Carry ] [ Core ] [ Mobility ] [ Rehab ]
         [ Skill ] [ Warmup ]
```

Filters match the pattern tags in `exercises.md` exactly. No invented categories (no "Ball", no "Stability").

Each exercise opens the same detail drawer used in workout cards. Same cues, same media state, same substitution table. One source, two surfaces.

Exercises with `media.status = approved` show a thumbnail in the library list. Exercises with `missing` or `needs_review` show a grey placeholder.

---

## Visual Design

**The palette serves function, not aesthetics:**

- Dark background — reduces glare in bright gym environments
- High contrast text — minimum 4.5:1, targeting 7:1 for body text
- Four semantic colors only:
  - Green: complete, Green readiness, positive trend
  - Amber: Yellow readiness, time warnings, caution flags
  - Red: Red readiness, pain flags, skipped sessions
  - Blue / Purple: neutral interactive elements, phase indicators
- White / grey for everything else

**Typography:**
- Session titles and intensity badge: large, bold — 20px minimum on mobile
- Exercise names: medium, bold — 16px minimum
- Sets × reps, tempo: medium — 15px minimum
- Notes and cues: smaller — 13px minimum, but expandable
- No text below 13px on mobile under any circumstance

**Touch targets:**
- All tappable elements: minimum 44×44pt
- Set circles: 48×48pt
- Rest timer dismiss: large — center of screen
- Bottom nav tabs: full width divided by 4

**What the design does not include:**
- Hero images or motivational banners
- Animated transitions that take more than 150ms
- Any element that requires two-handed interaction
- Splash screens or loading states (single HTML file — opens instantly)
- Onboarding modals that appear every session

---

## Data Persistence

All data stored in `localStorage`. Key namespaces:

```
workout-os:config          → program config (user, goals, split, phase)
workout-os:today           → today's session state (readiness, set logs, completion)
workout-os:history         → session log (last 90 days)
workout-os:benchmarks      → phase benchmark results
workout-os:weekly          → weekly check-in log
```

On every open: load config, determine today's session, render Today screen. No server, no login, no sync.

**Export / backup:** A single `[ Export data ]` button in settings writes the full `localStorage` state to a JSON file. Import restores it. This is the travel backup — email the file to yourself before a long trip.

**Offline:** The entire app is one self-contained HTML file. No network requests. Works on airplane mode. This is a hard requirement — the athlete may be in a basement gym with no signal.

---

## What This App Is Not

These patterns are explicitly excluded:

- **Not a social app.** No sharing, no leaderboards, no community features.
- **Not a content library.** Philosophy and methodology live in the MD files. The app does not display long explanatory text during a session.
- **Not a calculator.** The program config pre-computes everything. The athlete never manually calculates percentages, volumes, or progressions.
- **Not a motivational tool.** No streaks, badges, or celebration animations. The program working is its own reward.
- **Not multi-user in the MVP.** One config per file. Multiple users = multiple generated HTML files.
