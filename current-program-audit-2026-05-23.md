# Current Program Audit — 2026-05-23

## Scope

Audited:
- Source specs in `daily-practice.md`, `screens.md`, `exercises.md`, `program-config.md`, and `annual-roadmap.md`.
- Generated current app: `/Users/Veritas/Downloads/dustin_training_os_v5.html`.

Primary lens:
- Redundancy.
- Intra-day cohesion.
- Inter-day and weekly stress distribution.
- Warm-up vs. morning rehab/prehab separation.
- Phase/program rule consistency.

---

## High-Priority Findings

### 1. Saturday Duplicates Jefferson Curl In Warm-Up And Main Session

Severity: High  
Scope: intra-day / warm-up-main duplication

Evidence:
- Saturday immediate warm-up uses `Jefferson curl (bodyweight)` as the ramp exercise.
- Saturday main session uses `Jefferson Curl` for `4x5 @ 5s down`.
- Phase 3 Saturday morning rotation also adds `Jefferson curl (5lb DB)` before the warm-up and main session.

Why it matters:
- Jefferson curls are loaded or semi-loaded end-range spinal flexion. Repeating them as morning rotation, warm-up ramp, and main work turns a mobility session into repeated spinal-flexion exposure.
- The warm-up should prepare Jefferson curls, not redo them.

Recommended fix:
- Saturday warm-up should use the Jefferson curl activation sequence from `exercises.md`: supine knee-to-chest + seated forward fold, then one optional unloaded rehearsal only if the main set is not bodyweight.
- Keep Jefferson curls in the main session only.
- Remove Phase 3 Saturday morning Jefferson curl and replace it with decompression or low-intensity spinal segmentation.

---

### 2. Morning Rehab And Immediate Warm-Up Overlap Rules Are Inconsistent

Severity: High  
Scope: program-wide / generator rule conflict

Evidence:
- `daily-practice.md` says R1/R2 may overlap with immediate warm-up when useful.
- `screens.md` says the morning foundation may be shown as completed context and not repeated unless needed.
- The generated app repeats several drills instead of treating morning work as completed context.

Why it matters:
- The system has no hard duplicate guard. This allows the generator to copy useful drills into multiple blocks instead of deciding which block owns them.

Recommended fix:
- Add a generator rule: morning-to-warm-up overlap is forbidden by default.
- If overlap is intentional, the app must show a reason, reduce dose, or replace the warm-up drill.
- Add exact-name and synonym duplicate checks before app generation.

---

### 3. Ankle Stiffness Is Duplicated Inside The Same Day

Severity: High  
Scope: intra-day / weekly connective-tissue load

Evidence:
- Daily morning fixed work includes `Tibialis raise + single-leg calf raise`.
- The morning ankle block includes `Pogo hops`, `Tibialis raise`, and `Single-leg soleus raise`.
- Main sessions on Sunday, Monday, Wednesday, and Thursday also include an `Ankle Stiffness Block` with pogo/tibialis/soleus work.

Why it matters:
- Tibialis, calf, soleus, Achilles, and patellar-tendon loading appear in multiple blocks on the same day.
- The source spec says the morning ankle overlap is intentional, but the generated main-session ankle block adds a third exposure on several days.

Recommended fix:
- Choose one owner for ankle stiffness per day: morning ankle block or session warm-up/main block.
- If the morning ankle block is completed, the session should show it as completed context and omit duplicate tibialis/soleus volume.
- Keep pogo hops only on days where elastic ankle prep is actually needed.

---

## Medium-Priority Findings

### 4. Sunday Repeats Hip Flexor, Dead Bug, Tibialis, Soleus, And Goblet Squat Patterns

Severity: Medium  
Scope: intra-day

Evidence:
- Morning: hip flexor stretch, dead bug, tibialis/calf.
- Warm-up: hip flexor kneeling stretch, glute bridge, KB goblet squat ramp.
- Main: ankle block repeats tibialis/soleus/pogos; core block repeats dead bug; primary block contains a goblet squat complex.
- Night routine repeats passive hip flexor stretch and dead bug.

Why it matters:
- Some overlap is purposeful, but the day has too much repeated hip flexor, TVA, and lower-leg maintenance.
- Sunday is the hardest lower-body CNS day, so prep should be tight.

Recommended fix:
- Keep hip flexor in morning or warm-up, not both.
- Keep dead bug in morning or core accessory, not both unless the main-session version has a progression purpose.
- Move night dead bug to breath-led recovery only, or substitute crocodile breathing on heavy lower days.

---

### 5. Monday Push Has Exact Warm-Up/Main Duplicates

Severity: Medium  
Scope: intra-day

Evidence:
- Morning rotating work includes `Band pull-apart`.
- Immediate warm-up includes `Band pull-apart`.
- Immediate warm-up ramp is `Ring Push-Up`.
- Main session primary is `Ring Push-Up`, plus ring fly, slider chest fly, archer push-up, push press, decline ring push-up.

Why it matters:
- Band pull-apart can be useful, but repeating it blurs morning prehab and warm-up.
- Ring push-up as ramp plus main is acceptable only if shown explicitly as ramp sets, not as a separate warm-up exercise.

Recommended fix:
- If band pull-apart was done in morning, use scapular push-up or shoulder CAR as the warm-up neural drill.
- Display ring push-up ramp as `Ramp sets for Ring Push-Up`, not as a separate duplicated movement.

---

### 6. Wednesday Pull Has High Grip And Shoulder Accumulation

Severity: Medium  
Scope: intra-day / weekly

Evidence:
- Warm-up: dead hang, scapular pull-up, pull-up ramp.
- Main: pull-up, ring row, KB row.
- Accessory: towel hang and Y-T-W.

Why it matters:
- This is coherent for a pull day, but grip and shoulder depression/retraction volume is high.
- Towel hang after pull-ups, rows, and dead hangs may exceed useful grip volume when readiness is yellow.

Recommended fix:
- Keep dead hang or scapular pull-up, not both, on yellow days.
- Make towel hang a conditional accessory based on elbow/grip readiness.

---

### 7. Thursday Legs B Exceeds The Stated 60-Minute Cap

Severity: Medium  
Scope: session design / time cap

Evidence:
- `program-config.md` sets `session_time_cap_minutes: 60`.
- Thursday is listed as `60-65 min`.
- Thursday note says `65-min cap`.

Why it matters:
- This violates a core design rule: 60-minute hard cap, no exceptions.

Recommended fix:
- Set Thursday to 60 minutes.
- Make the upper isolation finisher optional or rotate two isolation movements per week instead of all four.

---

### 8. Friday Skill Warm-Up Is Duplicated As A Main Block

Severity: Medium  
Scope: intra-day / UI labeling

Evidence:
- Immediate warm-up includes `Neck CARs` and `Wrist + shoulder CARs`.
- Main session also starts with `Mandatory Warm-Up — 5 min` containing `Neck CARs` and `Wrist + shoulder CARs`.

Why it matters:
- This is likely a labeling/data modeling issue. The same warm-up exists in two places.

Recommended fix:
- Move the Friday mandatory warm-up fully into the immediate warm-up block.
- Main session should start at skill work.

---

## Low-Priority Findings

### 9. Night Recovery Repeats Dead Bug Daily

Severity: Low  
Scope: intra-day / program-wide

Evidence:
- Morning fixed work includes `Dead bug — exhale each rep`.
- Night routine includes `Dead bug — exhale-only`.

Why it matters:
- The night version is intentionally lower intensity, but it can look like a duplicate and may be unnecessary on days that already include core work.

Recommended fix:
- Rename night version to `Exhale-only supine reset`.
- Keep cues explicitly recovery-focused and remove training language.

---

### 10. Tuesday And Saturday Are Labeled Recovery But Can Become Full Sessions

Severity: Low to Medium  
Scope: weekly cohesion

Evidence:
- Tuesday: Zone 2 plus yoga/Pilates plus optional Tai Chi.
- Saturday: gymnastics mobility, recovery close, sleeves, and long walk; time listed as 55-65 minutes.

Why it matters:
- Recovery days are only recovery-biased if they stay low stress and time-bounded.

Recommended fix:
- Add recovery-day caps:
  - Tuesday: Zone 2 plus one practice only.
  - Saturday: gymnastics mobility or long walk/sleeves emphasis, not all expanded when readiness is low.

---

## Summary

The program has strong structure, but the current generated app needs duplicate guards. The biggest issues are not random exercise selection; they are ownership problems between morning rehab, ankle block, immediate warm-up, and main session.

Highest-impact fixes:
1. Remove Jefferson curl from Saturday warm-up and Phase 3 Saturday morning rotation.
2. Stop duplicating ankle stiffness across morning and main session.
3. Enforce the 60-minute cap on Thursday and Saturday.
4. Add a generator duplicate guard for exact names and known synonyms.
5. Treat warm-up ramp sets as part of the first main exercise, not a separate exercise duplicate.

