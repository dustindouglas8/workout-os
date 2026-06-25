# HTML Usability Audit — 2026-05-23

## Scope

Audited current generated app:
- `/Users/Veritas/Downloads/dustin_training_os_v5.html`

Purpose:
- Capture usability issues before the next rebuild.
- Focus on actual workout use: sweaty hands, between-set decisions, minimal taps, no confusion about what to do next.

---

## Highest-Priority Rebuild Requirements

### 1. Rest Timer Should Be A Bottom Dock, Not A Full-Screen Overlay

Severity: High  
Current behavior:
- Saving a set starts a full-screen rest overlay.
- The overlay blocks scrolling, checking cues, logging the next set early, or reviewing upcoming exercises.

Why it matters:
- During rest, the user often wants to scroll, check the next movement, review a cue, or adjust a previous log.
- The timer is important, but it should not trap the user.

Rebuild requirement:
- Rest timer becomes a persistent bottom dock / mini-player.
- It stays visible while the page scrolls.
- It shows exercise name, next set, countdown, Skip, +30s, and collapse/expand.
- On mobile, it sits above the bottom nav.
- On desktop, it can sit bottom-right or in the sticky context panel.
- When expanded, it can show larger countdown, but default state should not block the page.

Suggested dock:

```text
Rest · Ring Push-Up · Next: Set 2        1:23     [-15] [+30] [Skip]
```

---

### 2. Set 1 Load Should Carry Forward To Later Sets

Severity: High  
Current behavior:
- Opening any set defaults load to `BW` unless that exact set was already saved.
- If Set 1 is logged at `50`, Set 2 still opens as `BW`.

Why it matters:
- This creates repeated typing during the most-used workflow.
- Most exercises use the same load across all sets, with small adjustments only when needed.

Rebuild requirement:
- For each exercise, Set 2 defaults to Set 1's saved load.
- Set 3 defaults to Set 2's saved load, falling back to Set 1.
- If no previous set exists, use programmed load when available; otherwise use `BW`.
- Reps should default to programmed reps, but if the previous set was lower because of fatigue, the next set can default to previous reps with a small "programmed target" hint.

Suggested behavior:
- Set 1: `Load: 50`
- Set 2 opens with `Load: 50`
- User taps `+5` or `-5` only if changing.

---

### 3. Morning Rehab Should Not Ask The User To Choose Phase Or Day

Severity: High  
Current behavior:
- Morning Rehab has its own `Phase 1 / Phase 2 / Phase 3` selector.
- Morning Rehab also has its own day selector.
- The app already has a global selected day and global program phase.

Why it matters:
- This makes the user wonder whether morning rehab is separate from the program.
- It creates opportunities for mismatch: Saturday workout with Wednesday morning rehab, or Phase 2 session with Phase 1 morning work.

Rebuild requirement:
- Morning Rehab phase and day are inferred from `CFG.phase` and `CFG.selectedDay`.
- Display them as read-only context:

```text
Morning Rehab / Prehab
Saturday · Phase 1 · 14 min
```

- If override is needed, put it behind `Advanced override`, not inline.
- Remove the visible morning phase/day selectors from normal use.

---

### 4. Warm-Up Organization Needs A "Completed Context" Layer

Severity: High  
Current behavior:
- Morning Rehab, Immediate Warm-Up, and Main Session appear as separate blocks, but overlaps are not explained in the generated UI.
- Warm-up can feel like "more prehab" instead of "do this immediately before the first work set."

Why it matters:
- The user needs to know what was already handled and what still needs to be done.

Rebuild requirement:
- Warm-up should have two visual sub-blocks:
  - `Already handled this morning`
  - `Do now before working sets`
- If morning work covers a warm-up need, show it as completed context instead of repeating it.
- Ramp sets should be visually attached to the first main exercise, not floating as another warm-up item.

Suggested structure:

```text
Immediate Warm-Up — Do Now

Already handled this morning:
✓ Hip flexor reset
✓ Tibialis / soleus maintenance

Do now:
□ Glute bridge — 10 reps
□ Ramp: Goblet squat — 5 reps @ 50%
□ Ramp: Goblet squat — 3 reps @ 75%
```

---

### 5. Main Session Should Stay Gated Until Readiness Is Complete

Severity: High  
Current behavior:
- The main session renders with `green` as the default if readiness has not been checked.

Why it matters:
- The app says readiness is required, but the UI still shows the full session before readiness is done.
- This makes the readiness gate advisory instead of operational.

Rebuild requirement:
- Before readiness is completed, the Main Session section shows a locked placeholder:

```text
Complete readiness check to load today's session.
```

- After readiness:
  - Green renders full session.
  - Yellow renders reduced session.
  - Red renders recovery replacement.

---

## State / Logic Bugs

### 6. Morning Day Selector Can Render The Wrong Active Day

Severity: Medium  
Evidence:
- `selectDay()` calls `renderMornDays()` before `STATE.mornDay = dayIndex`.

Why it matters:
- Even though rotating moves update after the state change, the visible day selector can show the previous day as active.

Rebuild requirement:
- Update state first, then render.
- Better: remove the morning day selector entirely from normal UI.

---

### 7. Global Phase Change Does Not Sync Morning Phase

Severity: Medium  
Evidence:
- `settingsSet('phase', value)` updates `CFG.phase`, but does not update `STATE.mornPhase`.

Why it matters:
- The app can show Phase 2 main work while Morning Rehab remains on Phase 1.

Rebuild requirement:
- Morning phase should derive from `CFG.phase - 1`.
- If there is a rare manual override, show an override badge and a reset-to-program button.

---

### 8. Settings Are Too Close To Daily Training Controls

Severity: Medium  
Current behavior:
- Phase, week-in-phase, split, and protocol can be changed from Settings during normal use.
- Protocol also has a prominent daily toggle in the sticky header.

Why it matters:
- Phase and week are not daily choices. They are program state.
- Split is not a between-set decision.
- Protocol selection is powerful enough to change the workout stimulus; it should not look like a casual mode toggle.

Rebuild requirement:
- Keep Home / Hotel / Bodyweight in the session header.
- Move Phase, Week, Split, and Protocol to `Program Settings / Advanced`.
- If protocol variants remain available, expose them as `Today's variant` with clear warning and default to Standard.

---

## Set Logging / Training Flow

### 9. Rest Timer Should Start From The Saved Set And Know The Next Set

Severity: Medium  
Current behavior:
- Save set starts rest timer, but the timer does not display next set context.

Rebuild requirement:
- Timer dock should show:
  - Current exercise.
  - Completed set.
  - Next set number.
  - Prescribed rest.
  - Quick buttons: `-15`, `+30`, `Skip`.

---

### 10. The Rest Button Is Redundant Once Auto-Rest Exists

Severity: Medium  
Current behavior:
- Every exercise card has a `Rest timer` button even though saving a set auto-starts rest.

Why it matters:
- Adds visual clutter to every exercise card.

Rebuild requirement:
- Hide manual rest button by default.
- Show `Start rest` only in a small overflow action or when a set has been saved but no timer is running.

---

### 11. Set Logging Should Support Fast Repeat

Severity: Medium  
Current behavior:
- User opens set, adjusts reps/load/RPE, saves, then repeats from scratch.

Rebuild requirement:
- Add `Save + start rest` as the primary button.
- Add `Same as last set` one-tap option for Set 2+.
- Carry forward load automatically.
- Consider carrying forward RPE as blank, not previous, because RPE is an observation.
- Show previous set summary beside the current form:

```text
Previous: 10 reps · 50 lb · RPE 7
```

---

### 12. Numeric Load Controls Need Exercise-Specific Step Sizes

Severity: Low / Medium  
Current behavior:
- Load +/- always changes by 5.

Why it matters:
- Bodyweight, bands, dumbbells, kettlebells, vest, and time-based work need different controls.

Rebuild requirement:
- Use input type by exercise:
  - Bodyweight: `BW`, `BW + vest`, or assisted.
  - Dumbbell / KB: +/- 5 or available increments.
  - Band: light / medium / heavy.
  - Holds: seconds.
  - Distance/carry: steps or seconds.

---

## Section Organization

### 13. Timed Mobility Prescriptions Are Ambiguous

Severity: High  
Current behavior:
- Saturday `Pike stretch (active + passive)` is prescribed as `4 min`.
- Saturday `Pancake stretch` is prescribed as `3x60s`.
- The block label says `Gymnastics Mobility — 30 min`, but the user cannot tell whether these are total durations, per-side durations, rounds, or sets.

Why it matters:
- A timed stretch is not the same thing as a lifting set.
- If `Pancake stretch 3x60s` means 3 total holds, it is 3 minutes. If it means 3 per side or 3 rounds of forward/left/right, it can become 9 minutes.
- The user cannot pace the 30-minute block without knowing the unit.

Rebuild requirement:
- Timed mobility rows must define unit and total time explicitly.
- Replace ambiguous `sets` language with `holds`, `rounds`, `cycles`, or `total`.
- The UI should show the total time contribution for each timed mobility item.

Suggested Saturday rewrite:

```text
Pike active/passive sequence — 4 min total
Cycle: 20s active leg lift attempts + 40s passive fold x 4 rounds

Pancake stretch — 3 min total
3 holds x 60s total: center, left bias, right bias
```

Or, if the intent is longer:

```text
Pancake stretch — 6 min total
3 rounds: 60s center + 30s left + 30s right
```

Generator rule:
- If a row contains `min`, `s`, `x`, `/side`, `active + passive`, or `rounds`, the generated row must include `total time`.

---

### 14. Morning Rehab Is Too Long For A Daily Checklist Surface

Severity: Medium  
Current behavior:
- Morning section includes breathing, vacuum, phase selector, F1-F4, day selector, R1/R2, ankle block, and a completion button.

Why it matters:
- This makes a daily routine feel like a configuration screen.

Rebuild requirement:
- Default view should be compact and read-only except checkboxes.
- Advanced details should live behind `Cues`.
- No selectors in the default flow.

---

### 15. Completed Sections Become Too Dim

Severity: Low / Medium  
Current behavior:
- Completed sections get opacity `.5` on content.

Why it matters:
- The user may need to reread a cue later.
- Dimmed text can be hard to read in the gym.

Rebuild requirement:
- Keep completed content readable.
- Use a green check, subtle border, or collapsed optional summary instead of dimming all content.

---

### 16. Section Completion Buttons Add Extra Work

Severity: Low / Medium  
Current behavior:
- Morning, warm-up, main session, and session log all use explicit `Mark complete` buttons.

Why it matters:
- If all child items are checked, the section can infer completion.
- Extra completion buttons feel like admin work.

Rebuild requirement:
- Auto-complete checklist sections when all required items are checked.
- Keep manual override in an overflow menu.

---

### 17. Warm-Up Cue Cards Are Useful But Too Reference-Heavy

Severity: Low  
Current behavior:
- Warm-up cards include cue drawers and external MuscleWiki links.

Why it matters:
- During the workout, the user needs a quick cue, not a reference rabbit hole.

Rebuild requirement:
- Default warm-up card shows one-line execution cue.
- Drawer contains fuller detail.
- External links should live in Exercise Library, not the active warm-up flow.

---

## Navigation / Header

### 18. Sticky Header Has Too Many Controls

Severity: Medium  
Current behavior:
- Header includes Home/Hotel/BW, Travel week, Print, time, protocol buttons, session clock, start/end, and protocol guidance.

Why it matters:
- The header is the most valuable persistent surface. It should answer what to do now, not expose all configuration.

Rebuild requirement:
- Header keeps:
  - Day/session title.
  - RIR/RPE target.
  - Home/Hotel/BW.
  - Session clock.
- Move Travel week, Print, Protocol guide, and advanced settings out of the primary header.

---

### 19. Day Picker And Morning Day Selector Duplicate Each Other

Severity: Medium  
Current behavior:
- The Today screen has a day picker.
- Morning Rehab has a separate day selector.

Rebuild requirement:
- One selected day controls the whole page.
- Morning Rehab follows selected day automatically.

---

### 20. Pacing Warnings Are Useful But Not Actionable Enough

Severity: Low / Medium  
Current behavior:
- At 50 minutes: "consider skipping accessory block if not started."
- At 58 minutes: "finish this set and log."

Rebuild requirement:
- Add one-tap action from the warning:
  - `Hide remaining accessories`
  - `Jump to session log`
  - `Extend session by 10 min`

---

## Logging / Review

### 21. Session Log Duplicates Data Already Captured

Severity: Low  
Current behavior:
- Per-set logs save automatically, then the session log asks for summary inputs.

Rebuild requirement:
- Session Log should be short:
  - Completion status.
  - Session RPE.
  - Pain.
  - Notes.
- Pre-fill completion as `Full session` if all required primary/support sets were logged.

---

### 22. Weekly Check-In Is Always Prominent On Log Page

Severity: Low  
Current behavior:
- Weekly check-in is the first thing on the Log page, even when not Sunday.

Rebuild requirement:
- On non-check-in days, collapse it behind a small row.
- Put session history or today's saved session first immediately after training.

---

## Recommended Rebuild Order

1. Replace full-screen rest overlay with bottom rest dock.
2. Implement set load carry-forward and `Same as last set`.
3. Remove visible morning phase/day selectors; infer from program state.
4. Gate main session behind readiness completion.
5. Add completed-context rendering for morning/warm-up/main overlaps.
6. Simplify sticky header to session-critical controls.
7. Make timed mobility prescriptions explicit with total time and unit definitions.
8. Fix state sync bugs for selected day and phase.
9. Make section completion automatic where possible.
10. Make pacing warnings actionable.
11. Move reference links out of active workout flow.
