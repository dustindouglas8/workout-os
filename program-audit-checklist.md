# Program Audit Checklist

## Purpose

This checklist is the quality-control layer for Workout OS programming. Use it before generating a new HTML program, after changing a split, and whenever a daily session feels redundant, incoherent, too long, or mismatched to the current phase.

The audit is meant to catch:
- Duplicate exercises across morning rehab/prehab, immediate warm-up, main session, cooldown, and night recovery.
- Duplicate stress on the same tissue or joint inside a day.
- Poor recovery spacing across adjacent days.
- Weekly pattern imbalance.
- Phase drift, where old priorities stay in the program after they stop serving the current block.
- Warm-up and prehab blur, where low-load maintenance quietly becomes a second workout.

---

## 1. Intra-Day Cohesion

Audit every block on the same day: morning routine, ankle block, readiness-gated warm-up, main session, conditioning, recovery close, and night routine.

### Redundancy Checks

- Does the exact same exercise appear more than once in the same day?
- Does the same movement appear in both morning rehab/prehab and immediate warm-up?
- Does the same drill appear in warm-up and main session without a clear dose difference?
- Are similar joint actions repeated too often?
- Is the same tissue loaded in three or more separate blocks?
- Are prehab drills duplicated across morning routine, warm-up, cooldown, or night recovery?
- Are activation drills repeated after the target muscles are already warm?
- Are multiple exercises solving the same problem when one would be enough?

### Flow Checks

- Does the day move from general to specific?
- Does the warm-up prepare the actual main session?
- Are mobility drills placed before strength only when they improve the session?
- Are high-skill or high-load exercises placed before fatigue-heavy work?
- Are loaded end-range drills placed where they will not compromise the priority work?
- Is the recovery close actually recovery-focused?
- Does the total day respect the session time cap?

### Same-Day Stress Checks

Flag repeated or high-dose stress to:
- Lumbar spine
- Hamstrings
- Hip flexors
- Adductors
- Calves / Achilles
- Knees / patellar tendon
- Shoulders / rotator cuff
- Elbows
- Wrists
- Neck / upper traps

### Purpose Checks

For every exercise, answer:
- What is this doing?
- Is it preparation, training, correction, conditioning, recovery, or assessment?
- Does another block already accomplish this?
- Could this be removed without reducing the quality of the day?
- Is it here because it is needed for this day, or because it is generally useful?

---

## 2. Morning Rehab vs. Immediate Warm-Up

Morning rehab/prehab and immediate warm-up must be treated as separate programming objects.

### Morning Rehab/Prehab Rules

- Low effort only: 30-50% ceiling.
- One round only.
- Six exercises maximum unless the source spec explicitly changes.
- No failure, no pump work, no soreness target.
- Fixed work should remain general enough to use daily.
- Rotating work should address maintenance, not duplicate the session warm-up by default.

### Immediate Warm-Up Rules

- Directly prepares the main session.
- Contains only the minimum drills needed to improve session quality.
- Does not repeat completed morning work unless there is a documented reason.
- If overlap is intentional, the app must show the morning version as completed context and reduce or replace the warm-up dose.
- Loaded end-range work should not appear in both warm-up and main session unless warm-up dose is unloaded or explicitly ramped.

### Mandatory Duplicate Guard

No exercise should appear in both morning rehab/prehab and the workout warm-up on the same day unless it has a clearly different purpose, dose, intensity, and display note.

---

## 3. Inter-Day Cohesion

Audit how today affects tomorrow and how yesterday affects today.

### Recovery Spacing

- Does today interfere with tomorrow's priority session?
- Are eccentric-heavy movements placed before days that need the same tissue fresh?
- Are tendon-heavy drills spaced conservatively?
- Are high-impact or plyometric sessions separated from heavy lower-body work when needed?
- Do shoulders, elbows, wrists, knees, and low back get lower-stress days?

### Adjacent-Day Flags

Flag:
- Heavy hamstring eccentric work within 48 hours of another hamstring-dominant session.
- Loaded spinal flexion close to heavy hinging.
- Grip-intensive work before pull-up or ring-heavy sessions.
- Shoulder capsule end-range loading on consecutive days.
- Calf / Achilles plyometrics on too many consecutive days.
- Skill work that is actually conditioning added before a hard lower session.

---

## 4. Weekly Cohesion

Audit the seven-day plan as one unit.

### Pattern Balance

Track weekly exposure to:
- Squat
- Hinge
- Lunge / split squat
- Horizontal push
- Vertical push
- Horizontal pull
- Vertical pull
- Carry
- Rotation
- Anti-rotation
- Spinal flexion
- Spinal extension
- Lateral movement
- Sprint / jump / plyometric work
- Zone 2 / conditioning
- Skill practice
- Recovery / mobility

For each pattern, ask:
- Is it trained enough for the phase goal?
- Is it overrepresented?
- Is it always trained under fatigue?
- Is there enough repetition to improve without becoming stale?

### Weekly Volume and Intensity

- Are hard sets distributed logically?
- Are there too many moderate-hard days and no true easy days?
- Are the hardest sessions separated by lower-stress work?
- Are accessories crowding out primary work?
- Are small tissues receiving too much hidden volume?
- Are recovery days actually recoverable?

### Weekly Redundancy

- Are the same prehab drills repeated more often than intended?
- Are warm-ups copied across unrelated days?
- Are the same tissues hit in morning, warm-up, main session, and night routine several times per week?
- Are recurring drills progressed, reduced, or reassessed?

---

## 5. Phase Cohesion

Audit each 3-4 week phase against the current block goal.

### Phase Goal Alignment

- Does the phase have one primary training goal?
- Do warm-ups, accessories, conditioning, and mobility support that goal?
- Are secondary goals maintained without competing with the main goal?
- Are exercises selected for the current phase instead of carried forward by habit?
- Are outdated phase priorities removed?

### Progression Checks

- Is each main movement progressing by load, reps, sets, tempo, range, density, or skill quality?
- Are accessories progressed or intentionally held constant?
- Is conditioning progressed logically?
- Are mobility and prehab drills progressed, maintained, or exited based on criteria?
- Are deload and benchmark weeks placed where fatigue actually needs them?

### Fatigue Accumulation

- Does weekly stress rise intentionally?
- Are high-soreness movements introduced gradually?
- Are tendon-heavy drills progressed conservatively?
- Are new stressors limited so the phase can be interpreted?
- Is there a readiness-based recovery valve?

---

## 6. Program-Wide Data Checks

Every exercise should have structured tags.

### Required Tags

- Purpose: warm-up, mobility, activation, skill, strength, hypertrophy, power, conditioning, prehab, rehab, recovery, assessment.
- Pattern: squat, hinge, push, pull, carry, rotation, anti-rotation, lateral, locomotion, jump, sprint, isometric, flexion, extension.
- Tissue / joint stress: lumbar spine, thoracic spine, shoulder, elbow, wrist, hip, adductor, hamstring, quad, knee, calf, Achilles, foot / ankle, neck.
- Equipment: home, travel, bodyweight, hotel, unavailable.
- Phase: prep, strength, hypertrophy, conditioning, rehab, recovery, skill.

### Generator Rules

- Flag exact same exercise names inside the same day.
- Flag likely synonyms that represent the same drill.
- Flag same tissue stress appearing in three or more day blocks.
- Flag same exercise appearing in morning and immediate warm-up.
- Flag warm-up drills that are not connected to the main session.
- Flag main-session exercises missing from the exercise library.
- Flag exercise IDs missing from `exercise-media-map.md`.
- Flag generic provider links rendered as exercise media.
- Flag `related` or `close_variant` media rendered as exact demos.
- Flag exercises without clear progressions, regressions, or contraindications.
- Flag days exceeding time cap.

---

## 7. Warm-Up Audit

A warm-up passes only if it:
- Raises temperature or movement readiness.
- Opens ranges needed for that session.
- Activates muscles used in the first primary movement.
- Rehearses session-specific positions.
- Does not create fatigue.
- Does not duplicate completed morning work without an explicit reason.
- Does not include loaded end-range work unless clearly justified.
- Leads naturally into the first main exercise.
- Fits the session time cap.

### Loaded End-Range Guard

For Jefferson curls, skin the cat, German hang, deep Cossack, loaded shoulder extension, loaded pancake, Nordics, and heavy calf eccentrics:
- Is the tissue fresh enough today?
- Is this already present elsewhere today?
- Is the dose minimal enough for its role?
- Does it belong in warm-up, main work, or recovery?
- Is there a pain-based regression shown?

---

## 8. Prehab / Rehab Audit

- Is each drill tied to a known issue, risk, or performance need?
- Is dose appropriate?
- Is frequency defined?
- Is the drill duplicated elsewhere?
- Is there a progression?
- Is there an exit or maintenance criterion?
- Is pain response tracked?
- Is this still needed in the current phase?
- Is the label accurate: rehab, prehab, activation, mobility, or recovery?

### Exit Criteria Examples

- Remove when symptom-free for 2-4 weeks.
- Reduce to maintenance when strength or range symmetry improves.
- Replace when the drill no longer creates useful change.
- Keep at low dose only if it protects a known recurring issue.

---

## 9. Additional Checks

### Ankle Block Ownership

The tibialis raise, soleus raise, and Achilles loading appear in three potential locations: F4 (morning circuit), morning ankle block, and main session ankle stiffness block. Ownership must be resolved per day:

- Does F4 run before the ankle block, adding a fourth tibialis exposure on training days?
- Which block "owns" the tibialis/soleus volume for the day?
- In the morning routine, does the ankle block show tibialis/soleus as completed in F4 instead of repeating them?
- If tibialis/soleus are repeated after F4, is the day explicitly labeled ankle-priority rehab with a reduced supplemental dose?
- Is the main session ankle block showing morning work as completed context?
- Are pogo hops duplicated in morning ankle block and main session warm-up on the same day?
- Is the ankle stiffness progression level (Phase 1/2/3) consistent across blocks?

### Morning Circuit Rules Compliance

The 4 rules (daily-practice.md Section 8) must hold in every generated session:

- Is the circuit still at 6 exercises maximum? (F1–F4 + R1–R2, no additions)
- Is it still 1 round only?
- Are there rest intervals programmed between movements?
- Does any exercise appear at effort above 50%?

If Phase 3 adds loaded R1/R2 movements, check that none of the loaded exercises also appear in that day's main session (Phase 3 morning rotation guard).

### Night Recovery Checks

- Is each movement in the night routine genuinely decompression, breathing, or passive release?
- Does any night routine movement create fatigue, soreness, or mechanical load?
- Is Movement 4 (Exhale-Only Supine Reset) labeled as recovery, not as a dead bug or core exercise?
- On days with heavy core accessory work, has the supine reset been substituted with crocodile breathing?
- Does the night routine stay under 10 minutes?

### Ramp Sets vs. Exercise Duplication

- Are warm-up ramp sets of the first compound exercise labeled as ramp sets, not as a separate duplicate exercise?
- Does ring push-up (or any compound) appear in both the warm-up block and the main session without being labeled as ramp sets?
- Are ramp rows styled visually distinct from working sets so they are not confused with additional volume?

### Duration vs. Set Clarity

Every timed mobility, stretch, recovery, carry, hold, or conditioning prescription must make its unit unambiguous:

- If the prescription says `4 min`, does that mean one continuous 4-minute block, 4 minutes total, or 4 minutes per side?
- If the prescription says `3x60s`, does that mean 3 total holds, 3 holds per side, or 3 rounds of a sequence?
- If an exercise combines active and passive work, is the work/rest or active/passive split defined?
- Does every timed item have a `total time` field or an obviously calculable total?
- Does the sum of timed items fit the block label and session time cap?
- Are mobility "sets" labeled as `holds`, `rounds`, `cycles`, or `total time` when that would be clearer?

Generator-time rule: if a row uses minutes or seconds and also uses sets, sides, rounds, or mixed active/passive language, the generator must render the total time and unit definition. Example: `Pancake stretch — 3 holds x 60s total, alternate forward/side reaches`.

### Completed Context Rule

When morning circuit work overlaps with warm-up or main session work:

- Is the morning version shown as completed context, not silently repeated?
- Does the warm-up show what was already done and what is still pending?
- Does the main session ankle block acknowledge completed morning ankle work?

### Recovery Day Activity Cap

- Tuesday: Zone 2 plus one practice only (yoga/Pilates OR Tai Chi, not both).
- Saturday: gymnastics mobility OR long walk/compression sleeves, not all three when readiness is Yellow or Red.
- Is either recovery day exceeding 60 minutes?
- Is any exercise on a recovery day producing soreness the next day?

### GYR Modification Adequacy

- Does the Yellow modification actually reduce session load enough to justify training on a suboptimal day?
- Does the Red prescription provide a complete recovery alternative, not just a blank?
- Are loaded end-range movements (Jefferson curls, Nordics, skin the cat) automatically downgraded or removed on Yellow days?

---

## 10. When to Run Each Audit Tier

The audit has two tiers with different triggers and audiences.

### Tier 1 — Pre-Generation Audit (Human Review)

**When:** Before regenerating the HTML, after any source doc changes, and whenever a daily session feels wrong.

**What:** Full checklist — Sections 1–9. This is the programming design review. It catches intentional structural issues before they get baked into a generated file.

**Who runs it:** You (the programmer) against the source markdown files.

**Output:** Use the format in Section 12. Document findings before touching the HTML.

### Tier 2 — Generator-Time Audit (Automated Rules)

**When:** Every time the HTML is generated. These run automatically as part of the generation step, not as a manual review.

**What:** Mechanical duplicate guards only — Section 6 Generator Rules. These are binary checks that can be scripted:
- Exact exercise name appears twice in the same day → fail.
- Same exercise in morning circuit and warm-up → fail.
- Same tissue stressed in three or more blocks → warn.
- Main session ankle block not showing completed context when morning ankle block exists → fail.
- Day time exceeds session_time_cap_minutes → fail.
- Friday CARs circuit appears in both immediate warm-up and main session → fail.
- Timed mobility prescription is ambiguous or total time cannot be calculated → fail.

**Who runs it:** The generator script (or a pre-generation validation function).

**Relationship between tiers:** Tier 1 should catch programming design errors. Tier 2 is the final guard that catches anything that slipped through. If Tier 2 keeps catching the same error, the source docs have a structural problem that Tier 1 missed — fix the spec, not just the generated output.

---

## 11. Review Cadence

### Daily Audit

- Duplicate exercises.
- Morning/warm-up overlap.
- Warm-up matches session.
- High-risk tissue stress.
- Time cap.

### Weekly Audit

- Movement pattern balance.
- Tissue stress distribution.
- Recovery spacing.
- Conditioning placement.
- Prehab frequency.
- True easy days.

### Phase Audit

- Phase goal alignment.
- Progression clarity.
- Deload and benchmark placement.
- Exercise selection relevance.
- Removal of outdated priorities.

### Program Audit

- Exercise library completeness.
- Tag quality.
- Chronic gaps.
- Chronic overload zones.
- Redundancy trends.
- Generator rule failures.

---

## 12. Audit Output Format

Use this format when reporting findings:

```text
Finding:
Severity: High / Medium / Low
Scope: intra-day / inter-day / weekly / phase / program-wide
Evidence:
Why it matters:
Recommended fix:
```
