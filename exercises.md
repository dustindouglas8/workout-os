# Exercise Library

## Purpose

This is the canonical source for exercise selection, substitutions, cues, and media references. Workout tables should reference exercise IDs from this library instead of redefining exercise details inline.

## Media Policy

- Media is referenced, not embedded, so generated HTML stays light.
- Media source resolution lives in `exercise-media-map.md`. `exercises.md` owns local cues; `exercise-media-map.md` owns external source URLs, source status, match quality, and provider notes.
- Every exercise must have a media object, even if media is missing.
- External media is allowed for draft/reference mode and must be marked `needs_review`.
- Final approved media should be locally owned, explicitly approved, or otherwise safe to distribute.
- If media is missing, generated HTML shows cues and a "media pending" state.
- The generated HTML must never render a generic provider homepage or search page as an exercise demo. If an exact mapped URL does not exist, show `Media pending`.

Media statuses:

| Status | Meaning |
|---|---|
| missing | No useful media has been attached yet. |
| needs_review | External or draft media exists but has not been approved. |
| approved | Media is safe to use in generated output. |

## Movement Pattern Tags

Use these tags consistently:

- squat
- hinge
- push
- pull
- carry
- core
- mobility
- rehab
- conditioning
- skill
- warmup
- recovery

## Exercise Record Schema

Every exercise record in this library contains the following fields:

- **ID** — unique snake_case identifier
- **Pattern tags** — one or more movement pattern tags from the list above
- **Phases** — which training phases this exercise fits (prep, strength, hypertrophy, conditioning, rehab, recovery, skill)
- **Muscles** — primary and secondary muscles
- **Equipment** — required equipment, optional equipment, travel-viable flag, bodyweight-only flag
- **Substitutions table** — no-equipment, hotel, and pain-modified alternatives
- **Progressions** — ordered steps to increase difficulty
- **Regressions** — fallback options when the movement is too hard
- **Contraindications** — conditions that preclude this exercise
- **Caution flags** — form errors or situations requiring extra care
- **Tempo options** — recommended tempo prescriptions
- **Activation sequence** — 2-step pre-exercise primer: mobility unlock + neural prime (plus explosive note where applicable)
- **Cues** — setup, execution, breathing, common mistakes
- **Notes** — programming notes, emphasis, context
- **Media** — status flag plus pointer to `exercise-media-map.md`

---

## Push / Chest

---

### Ring Push-Up
`ring_push_up` · push · Phases: strength, hypertrophy

**Muscles:** pectoralis major, anterior deltoid (primary) · triceps, serratus anterior, rotator cuff stabilizers (secondary)

**Equipment:** gymnastic rings · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | push_up_standard |
| Hotel | push_up_standard |
| Pain-modified | push_up_incline |

**Progressions:** add tempo (4-1-X-0) → add weight vest Phase 2+ → superset with ring fly → progress to archer push-up
**Regressions:** standard push-up, push-up with handles
**Contraindications:** acute shoulder impingement, labrum pain
**Caution flags:** rings swinging outward · rib flare at bottom
**Tempo options:** 4-1-X-0, 3-0-X-0

**Activation sequence**
- *Mobility unlock:* Shoulder CAR (controlled articular rotation) — 5 slow circles each direction, 30 seconds. Opens shoulder capsule before loading it into external rotation.
- *Neural prime:* Push-up plus — 10 reps, protract the scapula hard at the top of each rep to fire serratus anterior and anterior deltoid at low load before the working set.

**Cues**
- *Setup:* Rings at chest height. Hands neutral or slightly turned out. Full dead hang stretch at bottom.
- *Execution:* Lower until chest touches rings, maintaining hollow body. Push to full extension without locking elbows hard.
- *Breathing:* Exhale on the push.
- *Common mistakes:* Flaring elbows past 90 degrees, letting rings drift wide at bottom, losing core tension.

**Notes:** Primary chest movement for home training. Rings rotate to natural hand position, protecting shoulders. Superior to fixed-handle push-ups for shoulder health.
**Media:** status: missing

---

### Ring Fly
`ring_fly` · push · Phases: hypertrophy

**Muscles:** pectoralis major (primary) · anterior deltoid, biceps (secondary)

**Equipment:** gymnastic rings · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | push_up_wide_slow |
| Hotel | dumbbell_chest_fly |
| Pain-modified | push_up_standard |

**Progressions:** increase ROM → slow tempo → superset with ring push-up
**Regressions:** ring_push_up, dumbbell fly, push-up
**Contraindications:** acute shoulder or elbow pain
**Caution flags:** over-rotating the wrist · going too wide and losing elbow control · arms straight (risk of bicep strain)
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Pec minor doorway stretch — lean into doorframe with forearm at 90 degrees, 30 seconds per side. Opens the pec minor so the fly reaches full stretch range.
- *Neural prime:* Ring push-up — 5 slow reps as a pre-activation set, then rest 30 seconds before moving into the fly. Warms the stabilizers at controlled load before the stretch-loaded fly.

**Cues**
- *Setup:* Rings at chest height, arms out wide, slight elbow bend (soft elbow maintained throughout).
- *Execution:* Squeeze hands together and in, contracting the chest. Slow return to start.
- *Breathing:* Exhale as hands come together.
- *Common mistakes:* Straightening the arms fully (bicep strain risk), rushing the return, losing shoulder position.

**Notes:** Highest stretch-load chest exercise in the home inventory. Phase 1 only if shoulder integrity is solid.
**Media:** status: missing

---

### Slider Chest Fly
`slider_chest_fly` · push · Phases: strength, hypertrophy

**Muscles:** pectoralis major (primary) · anterior deltoid, serratus anterior (secondary)

**Equipment:** sliders · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | push_up_wide_slow |
| Hotel | dumbbell_chest_fly_on_floor |
| Pain-modified | push_up_incline |

**Progressions:** increase ROM → add a 2s pause at full fly position → increase reps
**Regressions:** push-up, ring_push_up
**Contraindications:** wrist pain in weight-bearing position
**Caution flags:** sliders sliding too fast (loss of control) · rib flare · hips dropping
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Wrist circles plus prayer stretch — 10 wrist circles each direction, then hands in prayer position pressed flat, 20 seconds. Prepares wrists for the extended weight-bearing position.
- *Neural prime:* Push-up plus — 8 reps with scapular protraction at top to prime serratus anterior, which is the stabilizer keeping the scapulae from winging during the fly.

**Cues**
- *Setup:* Push-up position, hands on sliders. Ribs down. Slight bend at elbows.
- *Execution:* Slide hands wide while lowering chest toward floor. Drive hands back together.
- *Breathing:* Exhale as hands return.
- *Common mistakes:* Moving too fast, hips rising, elbows too straight (shoulder stress).

**Notes:** Fills the loaded chest stretch gap when rings are unavailable or as a complement to ring work. Phase 1+.
**Media:** status: missing

---

### Archer Push-Up
`archer_push_up` · push · Phases: strength, hypertrophy

**Muscles:** pectoralis major, anterior deltoid, triceps (primary) · core, serratus anterior (secondary)

**Equipment:** none · Optional: none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | archer_push_up |
| Hotel | archer_push_up |
| Pain-modified | push_up_incline |

**Progressions:** increase load-side rep ratio → add vest → progress to one-arm push-up
**Regressions:** ring_push_up, standard push-up
**Contraindications:** acute shoulder or elbow pain
**Caution flags:** hips rotating · non-working arm fully locked (elbow stress)
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Thoracic rotation in push-up position — from plank, rotate one hand off the floor and reach toward the ceiling, 5 reps per side. Opens the thoracic spine for the unilateral rotation demand.
- *Neural prime:* Standard push-up — 8 reps at moderate pace to fire the bilateral pressing pattern before shifting to the unilateral load of the archer variation.

**Cues**
- *Setup:* Wide push-up stance. Shift body weight toward one hand as you lower.
- *Execution:* Lower toward the loaded hand with the other arm extended. Push back up through the loaded arm.
- *Breathing:* Exhale on the push.
- *Common mistakes:* Hips twisting, leaning instead of shifting weight, non-working arm doing too much.

**Notes:** Unilateral overload without additional equipment. 70% load shift to one side.
**Media:** status: missing

---

### KB Push Press
`kb_push_press` · push · Phases: strength, hypertrophy

**Muscles:** deltoid, triceps (primary) · upper traps, core, legs (secondary)

**Equipment:** kettlebell · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | pike_push_up |
| Hotel | dumbbell_shoulder_press |
| Pain-modified | landmine_press_or_pike_push_up |

**Progressions:** increase load → add clean before press → strict press variation
**Regressions:** kb_strict_press, dumbbell_shoulder_press
**Contraindications:** acute shoulder impingement, AC joint pain
**Caution flags:** excessive lumbar extension · pressing out of a bad rack position · wrist buckle
**Tempo options:** 3-0-X-0, 2-0-1-0

**Activation sequence**
- *Mobility unlock:* Band external rotation — 15 reps per side at low tension, elbow pinned to ribs. Opens the shoulder into external rotation before loading it overhead.
- *Neural prime:* Pike push-up — 8 reps to prime the overhead pressing pattern and warm the deltoids and triceps before adding leg drive.

**Cues**
- *Setup:* KB in rack position, elbow slightly forward, wrist neutral. Slight knee bend.
- *Execution:* Drive from legs with a sharp hip extension, then press overhead as the hip reaches extension. Lockout overhead with packed shoulder.
- *Breathing:* Exhale at lockout.
- *Common mistakes:* Turning it into a push press from the knees (too much leg drive), losing wrist position, hyperextending the lower back.

**Notes:** Primary overhead push pattern. Phase 1 uses strict press tempo for pattern quality; Phase 2+ uses explosive push press.
**Media:** status: missing

---

### Decline Ring Push-Up
`decline_ring_push_up` · push · Phases: hypertrophy

**Muscles:** pectoralis major (clavicular head), anterior deltoid (primary) · triceps, serratus anterior (secondary)

**Equipment:** gymnastic rings, elevated surface for feet · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | decline_push_up_floor |
| Hotel | decline_push_up_floor |
| Pain-modified | incline_push_up |

**Progressions:** add weight vest → increase decline angle
**Regressions:** ring_push_up, decline push-up on floor
**Contraindications:** shoulder impingement, acute shoulder pain
**Caution flags:** hips rising · rings swinging · losing tension at lockout
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Shoulder CAR — 5 slow controlled articular rotations each direction. The decline angle shifts load to the clavicular head of pec, which needs the upper shoulder capsule warmed.
- *Neural prime:* Ring push-up (flat) — 6 reps at the same rings before elevating feet. Establishes the ring stability pattern at lower difficulty before adding the decline angle.

**Cues**
- *Setup:* Feet on chair or box. Rings at chest height. Hollow body maintained.
- *Execution:* Standard ring push-up with elevated feet loading upper chest.
- *Breathing:* Exhale on push.
- *Common mistakes:* Hips piking up, not maintaining hollow body, rushing the descent.

**Notes:** Fills the upper chest gap that's hard to address without a bench. Phase 1+ as a 2-set accessory, Phase 2+ as primary.
**Media:** status: missing

---

## Pull / Back

---

### Band External Rotation
`band_external_rotation` · pull, rehab, warmup · Phases: prep, rehab, strength

**Muscles:** infraspinatus, teres minor (primary) · posterior deltoid (secondary)

**Equipment:** light resistance band · Optional: anchor point · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | side_lying_external_rotation |
| Hotel | band_external_rotation |
| Pain-modified | isometric_external_rotation_against_wall |

**Progressions:** increase reps from 10 to 15 per side → add one-second pause at end range
**Regressions:** reduce band tension, perform side-lying external rotation without band
**Contraindications:** sharp shoulder pain
**Caution flags:** elbow drifting away from ribs · using trunk rotation instead of shoulder rotation
**Tempo options:** 2-1-2-0

**Activation sequence**
- *Mobility unlock:* Passive shoulder dislocate with band or towel — 10 slow overhead passes, loosening the shoulder capsule through its full arc before isolated rotator cuff loading.
- *Neural prime:* Isometric external rotation against wall — press the back of the wrist into a wall at 90 degrees for 5 seconds, 3 reps per side. Fires the rotator cuff at zero load before adding band resistance.

**Cues**
- *Setup:* Elbow at 90 degrees and pinned to the ribs. Band anchored at elbow height.
- *Execution:* Rotate from the shoulder only. Keep the movement slow and quiet.
- *Breathing:* Exhale as the hand rotates outward.
- *Common mistakes:* Pulling too hard. Letting the elbow drift.

**Notes:** Fixed morning rehab/prehab movement for shoulder maintenance. Rotator cuff opener used before all pressing.
**Media:** status: missing

---

### Ring Row
`ring_row` · pull · Phases: prep, strength, hypertrophy

**Muscles:** rhomboids, middle traps, posterior deltoid, biceps (primary) · lats, lower traps, brachioradialis (secondary)

**Equipment:** gymnastic rings · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | table_row |
| Hotel | cable_seated_row_or_dumbbell_row |
| Pain-modified | band_pull_apart |

**Progressions:** elevate feet → slow tempo (4-2-1-0) → add vest → decrease ring height (more horizontal)
**Regressions:** incline_ring_row, band_pull_apart
**Contraindications:** acute elbow pain
**Caution flags:** hips sagging · only pulling with arms instead of retracting scap first · partial ROM
**Tempo options:** 3-2-1-0, 4-2-1-0

**Activation sequence**
- *Mobility unlock:* Scapular pull-up — 5 reps from dead hang, no elbow bend, only scapular depression and retraction. Wakes the scapular stabilizers before the full rowing pattern.
- *Neural prime:* Band pull-apart — 15 reps, arms straight, pulling to full width. Fires the rear delts and rhomboids at zero load before the working set.

**Cues**
- *Setup:* Rings at hip height for standard, lower for harder. Straight body, heels on ground.
- *Execution:* Initiate by pulling shoulder blades together. Row hands to chest. Full retraction at top.
- *Breathing:* Exhale on the row.
- *Common mistakes:* Hips sagging, not retracting scapula before bending elbow, short ROM.

**Notes:** Horizontal pull — critical complement to vertical pull-ups. Feet elevated is significantly harder.
**Media:** status: missing

---

### KB Single-Arm Row
`kb_single_arm_row` · pull · Phases: strength, hypertrophy

**Muscles:** lats, rhomboids, posterior deltoid (primary) · biceps, forearm, core (secondary)

**Equipment:** kettlebell · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | table_row |
| Hotel | dumbbell_one_arm_row |
| Pain-modified | ring_row |

**Progressions:** add 2s top pause → increase load → chest-supported variation
**Regressions:** ring_row, band_row
**Contraindications:** acute lower back pain during loaded hip hinge
**Caution flags:** rotating trunk to pull · partial ROM · not retracting fully at top
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Hip hinge drill — 10 bodyweight hip hinges touching the wall behind you with both hands, grooves the loaded hip hinge position before adding the unilateral row on top of it.
- *Neural prime:* Ring row — 6 reps at bodyweight to fire the rhomboids and lats at low load before adding the kettlebell.

**Cues**
- *Setup:* Hip hinge position, non-working hand braced on knee. KB in working hand, arm extended.
- *Execution:* Pull KB to hip/lower rib by driving elbow back. 2-second hold at top retraction.
- *Breathing:* Exhale on the row.
- *Common mistakes:* Rotating the torso, short ROM, using momentum.

**Notes:** Primary unilateral back builder. 2s pause at top retraction ensures full lat engagement.
**Media:** status: missing

---

### KB Romanian Deadlift
`kb_romanian_deadlift` · hinge · Phases: strength, hypertrophy

**Muscles:** hamstrings, glutes, lower back (primary) · lats, forearms (secondary)

**Equipment:** kettlebell · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | single_leg_hip_hinge_bodyweight |
| Hotel | dumbbell_rdl |
| Pain-modified | hip_hinge_drill |

**Progressions:** add 1.5-rep method (Phase 2) → single-leg RDL (Phase 3) → increase load
**Regressions:** hip_hinge_drill, kb_deadlift_from_floor
**Contraindications:** acute herniated disc, sharp lower back pain
**Caution flags:** rounding the lower back · bending the knees too much (becomes a squat) · losing KB close to body
**Tempo options:** 4-2-1-0

**Activation sequence**
- *Mobility unlock:* 90/90 hip rotation — sit in 90/90 position, rotate between internal and external hip rotation for 60 seconds. Opens hip internal rotation, which is consistently restricted in athletes who struggle with proper hinge depth.
- *Neural prime:* Glute bridge — 10 reps with 2s hold at top. Fires glutes and hamstrings in the shortened position before loading them eccentrically in the RDL.

**Cues**
- *Setup:* Hinge from hips, not waist. Soft knee bend. KB in both hands or one.
- *Execution:* Push hips back, lower KB along legs maintaining neutral spine. Feel stretch in hamstrings at bottom. Drive hips forward to stand.
- *Breathing:* Inhale on the way down, exhale at top.
- *Common mistakes:* Rounding the lower back, squatting instead of hinging, letting KB swing away from body.

**Notes:** Primary posterior chain hinge. 4-2-1-0 tempo dramatically increases hamstring time under tension.
**Media:** status: missing

---

### KB Swing Dead Stop
`kb_swing_dead_stop` · hinge, conditioning · Phases: strength, conditioning

**Muscles:** hamstrings, glutes, lower back (primary) · lats, deltoids, core (secondary)

**Equipment:** kettlebell · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | broad_jump_or_broad_jump_land |
| Hotel | dumbbell_swing_or_hip_thrust |
| Pain-modified | kb_rdl |

**Progressions:** increase load → add consecutive swings → progress to KB snatch
**Regressions:** kb_rdl, hip_hinge_drill
**Contraindications:** acute lower back pain, acute hamstring strain
**Caution flags:** squatting the swing (quad-dominant) · overextending at top · pulling with arms instead of hip snap
**Tempo options:** explosive

**Activation sequence**
- *Mobility unlock:* Thoracic extension over a foam roller or the edge of a chair — 60 seconds. Frees the thoracic spine for the vertical torso required at the top of the swing.
- *Neural prime:* Hip hinge with bodyweight snap — 10 reps standing, hinging back, then snapping hips forward aggressively. Grooves the hip snap pattern at zero load before the kettlebell is added.
- *Explosive note:* 5 submaximal swings at 50% height before the working set, letting the bell settle fully between each rep. This primes the hip-snap timing without fatiguing the posterior chain before the real sets.

**Cues**
- *Setup:* KB between feet. Hinge to grip, load hamstrings.
- *Execution:* Snap hips to drive KB. Let it float to chest height. Hinge back as it returns. Let it come to a full stop on the floor between each rep.
- *Breathing:* Exhale sharply at top of each rep.
- *Common mistakes:* Muscling with arms, not using hip drive, treating it as a front raise.

**Notes:** Dead stop between reps eliminates momentum cheating. Better hip power training than consecutive swings for this program.
**Media:** status: missing

---

### Towel or Bar Dead Hang
`towel_hang` · pull, rehab · Phases: prep, strength, hypertrophy, rehab

**Muscles:** forearms, hands, biceps (primary) · shoulder girdle, lats (secondary)

**Equipment:** pull-up bar or rings · Optional: towel · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | none |
| Hotel | none |
| Pain-modified | seated_grip_squeeze |

**Progressions:** towel grip (harder) → one-arm alternating hang → add time
**Regressions:** dead hang (standard bar), seated grip holds
**Contraindications:** acute shoulder labrum tear
**Caution flags:** shrugging shoulders up (should stay packed or passive) · swinging
**Tempo options:** timed hold

**Activation sequence**
- *Mobility unlock:* Overhead shoulder CAR — stand, lift both arms overhead, make 5 large controlled circles forward and backward. Decompresses the shoulder joint before adding bodyweight traction.
- *Neural prime:* Scapular pull-up — 5 reps from dead hang, depressing and retracting scapulae without bending elbows. Wakes the lower trap and shoulder girdle before the static hang.

**Cues**
- *Setup:* Full dead hang from bar. Choose full passive (shoulders elevated, decompressive) or scap-packed (shoulders depressed, active).
- *Execution:* Hold. Focus on grip crush. Breathe.
- *Breathing:* Normal rhythmic breathing throughout hold.
- *Common mistakes:* Shrugging aggressively, bending knees for false comfort, cutting time short.

**Notes:** All-cause mortality correlation metric per research. Towel wrapping the bar increases grip demand significantly. Phase 1+ as grip maintenance.
**Media:** status: missing

---

### Y-T-W Prone
`y_t_w_prone` · pull, rehab, warmup · Phases: prep, rehab, strength

**Muscles:** lower trapezius, mid trapezius, rhomboids, posterior deltoid, external rotators (primary) · infraspinatus, teres minor, rear delt (secondary)

**Equipment:** none · Optional: light dumbbells (2-5lb) · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | y_t_w_prone |
| Hotel | y_t_w_prone |
| Pain-modified | y_t_w_seated_against_wall |

**Progressions:** add light DBs (2lb) → add 2s hold at top position
**Regressions:** band_pull_apart, wall slides
**Contraindications:** acute posterior shoulder pain
**Caution flags:** using neck instead of mid-back · lifting too high (compensating with lumbar)
**Tempo options:** 2-1-2-0

**Activation sequence**
- *Mobility unlock:* Prone cobra hold — lie face down, arms at sides, lift chest and hold 10 seconds × 3. Prepares the thoracic extensors to support the Y-T-W positions.
- *Neural prime:* Band pull-apart — 15 reps standing before getting prone. Pre-activates the same posterior chain (rear delt, rhomboids, mid-trap) that the Y-T-W will train.

**Cues**
- *Setup:* Face down, forehead on a rolled towel. Arms start at sides.
- *Execution:* Y: arms overhead at 45 degrees (thumbs up). T: arms straight out to sides. W: elbows at 90 degrees, externally rotate to bring hands up. Pause each position.
- *Breathing:* Exhale as arms lift.
- *Common mistakes:* Using the neck or lumbar, not pausing at top, using too much weight.

**Notes:** Small weight, huge postural benefit. Specifically programs the lower trapezius, the most underdeveloped scapular stabilizer in most athletes.
**Media:** status: missing

---

### Pull-Up Strict
`pull_up_strict` · pull · Phases: strength, hypertrophy, skill

**Muscles:** lats, biceps, lower traps (primary) · forearms, transverse abdominis (secondary)

**Equipment:** pull-up bar · Optional: resistance band, weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | towel_row_or_table_row |
| Hotel | cable_lat_pulldown_or_dumbbell_row |
| Pain-modified | ring_row |

**Progressions:** add reps until 3x8 clean → add tempo → add weight vest
**Regressions:** band-assisted pull-up, eccentric-only pull-up, ring row
**Contraindications:** sharp shoulder pain, uncontrolled elbow tendon pain
**Caution flags:** kipping · partial range · rib flare
**Tempo options:** 3-1-X-1, 4-2-1-0

**Activation sequence**
- *Mobility unlock:* Dead hang 30 seconds — passive hang with shoulders fully elevated, decompressing the shoulder joint and loading the lat in its lengthened position before the pulling work begins.
- *Neural prime:* Scapular pull-up — 8 reps from dead hang, depress and retract scapulae without bending elbows. This is the foundational mechanics of the pull-up starting position — firing it before the full movement locks in the shoulder position at the bottom of every rep.

**Cues**
- *Setup:* Start from a dead hang with ribs down. Slight hollow body; no swinging.
- *Execution:* Pull elbows toward ribs. Finish with chin over bar or chest approaching bar.
- *Breathing:* Exhale through the hard part of the pull.
- *Common mistakes:* Reaching with the chin. Losing shoulder position at the bottom.

**Notes:** Primary vertical pull benchmark.
**Media:** status: missing

---

## Legs / Lower Body

---

### KB Goblet Squat
`kb_goblet_squat` · squat · Phases: prep, strength, hypertrophy

**Muscles:** quadriceps, glutes, adductors (primary) · hamstrings, core, upper back (secondary)

**Equipment:** kettlebell · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | bodyweight_squat_pause |
| Hotel | dumbbell_goblet_squat |
| Pain-modified | box_squat_to_high_box |

**Progressions:** add vest (Phase 2+) → 1.5-rep method at bottom (Phase 3) → pause squat
**Regressions:** bodyweight_squat, goblet_squat_with_light_weight
**Contraindications:** acute knee or hip pain
**Caution flags:** heels rising · torso collapsing forward · KB dropping on descent
**Tempo options:** 4-2-1-0, 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Hip flexor kneeling stretch — 60 seconds per side with posterior pelvic tilt. Releases the hip flexors that limit squat depth and cause anterior tilt under load.
- *Neural prime:* Glute bridge — 10 reps with 2s hold at top. Fires the glutes before they're loaded in the squat, reducing the tendency for the quads to dominate and the glutes to go offline.

**Cues**
- *Setup:* KB held vertically at chest, elbows pointing down. Feet shoulder-width or slightly wider. Toes turned out 10-30 degrees.
- *Execution:* Squat deep, pushing knees out. Elbows track inside knees at bottom. Tall chest throughout.
- *Breathing:* Inhale on descent, exhale at top.
- *Common mistakes:* Heels rising (needs ankle mobility work), chest caving, not hitting depth.

**Notes:** Tempo makes 50lb genuinely brutal. Phase 3 1.5-rep at bottom doubles time under tension in the hardest range.
**Media:** status: missing

---

### KB Front Squat
`kb_front_squat` · squat · Phases: strength

**Muscles:** quadriceps, glutes, core (primary) · upper back, deltoids (secondary)

**Equipment:** kettlebell · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | bodyweight_squat |
| Hotel | dumbbell_front_squat |
| Pain-modified | kb_goblet_squat |

**Progressions:** increase load → add vest → double KB → pause squat
**Regressions:** kb_goblet_squat, bodyweight_squat
**Contraindications:** acute wrist or elbow pain from rack position
**Caution flags:** elbows dropping (KB rolling back) · heel rise · forward lean
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Wrist extension stretch — forearm parallel to floor, gently press hand back with the other, 30 seconds per side. The KB rack position requires a neutral wrist under load; this prevents the most common rack failure.
- *Neural prime:* Goblet squat — 6 reps with a light KB to groove the squat depth before transitioning to the more demanding rack position.

**Cues**
- *Setup:* KB in rack position (handle resting on forearm, elbow high, parallel to ground). Feet shoulder-width.
- *Execution:* Squat deep maintaining elbows up and vertical torso. Drive through heels.
- *Breathing:* Inhale on descent, exhale at top.
- *Common mistakes:* Elbow dropping and losing rack, excessive forward lean, not reaching depth.

**Notes:** More upper back and core demand than goblet squat due to rack position. Primary strength emphasis pattern.
**Media:** status: missing

---

### KB Bulgarian Split Squat
`kb_bulgarian_split_squat` · squat · Phases: strength, hypertrophy

**Muscles:** quadriceps, glutes (primary) · hamstrings, hip flexors, core (secondary)

**Equipment:** kettlebell, elevated surface for rear foot · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | split_squat_bodyweight |
| Hotel | dumbbell_split_squat |
| Pain-modified | forward_lunge_bodyweight |

**Progressions:** increase load → add pause at bottom (2s) → add vest
**Regressions:** split_squat_no_elevation, forward_lunge
**Contraindications:** acute knee pain, hip flexor injury
**Caution flags:** front knee caving in · torso collapsing forward · not reaching bottom range
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Hip flexor kneeling stretch — 60 seconds on the rear-leg side. The rear hip flexor is the primary limiting factor in Bulgarian split squat depth; releasing it before the set directly improves range and reduces compensation.
- *Neural prime:* Lateral band walk — 10 steps each direction with a light band above the knees. Fires glute medius to prevent the front-knee valgus collapse that is the most common form breakdown in the split squat.

**Cues**
- *Setup:* Rear foot elevated on bench or chair. Front foot far enough forward that knee stays over (not past) the toes at bottom.
- *Execution:* Lower until front thigh is parallel or below. 2-second pause at bottom. Drive through front heel.
- *Breathing:* Inhale on descent, exhale on drive up.
- *Common mistakes:* Front foot too close (knee too far forward), torso falling forward, not pausing.

**Notes:** 2s pause at bottom is the key cue — eliminates bounce and forces true range-of-motion strength.
**Media:** status: missing

---

### KB Suitcase Carry
`kb_suitcase_carry` · carry, core · Phases: strength, conditioning

**Muscles:** obliques, quadratus lumborum, core (primary) · traps, forearm, glutes (secondary)

**Equipment:** kettlebell · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | side_plank |
| Hotel | dumbbell_suitcase_carry |
| Pain-modified | side_plank |

**Progressions:** increase load → increase steps → add vest → switch to farmer's carry (bilateral)
**Regressions:** dead_bug, side_plank
**Contraindications:** acute lower back pain
**Caution flags:** lateral trunk lean toward weight (failing the test) · losing neutral spine · heel striking
**Tempo options:** steady pace

**Activation sequence**
- *Mobility unlock:* Side-lying thoracic rotation — lie on side, stack knees, open top arm toward the ceiling and follow with eyes, 8 reps per side. Opens the thoracic spine so the obliques can work from a mobile rib cage rather than compensating.
- *Neural prime:* Side plank hold — 20 seconds each side. Fires the obliques and QL in the lateral stability pattern that the suitcase carry will challenge under walking load.

**Cues**
- *Setup:* KB in one hand, arm at side. Stand tall. Ribs down.
- *Execution:* Walk with tall posture. Resist any lateral lean toward the heavy side. Breathe normally.
- *Breathing:* Normal nasal breathing throughout. If unable to breathe nasally, load is too heavy.
- *Common mistakes:* Leaning into the weight, holding breath, short steps.

**Notes:** All-cause mortality marker — grip and core together. Nasal breathing sustainability is the progression metric.
**Media:** status: missing

---

### Jump Squat → KB Goblet Squat Complex
`jump_squat_goblet_complex` · squat, conditioning · Phases: strength, conditioning

**Muscles:** quadriceps, glutes, calves (primary) · hamstrings, core (secondary)

**Equipment:** kettlebell · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | jump_squat_to_squat_hold |
| Hotel | jump_squat_to_dumbbell_goblet |
| Pain-modified | squat_to_goblet_no_jump |

**Progressions:** add vest for goblet squats only → increase jump height → increase goblet reps
**Regressions:** jump_squat_only, goblet_squat_only
**Contraindications:** acute knee pain, lower limb injury
**Caution flags:** knees caving on landing · not resetting between jumps · rushing into goblet too fast
**Tempo options:** explosive then 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Hip flexor kneeling stretch — 45 seconds per side. Jump squats load the hip flexors aggressively on landing; releasing them first reduces the anterior pelvic tilt pattern under fatigue.
- *Neural prime:* Glute bridge — 10 reps with 2s hold. Fires glutes and quads before the explosive loading so the posterior chain is online from the first jump.
- *Explosive note:* 5 submaximal jump squats at 60% height before the working set, with full landing absorption and 2-second pause between each rep. This primes the stretch-shortening cycle without pre-fatiguing the legs.

**Cues**
- *Setup:* 4 explosive jump squats then immediately pick up KB for 6 goblet squats.
- *Execution:* Jump squats: load, jump, soft landing with hip and knee absorption. Goblet squats: full ROM, no rushing.
- *Breathing:* Breathe between jumps, exhale on each goblet rep.
- *Common mistakes:* Treating the jump as a bounce, not landing through the full foot, rushing goblets without proper depth.

**Notes:** Post-activation potentiation complex. The explosive jump primes neuromuscular firing so the subsequent goblet squat produces higher force output.
**Media:** status: missing

---

### Slider Hamstring Curl
`slider_hamstring_curl` · hinge · Phases: prep, strength, hypertrophy, rehab

**Muscles:** hamstrings (primary) · glutes, calves (secondary)

**Equipment:** sliders · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | nordic_hamstring_eccentric |
| Hotel | towel_hamstring_curl_on_smooth_floor |
| Pain-modified | glute_bridge_isometric |

**Progressions:** add 2s pause at full hip extension → single-leg version
**Regressions:** glute_bridge, hip_raise_only
**Contraindications:** acute hamstring strain
**Caution flags:** hips dropping at any point · losing full hip extension at top
**Tempo options:** 3-2-1-0, eccentric focus

**Activation sequence**
- *Mobility unlock:* Standing hamstring nerve floss — stand, hinge to touch toes, then nod chin to chest while extending one knee, 6 reps per leg. Mobilizes the sciatic nerve and hamstring fascial tissue before the loaded eccentric.
- *Neural prime:* Glute bridge — 10 reps with 2s hold. Establishes hip extension strength and glute activation before adding the hamstring curl demand on top of the bridge position.

**Cues**
- *Setup:* Lie on back, heels on sliders, hips down. Bridge hips fully.
- *Execution:* From bridged position, curl heels in toward glutes, then slide back out to full extension. Hips stay up throughout.
- *Breathing:* Exhale on the curl in.
- *Common mistakes:* Letting hips sag at the end range, rushing the return, losing hip height.

**Notes:** Fills the biggest hamstring eccentric gap in the home program. Slider version bridges between glute bridge and full Nordic curl.
**Media:** status: missing

---

### Slider Adductor Slide
`slider_adductor_slide` · squat, rehab · Phases: prep, strength, hypertrophy, rehab

**Muscles:** adductors (primary) · glutes, quadriceps (secondary)

**Equipment:** sliders · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | sumo_squat_wide |
| Hotel | sumo_squat |
| Pain-modified | lying_adductor_stretch |

**Progressions:** increase ROM → add 2s pause at bottom → single-leg squat depth on support leg
**Regressions:** side_lying_hip_adduction, standing_adductor_stretch
**Contraindications:** acute groin strain or adductor tear
**Caution flags:** sliding foot too far too fast · losing torso upright position · knee caving on support leg
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Sumo squat hold — hold the bottom of a wide-stance squat for 45 seconds, letting gravity open the adductors passively before loading them through range of motion.
- *Neural prime:* Side-lying hip adduction — 12 reps per side lying on the floor, slow and controlled. Fires the adductors in a non-weight-bearing position before the standing slider version.

**Cues**
- *Setup:* Stand with one foot on slider, weight on support foot. Upright torso.
- *Execution:* Slide working foot out laterally as you lower into a single-leg squat on the support leg. Slide back in to standing.
- *Breathing:* Exhale on the return.
- *Common mistakes:* Support knee caving inward, leaning forward, sliding too quickly.

**Notes:** Biggest muscle audit gap fix from v1. Adductors are neglected in most programs and are a primary injury risk in high-volume lower body training.
**Media:** status: missing

---

### Slider Lateral Lunge
`slider_lateral_lunge` · squat, rehab · Phases: prep, strength, hypertrophy, rehab

**Muscles:** glute medius, adductors, quadriceps (primary) · hip abductors, hamstrings (secondary)

**Equipment:** sliders · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | lateral_lunge_bodyweight |
| Hotel | lateral_lunge_bodyweight |
| Pain-modified | lateral_step_touch |

**Progressions:** add KB for loaded version → increase ROM
**Regressions:** lateral_lunge_bodyweight, slider_adductor_slide
**Contraindications:** acute knee medial pain
**Caution flags:** knee caving on working leg · losing torso uprightness · heel rising on support leg
**Tempo options:** 3-2-1-0

**Activation sequence**
- *Mobility unlock:* Hip 90/90 to open lateral hip — sit in 90/90, lean into the front-hip side and feel the external rotation open, 8 slow shifts per side. The lateral lunge demands hip external rotation on the working leg; this unlocks it before loading.
- *Neural prime:* Lateral band walk — 10 steps each direction. Fires the glute medius bilaterally before the single-leg demand of the slider lateral lunge.

**Cues**
- *Setup:* One foot on slider. Upright torso.
- *Execution:* Slide working foot out to the side, lowering into a lateral lunge. Push through heel of both feet to return.
- *Breathing:* Exhale on the return.
- *Common mistakes:* Trunk collapsing, support knee caving, not reaching full lunge depth.

**Notes:** Glute medius + adductor combo. Two gap-fix muscles in one movement.
**Media:** status: missing

---

## Ring Dips + Chest Isolation

---

### Ring Dip — Chest Lean
`ring_dip_chest_lean` · push · Phases: strength, hypertrophy

**Muscles:** pectoralis major, triceps (primary) · anterior deltoid, serratus anterior (secondary)

**Equipment:** gymnastic rings · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | bench_dip |
| Hotel | bench_dip |
| Pain-modified | push_up_standard |

**Progressions:** add weight vest → increase lean angle
**Regressions:** parallel_bar_dip, bench_dip, push_up
**Contraindications:** acute shoulder or AC joint pain
**Caution flags:** shoulders shrugging up · going too deep (anterior shoulder stress) · straight vertical dip angle (becomes tricep only)
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Shoulder CAR with a focus on internal rotation — 5 slow circles each arm, pausing at the internal rotation end range. The ring dip loads the shoulder into anterior stress; opening internal rotation before the set helps center the humeral head.
- *Neural prime:* Ring push-up — 6 reps to warm the stabilizing muscles and establish ring control before adding the dip pattern.

**Cues**
- *Setup:* Lean torso 20-25 degrees forward. Elbows slightly wide.
- *Execution:* Lower until upper arms are parallel to ground. Drive up maintaining lean.
- *Breathing:* Exhale on the push.
- *Common mistakes:* Not leaning (becomes straight tricep dip), shoulders rising to ears, losing ring control.

**Notes:** Forward lean shifts emphasis from triceps to chest. Rings rotate to natural hand position throughout, protecting the shoulder complex.
**Media:** status: missing

---

### DB Floor Press
`db_floor_press` · push · Phases: hypertrophy

**Muscles:** pectoralis major, triceps (primary) · anterior deltoid (secondary)

**Equipment:** dumbbells · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | close_grip_push_up |
| Hotel | dumbbell_floor_press |
| Pain-modified | push_up_incline |

**Progressions:** add slow eccentric (4s) → pause at bottom (triceps on floor) → increase load
**Regressions:** push_up_standard
**Contraindications:** acute elbow or wrist pain
**Caution flags:** elbows past 45-degree angle (shoulder stress) · not touching floor lightly each rep
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Wrist circles plus passive wrist extension — 10 circles each direction, then hold wrist in extension for 20 seconds. Dumbbells require wrist stability in full pronation; this prepares it.
- *Neural prime:* Push-up plus — 8 reps on the floor in the same position to fire the pec, anterior delt, and serratus before adding dumbbell load.

**Cues**
- *Setup:* Lie on back, DBs at chest height, elbows at 45 degrees.
- *Execution:* Press to full extension, lower until triceps lightly touch floor. Pause briefly.
- *Breathing:* Exhale on press.
- *Common mistakes:* Bouncing off the floor, flaring elbows, not pressing to full extension.

**Notes:** Limited ROM compared to bench press, which reduces shoulder stress. Good chest finisher for Thursday isolation block.
**Media:** status: missing

---

### DB Lateral Raise
`db_lateral_raise` · push, rehab · Phases: hypertrophy, rehab

**Muscles:** medial deltoid (primary) · anterior deltoid, supraspinatus (secondary)

**Equipment:** dumbbells · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | band_lateral_raise |
| Hotel | dumbbell_lateral_raise |
| Pain-modified | scapular_plane_raise_light |

**Progressions:** slow eccentric (4s) → seated variation → increase reps before load
**Regressions:** band_lateral_raise, scapular_plane_raise
**Contraindications:** acute rotator cuff tear, acute shoulder impingement
**Caution flags:** shrugging at the top · raising past parallel · using momentum
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Cross-body shoulder stretch — pull one arm across the chest, hold 30 seconds per side. Opens the posterior capsule and reduces the impingement risk that comes from raising through a tight posterior shoulder.
- *Neural prime:* Band pull-apart — 15 reps to fire the rear deltoid and create the posterior-anterior balance before loading the medial deltoid in isolation.

**Cues**
- *Setup:* Slight forward lean at hip (20 degrees). DBs in front of hips, not at sides.
- *Execution:* Raise to parallel (not higher). Slight forward angle in the plane of the scapula.
- *Breathing:* Exhale on the raise.
- *Common mistakes:* Going above parallel, shrugging, swinging the weight.

**Notes:** Keep load light — this is a corrective and hypertrophy movement for the medial delt, not a strength exercise. Slow eccentric is the most effective programming cue.
**Media:** status: missing

---

### DB Rear Delt Fly
`db_rear_delt_fly` · pull, rehab · Phases: hypertrophy, rehab

**Muscles:** posterior deltoid, rhomboids (primary) · middle trapezius, lower trapezius, infraspinatus (secondary)

**Equipment:** dumbbells · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | prone_y_t_w |
| Hotel | dumbbell_rear_delt_fly |
| Pain-modified | band_pull_apart |

**Progressions:** slow eccentric → add pause at top → increase reps
**Regressions:** prone_y_t_w, band_pull_apart
**Contraindications:** acute posterior shoulder or rotator cuff pain
**Caution flags:** using momentum · not hinging at hip · arms too straight (elbow stress)
**Tempo options:** 3-1-X-0

**Activation sequence**
- *Mobility unlock:* Hip hinge drill — 10 bodyweight hinges touching the wall behind you. The rear delt fly is performed in a hip-hinged position; establishing the hinge first prevents lumbar compensation during the shoulder movement.
- *Neural prime:* Band pull-apart — 15 reps standing upright to fire the rear delt and rhomboids before adding the hinge position and dumbbell load.

**Cues**
- *Setup:* Hip hinge 45-60 degrees. DBs hanging. Slight elbow bend.
- *Execution:* Raise arms to side in line with shoulder. Squeeze rear delt and rhomboids at top.
- *Breathing:* Exhale on the raise.
- *Common mistakes:* Swinging torso to help, losing hip hinge, going too heavy.

**Notes:** Posterior delt directly opposes the anterior delt dominance created by pressing volume. Required for shoulder balance at high push volumes.
**Media:** status: missing

---

### DB Curl Pyramid
`db_curl_pyramid` · pull · Phases: hypertrophy

**Muscles:** biceps brachii (primary) · brachialis, brachioradialis (secondary)

**Equipment:** dumbbells · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | band_curl |
| Hotel | dumbbell_curl |
| Pain-modified | band_curl_light |

**Progressions:** 4s eccentric on back-down sets → hammer curl variation → concentration curl
**Regressions:** band_curl
**Contraindications:** acute bicep tendon pain
**Caution flags:** swinging torso · partial ROM · not controlling the lowering
**Tempo options:** 2-0-1-0, 4-0-1-0 on back-down sets

**Activation sequence**
- *Mobility unlock:* Forearm supination and wrist circles — 10 rotations each wrist, then supinate slowly against light resistance (hold a light object). The bicep is a supinator as well as an elbow flexor; warming the supination range reduces distal bicep tendon stress.
- *Neural prime:* Band curl — 15 reps at low tension to fire the bicep at minimal load before adding dumbbell weight.

**Cues**
- *Setup:* Stand or sit. Palms forward. Full arm extension at bottom.
- *Execution:* Curl to shoulder, slow lower. Pyramid: 15lb × 10 → 20lb × 10 → 20lb × 10 → 15lb × 10 slow eccentric.
- *Breathing:* Exhale on curl.
- *Common mistakes:* Elbow drifting forward (partial ROM), swinging, no eccentric control on back-down sets.

**Notes:** The 4-second eccentric on back-down sets is the key — it produces more hypertrophic stimulus than heavier loads done fast.
**Media:** status: missing

---

## Core

---

### Dead Bug
`dead_bug` · core, rehab, warmup · Phases: prep, rehab, strength, hypertrophy

**Muscles:** transverse abdominis, rectus abdominis (primary) · diaphragm, hip flexors, lower back stabilizers (secondary)

**Equipment:** none · Optional: light dumbbell · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | dead_bug |
| Hotel | dead_bug |
| Pain-modified | dead_bug_arms_only |

**Progressions:** add 2s pause at full extension (Phase 2) → add 5lb DB in same-side hand (Phase 3)
**Regressions:** dead_bug_arms_only, dead_bug_legs_only
**Contraindications:** acute herniated disc during leg extension
**Caution flags:** lower back arching off floor · holding breath · rushing the movement
**Tempo options:** slow and controlled, 3s extension

**Activation sequence**
- *Mobility unlock:* 90/90 breathing — lie on back with hips and knees at 90 degrees, feet on a wall or chair, and take 5 slow diaphragmatic breaths. Establishes the intra-abdominal pressure pattern that the dead bug demands.
- *Neural prime:* Dead bug arms-only — 8 reps lowering just the arms to establish the TVA co-contraction before adding the leg component.

**Cues**
- *Setup:* Lie on back. Arms straight up, knees over hips at 90 degrees. Lower back pressed into floor.
- *Execution:* Lower opposite arm and leg toward floor simultaneously. Exhale completely as you extend. Return slowly.
- *Breathing:* Full exhale through each rep — this is the main cue.
- *Common mistakes:* Arching the lower back, only going partway, holding breath.

**Notes:** Same TVA co-contraction as ab vacuum and pull-up hollow body. The exhale cue links all three patterns.
**Media:** status: missing

---

### Ab Roller — Full Extension
`ab_roller` · core · Phases: strength, hypertrophy

**Muscles:** transverse abdominis, rectus abdominis, obliques (primary) · lats, shoulders, hip flexors (secondary)

**Equipment:** ab roller · Optional: weight vest · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | plank_shoulder_tap |
| Hotel | plank_or_slider_pike |
| Pain-modified | plank |

**Progressions:** add 3s pause at full extension (Phase 3) → vest (Phase 3) → progress to standing rollout
**Regressions:** ab_roller_partial_range, plank, dead_bug
**Contraindications:** acute herniated disc, shoulder impingement
**Caution flags:** hips sagging · lumbar overextension (collapse at bottom) · holding breath
**Tempo options:** 4-1-return-0

**Activation sequence**
- *Mobility unlock:* Cat-cow — 10 slow cycles on all fours, emphasizing full spinal flexion at the top. The ab roller demands that the core holds lumbar neutral under full extension; cat-cow warms the spinal range before it's loaded.
- *Neural prime:* Dead bug — 8 reps to fire the TVA in the exact co-contraction pattern that must be maintained throughout the rollout. If the TVA isn't braced first, the lumbar collapses.

**Cues**
- *Setup:* Kneel, hands on roller. Tuck pelvis. Ribs down. TVA braced before moving.
- *Execution:* Roll forward to full extension maintaining plank position. 1s hold. Return under control.
- *Breathing:* Exhale on the rollout, inhale on return.
- *Common mistakes:* Piking hips up on return, collapsing into lumbar extension, no TVA pre-brace.

**Notes:** Phase 3 pause at full extension is the progression that makes this brutally effective without adding load.
**Media:** status: missing

---

### KB Woodchop High-to-Low
`kb_woodchop` · core, conditioning · Phases: strength, conditioning

**Muscles:** obliques, transverse abdominis (primary) · glutes, quadratus lumborum, shoulder girdle (secondary)

**Equipment:** kettlebell · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | bodyweight_rotational_lunge |
| Hotel | dumbbell_rotational_chop |
| Pain-modified | pallof_press |

**Progressions:** increase load → reduce speed (loaded control) → add rotation pause
**Regressions:** pallof_press, anti_rotation_chop_band
**Contraindications:** acute spinal disc injury, acute oblique strain
**Caution flags:** using arms only (rotation must come from hip and trunk) · losing balance on pivot foot · excessive spine flexion
**Tempo options:** controlled 2s

**Activation sequence**
- *Mobility unlock:* Thoracic rotation seated — sit tall in a chair, arms crossed, rotate maximally left and right, 10 reps per side. The woodchop is a transverse-plane movement; thoracic rotation must be available before loading it or the lumbar spine compensates.
- *Neural prime:* Pallof press — 10 reps per side with a light band or cable to fire the rotational stabilizers before the dynamic chop pattern.
- *Explosive note:* 5 slow, deliberate bodyweight woodchop movements at half speed before the working set, feeling the hip rotation drive the arms rather than the arms pulling the movement.

**Cues**
- *Setup:* Stand, KB held with both hands. Weight shifts onto pivot foot on the same side as starting position.
- *Execution:* Drive rotation from the hip. Chop KB from high (above shoulder) to low (outside opposite knee). Rotation, not crunch.
- *Breathing:* Exhale on the chop.
- *Common mistakes:* Arm-only movement, bending at waist instead of rotating, no pivot.

**Notes:** Transverse plane loading — the most neglected plane in most programs. Hip drives the movement, arms transmit.
**Media:** status: missing

---

### Cross-Body Crawl
`cross_body_crawl` · core, conditioning, skill · Phases: prep, strength, conditioning

**Muscles:** core, shoulder, hip (primary) · glutes, shoulders, quadriceps (secondary)

**Equipment:** none · Optional: none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | cross_body_crawl |
| Hotel | cross_body_crawl |
| Pain-modified | bird_dog |

**Progressions:** add load (vest) → increase speed → progress to loaded bear crawl
**Regressions:** dead_bug, bird_dog
**Contraindications:** acute wrist pain in weight-bearing
**Caution flags:** hips rising · losing the contralateral reach (crawling without the cross-body element)
**Tempo options:** deliberate 1s per step

**Activation sequence**
- *Mobility unlock:* Wrist extension and flexion circles — 10 rotations each wrist, plus 20 seconds wrist extension hold with palms flat on floor. Weight-bearing wrist extension is the mechanical demand of the crawl; this is non-negotiable if wrists are stiff.
- *Neural prime:* Bird dog — 8 reps per side from a static kneeling position, extending opposite arm and leg. This is the grounded version of the cross-body coordination before the movement pattern goes mobile.
- *Explosive note:* 10 slow deliberate steps at half speed before progressing to working pace, ensuring the cross-body pattern is established (right arm + left foot together) before adding speed or load.

**Cues**
- *Setup:* Bear position: hips above knees, knees off ground, back flat.
- *Execution:* Move opposite hand and foot together. Right hand forward, left foot forward. Maintain flat back.
- *Breathing:* Exhale every 4 steps.
- *Common mistakes:* Hips rising, moving same-side arm and leg (dog crawl), losing core bracing.

**Notes:** Rotational core + coordination simultaneously. Directly trains the diagonal stability pattern used in boxing, salsa, and carries.
**Media:** status: missing

---

### Side Plank With Hip Dip
`side_plank_hip_dip` · core · Phases: prep, strength, hypertrophy

**Muscles:** obliques, quadratus lumborum, glute medius (primary) · shoulder girdle, adductors (secondary)

**Equipment:** none · Optional: none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | side_plank_hip_dip |
| Hotel | side_plank_hip_dip |
| Pain-modified | side_plank_static_hold |

**Progressions:** add rotation (thread the needle) → leg raise added → feet elevated
**Regressions:** side_plank_static_hold, side_lying_abduction
**Contraindications:** acute shoulder impingement (modify to forearm)
**Caution flags:** hips rotating forward · not reaching full hip drop
**Tempo options:** 2-0-2-0

**Activation sequence**
- *Mobility unlock:* Side-lying thoracic rotation — lie on side, stack hips, open top arm toward ceiling and follow with eyes, 8 reps. Frees the thoracic spine from lateral compression so the obliques can work through full range.
- *Neural prime:* Dead bug — 8 reps to co-activate the TVA and obliques before the side plank isolates the lateral chain under gravity.

**Cues**
- *Setup:* Forearm or hand plank on side. Hips stacked. Full alignment head to heel.
- *Execution:* Lower hip toward floor (dip), then raise to slightly above neutral. Controlled through full range.
- *Breathing:* Exhale on the raise.
- *Common mistakes:* Rotating hips forward, only small ROM hip dip, looking down instead of forward.

**Notes:** Oblique emphasis movement. Pairs with dead bug and woodchop for full core coverage.
**Media:** status: missing

---

## Mobility + Gymnastics

---

### Jefferson Curl
`jefferson_curl` · mobility, rehab · Phases: prep, recovery, rehab

**Muscles:** spinal extensors, hamstrings, upper back (primary) · traps, rhomboids (secondary)

**Equipment:** none · Optional: light dumbbell (5lb) · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | jefferson_curl |
| Hotel | jefferson_curl |
| Pain-modified | seated_forward_fold |

**Progressions:** add minimal load (5lb) → increase height (standing on block)
**Regressions:** seated forward fold, standing toe touch
**Contraindications:** acute disc herniation, active nerve symptoms (numbness or tingling down leg)
**Caution flags:** moving too fast · using load before earning range · breath-holding
**Tempo options:** 5s full descent

**Activation sequence**
- *Mobility unlock:* Supine knee-to-chest — lie on back, pull both knees gently to chest and rock side to side for 30 seconds. Gently decompresses the lumbar spine before asking it to flex under its own weight.
- *Neural prime:* Seated forward fold — sit with legs extended, reach toward feet and hold 20 seconds. Establishes the hamstring length and spinal flexion range that the Jefferson curl will take into a standing, controlled-load context.

**Cues**
- *Setup:* Stand tall. Begin to nod chin to chest, then curl vertebra by vertebra downward.
- *Execution:* Take 5 seconds to descend. Each vertebra peels away from the one above. Hang at the bottom briefly. Reverse slowly.
- *Breathing:* Long exhale on the descent.
- *Common mistakes:* Rushing, hinging at hips instead of segmentally flexing the spine, too much weight too soon.

**Notes:** Counter-intuitive — loaded spinal flexion builds the tissue tolerance that prevents lower back pain. Progress conservatively and never with acute symptoms.
**Media:** status: missing

---

### Skin the Cat
`skin_the_cat` · mobility, skill · Phases: skill, prep, mobility

**Muscles:** shoulder capsule, pectoralis minor, lats (primary) · core, shoulder external rotators (secondary)

**Equipment:** gymnastic rings or pull-up bar · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | none |
| Hotel | none |
| Pain-modified | passive_shoulder_dislocate |

**Progressions:** tuck (Phase 1) → attempt extended (Phase 2) → full German hang (Phase 3)
**Regressions:** passive shoulder dislocate with band or towel, wall slide
**Contraindications:** acute shoulder injury, labrum instability, prior dislocation
**Caution flags:** moving too fast · not tapping strength and control before adding range · skipping tuck progressions
**Tempo options:** slowest possible

**Activation sequence**
- *Mobility unlock:* Passive shoulder dislocate with a band or towel — 10 slow overhead passes, taking 5 seconds each direction. Skin the cat asks the shoulder to pass through its full rotational arc under load; the passive dislocate earns that range first.
- *Neural prime:* Scapular pull-up — 8 reps from dead hang. Fires the lower trap and scapular stabilizers that must be active and in control before any rotation through the German hang position.

**Cues**
- *Setup:* Dead hang from rings. Begin in tuck version only (Phase 1-2).
- *Execution:* Tuck knees to chest, rotate backward until inverted, then continue until German hang. Reverse.
- *Breathing:* Breathe throughout — if breath holds, range is too great.
- *Common mistakes:* Rushing through range, straight-leg attempt before tuck is mastered, jerking movements.

**Notes:** Phase 3 goal for the program. Requires weeks of shoulder preparation (morning circuit F1, scapular pulls, ring rows) before attempting.
**Media:** status: missing

---

### Hip Flexor Kneeling Stretch
`hip_flexor_kneeling_stretch` · mobility, rehab · Phases: prep, rehab, recovery

**Muscles:** psoas, iliacus (primary) · rectus femoris, glute max (secondary)

**Equipment:** mat or soft surface · Optional: none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | standing_hip_flexor_stretch |
| Hotel | hip_flexor_kneeling_stretch |
| Pain-modified | standing_hip_flexor_stretch |

**Progressions:** add active posterior pelvic tilts → add end-range knee drives
**Regressions:** shorten stance, perform standing hip flexor stretch
**Contraindications:** knee pain with kneeling
**Caution flags:** lumbar extension replacing hip extension
**Tempo options:** timed hold

**Activation sequence**
- *Mobility unlock:* Supine knee-to-chest — pull the same-side knee to chest and hold 20 seconds before kneeling. This passive hip flexor lengthen before the loaded stretch prepares the tissue and reduces the initial tightness that causes lumbar compensation.
- *Neural prime:* Standing glute squeeze on the same side — standing on one leg, contract the glute of the opposite (rear leg) side maximally for 5 seconds. Firing glute max creates reciprocal inhibition of the hip flexor, improving the stretch quality from the first second.

**Cues**
- *Setup:* Back knee on a soft surface. Front foot planted and ribs stacked over pelvis.
- *Execution:* Tuck the pelvis before moving forward. Keep the glute of the rear leg lightly active.
- *Breathing:* Long exhales into the stretch.
- *Common mistakes:* Arching the low back. Forcing range instead of owning position.

**Notes:** Fixed morning rehab/prehab movement for hip and low-back mechanics.
**Media:** status: missing

---

## Ankle + Prehab

---

### Pogo Hop
`pogo_hop` · conditioning, warmup, rehab · Phases: prep, conditioning

**Muscles:** gastrocnemius, soleus, Achilles tendon (primary) · tibialis anterior, peroneals (secondary)

**Equipment:** none · Optional: none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | pogo_hop |
| Hotel | pogo_hop |
| Pain-modified | bilateral_calf_raise |

**Progressions:** increase amplitude (Phase 2) → single-leg pogo (Phase 3)
**Regressions:** bilateral calf raise
**Contraindications:** acute Achilles tendon pain, acute plantar fasciitis (modify to lower amplitude only)
**Caution flags:** heel contacting ground (defeats elastic purpose) · knees bending too much (becomes squat) · heel collapse on landing
**Tempo options:** rapid elastic, minimal ground contact

**Activation sequence**
- *Mobility unlock:* Ankle circles and calf stretch — 10 circles each ankle followed by a 30-second standing calf stretch against a wall. Ankle dorsiflexion range directly limits the elastic loading in the Achilles; stretching the calf first improves the spring quality.
- *Neural prime:* Slow bilateral calf raise — 10 reps, 2s up, 2s down, heel fully below neutral at bottom. Fires the calf-Achilles unit through slow range before adding the fast-elastic demand of the pogo.
- *Explosive note:* 5-10 pogo hops at half amplitude before progressing to full height. Start conservatively — the elastic energy storage in the Achilles requires progressive loading, not immediate full intensity.

**Cues**
- *Setup:* Slight forward lean. Feet hip-width.
- *Execution:* Minimal knee bend. Ankle spring drives the hop. Minimal ground contact time. Aim for maximal elastic efficiency.
- *Breathing:* Normal nasal breathing (if unable, amplitude too high).
- *Common mistakes:* Too much knee bend (becomes a jump squat), heels hitting hard, thinking too hard about it.

**Notes:** Training days only — not rest days. Pogo amplitude increases weekly. Elastic loading via stiff ankle is the adaptation target.
**Media:** status: missing

---

### Nordic Hamstring Eccentric
`nordic_hamstring_eccentric` · hinge, rehab · Phases: prep, strength, rehab

**Muscles:** hamstrings (primary) · calves, glutes (secondary)

**Equipment:** foot anchor · Optional: pad, resistance band · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | slider_hamstring_curl_if_sliders_available_or_bridge_walkout |
| Hotel | towel_hamstring_curl |
| Pain-modified | hamstring_bridge_isometric |

**Progressions:** increase lowering duration → reduce hand assistance → add partial concentric
**Regressions:** isometric lean hold, slider hamstring curl
**Contraindications:** acute hamstring strain, sharp posterior knee pain
**Caution flags:** hips folding backward · collapsing quickly
**Tempo options:** 5-0-assisted-0, 8-0-assisted-0

**Activation sequence**
- *Mobility unlock:* Standing hamstring nerve floss — 8 reps per leg: hinge forward, touch toes, nod chin to chest while extending the knee. Frees the sciatic nerve from any adhesion before the high-tension eccentric loading of the Nordic.
- *Neural prime:* Glute bridge — 10 reps with 2s hold at top. Activates the glutes and fires the hamstring-glute connection before the knee-dominant eccentric demand.

**Cues**
- *Setup:* Knees padded and feet anchored. Hips extended, ribs down.
- *Execution:* Lower as one long line from knee to shoulder. Catch with hands before form breaks.
- *Breathing:* Exhale slowly during the lowering.
- *Common mistakes:* Bending at the hips. Treating it like a max-effort test too early.

**Notes:** High-value hamstring resilience movement; progress conservatively.
**Media:** status: missing

---

### Glute Bridge
`glute_bridge` · hinge, warmup, rehab · Phases: prep, rehab, strength

**Muscles:** glutes (primary) · hamstrings, core, spinal extensors (secondary)

**Equipment:** none · Optional: resistance band above knees, weight plate on hips · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | glute_bridge |
| Hotel | glute_bridge |
| Pain-modified | glute_squeeze_isometric |

**Progressions:** add 2s hold at top → single-leg glute bridge (Phase 2) → loaded with band or weight (Phase 3)
**Regressions:** glute_squeeze_standing
**Contraindications:** acute lower back pain during extension
**Caution flags:** using lower back instead of glutes · hyperextending lumbar at top · knees caving
**Tempo options:** 2-2-1-0

**Activation sequence**
- *Mobility unlock:* Hip flexor kneeling stretch — 30 seconds per side. A tight hip flexor prevents full glute activation at the top of the bridge; releasing it first means the bridge actually trains the glutes rather than the spinal extensors.
- *Neural prime:* Glute squeeze standing — 3 maximal isometric glute contractions held 5 seconds each. Wakes the neuromuscular connection to the glute max before the bridging pattern, which many people perform while dominated by the hamstrings.

**Cues**
- *Setup:* Lie on back, knees bent, feet flat. Ribs down. Chin tucked.
- *Execution:* Drive hips straight up. Squeeze glutes hard at top. Maintain for cued hold time.
- *Breathing:* Exhale on bridge up.
- *Common mistakes:* Hyperextending lower back at top, not fully extending hips, feet too far away.

**Notes:** Foundation of glute activation. In morning warm-up, the 2s hold is essential — without it, athletes just go through the motion.
**Media:** status: missing

---

### Lateral Band Walk
`lateral_band_walk` · warmup, rehab · Phases: prep, rehab

**Muscles:** glute medius, hip abductors (primary) · TFL, glute minimus (secondary)

**Equipment:** loop resistance band · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | side_lying_hip_abduction |
| Hotel | lateral_band_walk |
| Pain-modified | side_lying_hip_abduction |

**Progressions:** increase band tension → add squat in the middle of each step
**Regressions:** side-lying hip abduction (no band)
**Contraindications:** acute hip pain
**Caution flags:** band around ankles only (shifts to TFL, not glute med) · torso swaying · short steps
**Tempo options:** controlled 1s per step

**Activation sequence**
- *Mobility unlock:* 90/90 hip rotation — sit in 90/90 on the floor, rotate into internal and external hip rotation on each side, 8 slow shifts. Hip internal rotation restriction is the most common cause of the torso sway compensation in the lateral band walk.
- *Neural prime:* Side-lying hip abduction — 12 reps per side with no band, lying on the floor. Fires the glute medius in isolation before adding the band tension and upright walking pattern.

**Cues**
- *Setup:* Band just above knees. Quarter-squat position. Toes forward.
- *Execution:* Step laterally, maintain tension in band throughout. Keep hips level.
- *Breathing:* Normal nasal breathing.
- *Common mistakes:* Feet coming together between steps (releasing tension), swaying torso, steps too short.

**Notes:** Directly prevents knee valgus collapse in split squats and Bulgarian split squats. Morning warm-up on leg days.
**Media:** status: missing

---

### Scapular Pull-Up
`scapular_pull_up` · pull, warmup, rehab · Phases: prep, rehab

**Muscles:** lower trapezius, serratus anterior, rhomboids (primary) · lats, rotator cuff stabilizers (secondary)

**Equipment:** pull-up bar or rings · Optional: none · Travel-viable: No · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | none |
| Hotel | none |
| Pain-modified | band_pull_apart |

**Progressions:** add 2s hold at retracted position (Phase 2) → progress to full pull-up
**Regressions:** band_pull_apart, prone_Y
**Contraindications:** acute shoulder impingement
**Caution flags:** bending elbows at all (not the goal) · using momentum · not reaching full depression/retraction
**Tempo options:** 2-2-0-0

**Activation sequence**
- *Mobility unlock:* Dead hang 20 seconds — passive shoulders elevated, letting the thoracic spine decompress. Establishes the full range of shoulder elevation before asking the lower trap to depress through that range.
- *Neural prime:* Y-T-W prone — one full Y-T-W set on the floor to fire the lower trap and scapular stabilizers before adding bodyweight hanging load.

**Cues**
- *Setup:* Dead hang from bar. Arms fully straight.
- *Execution:* Without bending elbows, depress and retract shoulder blades. Feel slight rise of body. Hold. Release back to dead hang.
- *Breathing:* Exhale on the depression.
- *Common mistakes:* Bending elbows (becomes a pull-up start), shrugging instead of depressing.

**Notes:** Most important pull-up warm-up movement. Teaches the scapular mechanics that prevent shoulder shrugging at the bottom of every pull.
**Media:** status: missing

---

### Band Pull-Apart
`band_pull_apart` · pull, warmup, rehab · Phases: prep, rehab, strength

**Muscles:** rear deltoid, rhomboids, middle trapezius (primary) · infraspinatus, teres minor (secondary)

**Equipment:** resistance band · Optional: none · Travel-viable: Yes · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | none |
| Hotel | resistance_band_pull_apart |
| Pain-modified | face_pull_with_light_band |

**Progressions:** add external rotation at end range (combo move) → increase band tension → slow eccentric
**Regressions:** face_pull_light_band
**Contraindications:** acute posterior shoulder pain
**Caution flags:** arms not fully extended · using momentum · not pulling to full extension
**Tempo options:** 2-1-2-0

**Activation sequence**
- *Mobility unlock:* Cross-body shoulder stretch — pull one arm across chest, hold 20 seconds per side. Opens the posterior shoulder capsule so the band pull-apart can reach full retraction without restriction.
- *Neural prime:* Isometric rear delt squeeze — reach both arms out to sides and squeeze as if pulling against resistance, 5 seconds × 3. Fires the rear deltoid and rhomboids before adding band tension.

**Cues**
- *Setup:* Hold band with both hands, arms straight out in front, palms down.
- *Execution:* Pull band apart to full arm extension, stretching it across the chest. Squeeze rear delts and rhomboids.
- *Breathing:* Exhale on pull.
- *Common mistakes:* Arms bending, not pulling fully wide, zero control on return.

**Notes:** High frequency is the key — 15 reps daily at low intensity is better than 3 sets weekly at high intensity for posterior shoulder health.
**Media:** status: missing

---

## Warm-Up Activation

---

### Scapular Push-Up
`scapular_push_up` · push, warmup, rehab · Phases: prep, rehab

**Muscles:** serratus anterior, lower trapezius (primary) · pectoralis minor, rhomboids (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | scapular_push_up |
| Hotel | scapular_push_up |
| Pain-modified | wall_scapular_protraction |

**Progressions:** add tempo hold at full protraction → incline surface → rings
**Regressions:** wall scapular protraction
**Contraindications:** acute serratus anterior tear
**Caution flags:** elbows bending · not reaching full protraction · moving too fast
**Tempo options:** 1-2-1-0 (hold 2s at full protraction)

**Activation sequence**
- *Mobility unlock:* Pec minor stretch — hand at shoulder height on doorframe, lean gently forward 20 seconds per side. Opens anterior shoulder so serratus can fully protract.
- *Neural prime:* Wall protraction hold — palms on wall, push through heels of hands, hold 10 seconds. Fires serratus before bodyweight.

**Cues**
- *Setup:* Plank position. Arms fully extended, no elbow bend.
- *Execution:* Without bending elbows, push the floor away — protract the scapulae (round the upper back slightly). Then allow scapulae to retract. This is a small movement, not a large ROM.
- *Breathing:* Exhale on protraction.
- *Common mistakes:* Bending elbows (makes it a push-up), not reaching full protraction, moving too fast.

**Notes:** The primary serratus maintenance movement in the program. Serratus stabilizes the scapula during all pressing and pulling. Failure of serratus leads to winging and shoulder impingement. At 50% effort this is purely maintenance.
**Media:** status: missing

---

### Push-Up Plus
`push_up_plus` · push, warmup · Phases: prep, strength

**Muscles:** serratus anterior, anterior deltoid (primary) · pectoralis, triceps (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | push_up_plus |
| Hotel | push_up_plus |
| Pain-modified | kneeling_push_up_plus |

**Progressions:** feet elevated → add weight vest → push-up plus on rings
**Regressions:** scapular push-up
**Contraindications:** acute shoulder impingement or labral pain
**Caution flags:** skipping the protraction at top · rib flare · hips sagging
**Tempo options:** 3-1-X-1 (hold protraction 1s at top)

**Activation sequence**
- *Mobility unlock:* Shoulder CAR — 3 slow circles each direction per side.
- *Neural prime:* Scapular push-up × 6. Fires serratus at low load before adding the full push-up stimulus.

**Cues**
- *Setup:* Full push-up position. Body rigid.
- *Execution:* Lower to chest. Press to lockout. At the top, push even further — drive the floor away to fully protract the scapulae. That extra range is the "plus."
- *Breathing:* Exhale on push and protraction.
- *Common mistakes:* Stopping at lockout without protraction, losing core tension, rib flare during protraction.

**Notes:** Monday Push warm-up neural prime. Fires serratus and anterior delt before ring push-ups. Band pull-apart covers the posterior shoulder in morning circuit; push-up plus covers the anterior.
**Media:** status: missing

---

### Wall Slide
`wall_slide` · push, warmup, rehab · Phases: prep, rehab

**Muscles:** lower trapezius, serratus anterior (primary) · rotator cuff, rear deltoid (secondary)

**Equipment:** wall · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | wall_slide |
| Hotel | wall_slide |
| Pain-modified | floor_angel |

**Progressions:** add resistance band above elbows → overhead carry → landmine press
**Regressions:** floor angel
**Contraindications:** acute thoracic pain
**Caution flags:** lower back arching from wall · elbows losing contact · shrugging
**Tempo options:** 3-1-3-0

**Activation sequence**
- *Mobility unlock:* Thoracic rotation — 10 each side. Opens thoracic extension needed for overhead position.
- *Neural prime:* Isometric lower trap press — hands on wall at shoulder height, push lightly for 5 seconds.

**Cues**
- *Setup:* Back, elbows, and wrists against wall. Feet 6 inches from wall. Elbows at 90 degrees.
- *Execution:* Slide arms up while maintaining contact with elbows and wrists. Stop at full overhead or end of available range. Slide back slowly.
- *Breathing:* Exhale on slide up.
- *Common mistakes:* Back arching off wall (limited thoracic extension), shrugging, elbows losing contact.

**Notes:** Trains lower trap and serratus through overhead range — the muscles most responsible for shoulder impingement prevention. Pairs with band pull-apart in the warm-up.
**Media:** status: missing

---

### Shoulder CARs
`shoulder_cars` · mobility, warmup, rehab · Phases: prep, rehab, recovery

**Muscles:** shoulder capsule, rotator cuff (primary) · deltoid, pec, lat, thoracic extensors (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | shoulder_cars |
| Hotel | shoulder_cars |
| Pain-modified | smaller_range_shoulder_car |

**Progressions:** add resistance band → Controlled Articular Rotation with light load
**Regressions:** pendulum swing → passive circumduction
**Contraindications:** acute labral tear (modify range)
**Caution flags:** moving too fast · compensating with torso rotation · any pain in the circle
**Tempo options:** 5+ seconds per full circle

**Activation sequence**
- *Mobility unlock:* Cross-body shoulder stretch — 20 seconds per side. Opens posterior capsule before CARs.
- *Neural prime:* The CAR itself is the preparation — no separate neural prime needed.

**Cues**
- *Setup:* Standing. Move the arm through the largest possible controlled circle.
- *Execution:* Flex → external rotation overhead → extension behind → internal rotation → return. Keep the entire movement under active control. No passive hanging points in the circle.
- *Breathing:* Slow nasal. One breath per half circle.
- *Common mistakes:* Moving too fast (becomes a swing), compensating with the torso, avoiding restricted ranges.

**Notes:** Used in Monday/Friday/Sunday Push warm-ups. The purpose is not to warm up — it is to take the shoulder through its full owned range before loading. Any point in the circle where control is lost is a mobility deficit.
**Media:** status: missing

---

### Hip CARs
`hip_cars` · mobility, warmup, rehab · Phases: prep, rehab, recovery

**Muscles:** hip capsule, hip flexors, glutes, deep rotators (primary) · adductors, hamstrings (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | hip_cars |
| Hotel | hip_cars |
| Pain-modified | smaller_range_hip_car |

**Progressions:** standing single-leg CAR with ankle weight
**Regressions:** passive hip circle → supine figure-4
**Contraindications:** acute hip labral tear (pain modification)
**Caution flags:** pelvis tilting to compensate · knee bending to gain range · moving too fast
**Tempo options:** 5+ seconds per full circle

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Glute squeeze isometric — stand on one leg, squeeze glute hard 5 seconds. Activates glute before the CAR demands it.

**Cues**
- *Setup:* Standing on one leg, hand on wall. Raise opposite knee to hip height.
- *Execution:* Move the hip through the largest circle possible while the pelvis stays level. Flex → external rotation → extension → internal rotation → return. If the pelvis tilts, reduce range.
- *Breathing:* Slow nasal.
- *Common mistakes:* Tilting the pelvis to gain range (compensation not mobility), bending the knee, rushing.

**Notes:** Used in Tuesday/Friday warm-ups and Friday CARs circuit. If hip feels rough at the start, continue slowly — the capsule opens within 2-3 circles.
**Media:** status: missing

---

### Neck CARs
`neck_cars` · mobility, warmup, rehab · Phases: prep, rehab, recovery

**Muscles:** cervical extensors, sternocleidomastoid, scalenes (primary) · upper traps, levator scapulae (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | neck_cars |
| Hotel | neck_cars |
| Pain-modified | cervical_rotation_only |

**Progressions:** add isometric resistance with hand at each endpoint
**Regressions:** cervical rotation only → nodding only
**Contraindications:** cervical disc herniation (pain modification), cervical instability
**Caution flags:** any sharp or radiating sensation — stop immediately · moving too fast
**Tempo options:** 5+ seconds per full circle

**Activation sequence**
- *Mobility unlock:* Cervical traction — interlace hands behind head, let head fall forward gently, hold 20s. Decompresses cervical spine before movement.
- *Neural prime:* Chin tuck × 5, hold 3s each. Activates deep cervical flexors before full CAR.

**Cues**
- *Setup:* Standing or seated. Shoulders relaxed.
- *Execution:* Forward nod (not a drop) → lateral flexion to one side → gentle extension → lateral flexion other side → return to forward. Slow and controlled throughout.
- *Breathing:* Nasal. Slow.
- *Common mistakes:* Moving too fast, dropping into extension without control, ignoring any sharp or radiating sensation.

**Notes:** Used in Friday skill day warm-up. Many athletes have asymmetric neck CARs from desk posture and sleep position. The circle becomes more even over weeks. Never force range.
**Media:** status: missing

---

### Ankle CARs
`ankle_cars` · mobility, warmup, rehab · Phases: prep, rehab, recovery

**Muscles:** tibialis anterior, peroneals, gastrocnemius, soleus (primary) · plantar fascia, Achilles (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | ankle_cars |
| Hotel | ankle_cars |
| Pain-modified | ankle_roll |

**Progressions:** add resistance band
**Regressions:** ankle roll (passive)
**Contraindications:** acute Achilles tear or ankle sprain (pain modification)
**Caution flags:** substituting ankle ROM with foot pronation/supination instead of true ankle motion
**Tempo options:** 3+ seconds per full circle

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Single-leg balance × 10s. Fires tibialis and peroneals before the CAR.

**Cues**
- *Setup:* Seated or standing on one leg. Lift foot off ground.
- *Execution:* Plantar flexion → inversion → dorsiflexion → eversion → return. Isolate at the ankle — do not rotate the knee or hip.
- *Breathing:* Normal.
- *Common mistakes:* Rotating the whole leg instead of isolating the ankle, skipping restricted ranges.

**Notes:** Used in Phase 3 Friday warm-up. Ankle stiffness work (pogo, tib raise, soleus) addresses capacity; ankle CARs address joint range. Both are needed.
**Media:** status: missing

---

## Mobility / Joint Care

---

### Hip Circle
`hip_circle` · mobility, warmup · Phases: prep, recovery

**Muscles:** hip flexors, glutes, adductors, TFL (primary) · core stabilizers (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | hip_circle |
| Hotel | hip_circle |
| Pain-modified | supine_hip_circle |

**Progressions:** hip CARs (controlled, larger range)
**Regressions:** supine hip circle
**Contraindications:** none
**Caution flags:** lateral trunk sway · small range
**Tempo options:** 2-3 seconds per circle

**Activation sequence**
- *Mobility unlock:* Hip flexor kneeling stretch — 20s/side. Opens hip flexors before the circle uses hip extension range.
- *Neural prime:* Glute squeeze standing — 5 seconds per side.

**Cues**
- *Setup:* Standing, hands on hips. Feet shoulder-width.
- *Execution:* Draw large circles with your hips. Front → side → back → other side. As large as possible without compensating with the upper body.
- *Breathing:* Normal.
- *Common mistakes:* Small range, tilting the whole torso instead of moving from the hip.

**Notes:** Used in Tuesday Zone 2 warm-up and Friday skill warm-up. Low-skill joint lubrication before sustained locomotion or skill work. Stiffness at the start is feedback — stay in the movement until it loosens.
**Media:** status: missing

---

### World's Greatest Stretch
`worlds_greatest_stretch` · mobility, warmup · Phases: prep, recovery

**Muscles:** hip flexors, thoracic rotators, hamstrings, adductors (primary) · shoulders, ankles (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | worlds_greatest_stretch |
| Hotel | worlds_greatest_stretch |
| Pain-modified | split_into_components |

**Progressions:** add hold at top of rotation → add lateral reach
**Regressions:** split into hip flexor stretch + thoracic rotation separately
**Contraindications:** none
**Caution flags:** front knee caving · rounding instead of rotating · rushing
**Tempo options:** 3 counts per position

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Hip circle × 5/side. Warms the hip before the lunge position is loaded.

**Cues**
- *Setup:* Lunge position, front foot flat, back knee hovering.
- *Execution:* Bring same-side hand to instep of front foot. Rotate opposite arm toward ceiling. Return arm down. Step forward with opposite foot. Repeat.
- *Breathing:* Exhale on the rotation.
- *Common mistakes:* Front knee caving, rounding the back instead of rotating from thoracic, losing the lunge.

**Notes:** Used in Tuesday Zone 2 warm-up. The single best movement-prep exercise for full-body warm-up — hits hip flexors, thoracic rotation, and hamstring length in one flowing movement. Slow = mobility work; faster = warm-up.
**Media:** status: missing

---

### Cat-Cow
`cat_cow` · mobility, warmup, recovery · Phases: prep, recovery, rehab

**Muscles:** lumbar erectors, multifidus (primary) · abdominals, thoracic extensors (secondary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | cat_cow |
| Hotel | cat_cow |
| Pain-modified | seated_spinal_flexion_extension |

**Progressions:** add thoracic rotation at top of extension (thread-the-needle)
**Regressions:** standing spinal flexion/extension
**Contraindications:** none (pace-modify for acute disc pain)
**Caution flags:** forcing range · jamming into lumbar extension · moving too fast
**Tempo options:** 4 counts each way, breath-led

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable — this is purely movement preparation.

**Cues**
- *Setup:* All fours. Hands under shoulders, knees under hips.
- *Execution:* Cow — drop belly toward floor, lift chest and tailbone, inhale. Cat — push floor away, round spine toward ceiling, tuck chin and pelvis, exhale. Breathe to pace the movement.
- *Breathing:* Inhale into cow, exhale into cat. Full breath each rep.
- *Common mistakes:* Moving from the neck only instead of the whole spine, rushing, not reaching full range in both directions.

**Notes:** Saturday morning R1 across all phases. Primary morning warm-up for gymnastics/mobility day. Phase 3 variant adds thoracic rotation at the top of the cow phase (thread-the-needle) for a full spinal prep.
**Media:** status: missing

---

### 90/90 Hip Stretch
`hip_90_90` · mobility, warmup · Phases: prep, recovery, rehab

**Muscles:** hip internal rotators (front leg), hip external rotators (back leg), adductors (primary) · hip flexors, piriformis (secondary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | hip_90_90 |
| Hotel | hip_90_90 |
| Pain-modified | supine_figure_4 |

**Progressions:** add PAILs + RAILs → add hip lift at each position → active 90/90 flow
**Regressions:** supine figure-4, pigeon prep
**Contraindications:** acute hip labral tear (pain modification)
**Caution flags:** spine rounding excessively · weight through the knee · rushing out of position
**Tempo options:** 60s per position (static) or 5 slow transitions (flow)

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Glute bridge × 10 before the 90/90 to activate glutes and create body heat before passive hip work.

**Cues**
- *Setup:* Seated. Front leg at 90 degrees (knee and hip both at 90). Back leg at 90 degrees behind. Shin parallel to front of mat.
- *Execution:* Static — sit tall, breathe into the hip. Flow — shift weight to transition front leg to behind, alternating sides.
- *Breathing:* Long exhale on each hold. Do not hold breath.
- *Common mistakes:* Leaning hard to one side, letting the back collapse, rushing out of position.

**Notes:** Used in Saturday warm-up and Saturday morning R2 Phase 2+. Addresses both hip internal and external rotation simultaneously — the most common combined deficit in strength athletes and desk workers.
**Media:** status: missing

---

### Thoracic Rotation
`thoracic_rotation` · mobility, warmup · Phases: prep, recovery

**Muscles:** thoracic rotators, obliques (primary) · lats, intercostals (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | thoracic_rotation |
| Hotel | thoracic_rotation |
| Pain-modified | seated_thoracic_rotation |

**Progressions:** add reach at end of rotation → rotate against light resistance
**Regressions:** seated thoracic rotation
**Contraindications:** none
**Caution flags:** rotating from lumbar spine instead of thoracic · hip compensating
**Tempo options:** 2-3 seconds each way

**Activation sequence**
- *Mobility unlock:* Cat-cow × 5. Opens the spine before asking for rotation.
- *Neural prime:* Not applicable — this is mobility work.

**Cues**
- *Setup:* Quadruped or seated. For quadruped: place one hand behind head.
- *Execution:* Rotate elbow toward opposite wrist (close), then open toward ceiling. The movement comes from the thoracic spine. Lower back stays still.
- *Breathing:* Exhale on the rotation open.
- *Common mistakes:* Rotating from hips or lower back, moving too fast, not getting full range.

**Notes:** Used in Saturday warm-up and Tuesday warm-up. Loss of thoracic rotation loads the lumbar spine and shoulder with rotational demands they should not absorb.
**Media:** status: missing

---

### Pigeon Prep
`pigeon_prep` · mobility, warmup · Phases: prep, recovery

**Muscles:** piriformis, glute medius, hip external rotators (primary) · hip flexors, IT band (secondary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | pigeon_prep |
| Hotel | pigeon_prep |
| Pain-modified | supine_figure_4 |

**Progressions:** full pigeon → elevated pigeon
**Regressions:** supine figure-4
**Contraindications:** knee instability
**Caution flags:** knee twisting instead of hip rotating · forcing hip to floor
**Tempo options:** 60s hold per side minimum

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable — passive mobility work.

**Cues**
- *Setup:* From quadruped, bring one shin forward parallel to the top of the mat (or at an angle if hip is restricted). Extend opposite leg straight behind.
- *Execution:* Lower hips toward mat. Use hands to control descent. Hold and breathe into the outer hip. Do not force the hip to the floor.
- *Breathing:* Long exhale on each breath. Breathe into the front hip.
- *Common mistakes:* Front foot too close to hip (reduces hip angle), torquing the knee, holding breath.

**Notes:** Used in Saturday warm-up for gymnastics/mobility day. Addresses hip external rotator tightness that limits squat depth, 90/90 position, and all rotational movements.
**Media:** status: missing

---

### Supine Knee-to-Chest
`supine_knee_to_chest` · mobility, warmup, recovery · Phases: prep, recovery

**Muscles:** lumbar erectors, glute (passive stretch), sacroiliac joint (primary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | supine_knee_to_chest |
| Hotel | supine_knee_to_chest |
| Pain-modified | supported_single_knee_hug |

**Progressions:** add ankle circles while holding → progress to supine spinal twist
**Regressions:** seated forward lean
**Contraindications:** none
**Caution flags:** pulling aggressively · neck tension
**Tempo options:** 30s hold per side

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable — decompression work.

**Cues**
- *Setup:* Supine. One or both knees drawn to chest.
- *Execution:* Hug knee(s) gently toward chest. Hold. Breathe into the lower back. Let gravity do the work.
- *Breathing:* Long exhale. Let the body relax on each exhale.
- *Common mistakes:* Pulling with effort, tensing the neck.

**Notes:** Used in Saturday warm-up spinal prep before Jefferson curl. Also in night recovery when low back is compressed. Decompresses lumbar spine and sacroiliac joint.
**Media:** status: missing

---

### Seated Forward Fold
`seated_forward_fold` · mobility, warmup · Phases: prep, recovery

**Muscles:** hamstrings, lumbar erectors, calf (passive stretch) (primary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | seated_forward_fold |
| Hotel | seated_forward_fold |
| Pain-modified | seated_forward_fold_bent_knee |

**Progressions:** add passive load on back → progress to Jefferson curl
**Regressions:** bent-knee version
**Contraindications:** acute disc herniation with anterior loading pain
**Caution flags:** forcing the fold · bouncing · neck craning forward
**Tempo options:** 20s hold × 2

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable — pre-Jefferson curl spinal prep.

**Cues**
- *Setup:* Seated, legs extended. Sit tall first.
- *Execution:* Reach forward, let the spine round gradually. Hold at end of range. Breathe into the hamstrings and lower back.
- *Breathing:* Long exhale on each hold. Relax further into the fold on each exhale.
- *Common mistakes:* Forcing range with aggressive pulling, bouncing, neck jutting forward.

**Notes:** Used in Saturday warm-up spinal prep. Establishes hamstring length and controlled spinal flexion range before the standing, loaded Jefferson curl. This is the neural prime referenced in the Jefferson curl activation sequence.
**Media:** status: missing

---

### Supine Spinal Twist
`supine_spinal_twist` · mobility, recovery · Phases: prep, recovery

**Muscles:** lumbar rotators, thoracolumbar fascia (primary) · glute, IT band, thoracic rotators (secondary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | supine_spinal_twist |
| Hotel | supine_spinal_twist |
| Pain-modified | bent_knee_drop_smaller_range |

**Progressions:** add hold time → add top knee weight
**Regressions:** bent-knee drop (smaller range)
**Contraindications:** acute lumbar disc with rotational pain
**Caution flags:** forcing knee to floor · opposite shoulder lifting fully
**Tempo options:** 30s hold per side

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable — decompression and rotation work.

**Cues**
- *Setup:* Supine. Bring one knee to chest, cross it to the opposite side with light hand pressure. Extend same-side arm out.
- *Execution:* Let the knee drop toward floor. Hold and breathe.
- *Breathing:* Long exhale. Let the body settle on each exhale.
- *Common mistakes:* Forcing the knee to the floor when opposite shoulder lifts significantly (that is the end range — do not force further).

**Notes:** Phase 3 Saturday morning R2. Also night recovery Movement 5. Intervertebral fluid returns during this position. Addresses cumulative spinal compression from the training day.
**Media:** status: missing

---

### Ankle Roll
`ankle_roll` · mobility, warmup · Phases: prep, recovery

**Muscles:** peroneals, tibialis anterior, gastrocnemius (primary) · plantar fascia, Achilles (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | ankle_roll |
| Hotel | ankle_roll |
| Pain-modified | ankle_roll |

**Progressions:** ankle CARs (active, controlled version)
**Regressions:** seated ankle roll
**Contraindications:** none
**Caution flags:** none
**Tempo options:** 10 circles each direction

**Activation sequence**
- *Mobility unlock:* Self-contained.
- *Neural prime:* Not applicable.

**Cues**
- *Setup:* Seated or standing, foot lifted.
- *Execution:* Draw slow circles with the ankle. Maximize plantar flexion and dorsiflexion range.
- *Breathing:* Normal.
- *Common mistakes:* Small range, rotating the whole lower leg.

**Notes:** Used in Tuesday Zone 2 warm-up. Low-intensity joint preparation before walking and Zone 2 work. Passive/rhythmic — distinguishable from ankle CARs which are controlled articular.
**Media:** status: missing

---

## Rehab / Daily Practice (Standalone)

---

### Tibialis Raise
`tibialis_raise` · rehab, warmup · Phases: prep, rehab, recovery

**Muscles:** tibialis anterior (primary) · peroneals (secondary)

**Equipment:** wall · Optional: ankle weight · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | tibialis_raise |
| Hotel | tibialis_raise |
| Pain-modified | seated_tibialis_raise |

**Progressions:** add ankle weight → increase rep count → slow eccentric (3s lower)
**Regressions:** seated version
**Contraindications:** acute anterior shin compartment syndrome
**Caution flags:** partial range · rushing
**Tempo options:** 1s up, 1s hold at top, controlled lower

**Activation sequence**
- *Mobility unlock:* Ankle roll × 10 each direction.
- *Neural prime:* Single-leg balance × 15s per side. Fires tibialis in stabilization mode before isolated movement.

**Cues**
- *Setup:* Back against wall. Heels approximately 4 inches from wall. Weight through heels.
- *Execution:* Lift toes and forefoot as high as possible. Hold 1 second at top. Lower with control.
- *Breathing:* Normal.
- *Common mistakes:* Partial range (not reaching full dorsiflexion), rushing, leaning forward.

**Notes:** Part of F4 in morning circuit and ankle stiffness block. Tibialis anterior directly protects the patellar tendon and Achilles under load at 225lb. Daily low-intensity work is the correct dosing strategy — connective tissue adapts slowly.
**Media:** status: missing

---

### Single-Leg Soleus Raise
`single_leg_soleus_raise` · rehab, warmup · Phases: prep, rehab, recovery

**Muscles:** soleus (primary) · gastrocnemius, Achilles tendon (secondary)

**Equipment:** elevated surface (step, curb, or book) · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | flat_single_leg_calf_raise |
| Hotel | flat_single_leg_calf_raise |
| Pain-modified | bilateral_calf_raise |

**Progressions:** add load (vest, DB) → increase elevation → slow eccentric (4s)
**Regressions:** bilateral calf raise
**Contraindications:** acute Achilles tendinopathy (reduce load, not eliminate)
**Caution flags:** knee fully straight (hits gastroc not soleus) · rushing the lowering
**Tempo options:** 2s up, 2s hold, 3s lower

**Activation sequence**
- *Mobility unlock:* Ankle dorsiflexion stretch — foot on elevated surface, lean knee forward over toes, hold 20s. Opens ankle range before loaded calf work.
- *Neural prime:* Bilateral calf raise × 10. Prepares Achilles before single-leg loading.

**Cues**
- *Setup:* One foot on elevated surface. Slight knee bend (~20-30°) — targets soleus over gastrocnemius.
- *Execution:* Full plantar flexion up. Hold. Lower heel below surface level for full ROM.
- *Breathing:* Exhale up.
- *Common mistakes:* Knee fully straight, no heel drop below surface (loses Achilles eccentric), bilateral compensation.

**Notes:** Part of F4 morning circuit and ankle stiffness block. Soleus is the primary Achilles load-bearing muscle at walking/jogging speeds. At 225lb, daily soleus maintenance is connective tissue insurance.
**Media:** status: missing

---

## Breathing / Recovery

---

### Physiological Sigh
`physiological_sigh` · recovery · Phases: recovery

**Muscles:** diaphragm (primary) · intercostals (secondary)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | physiological_sigh |
| Hotel | physiological_sigh |
| Pain-modified | slow_exhale_only |

**Progressions:** none — regulation tool, not a progression
**Regressions:** extended exhale only
**Contraindications:** none
**Caution flags:** more than 5 cycles per session (risk of light-headedness)
**Tempo options:** double inhale (~2s) then extended exhale (6-8s)

**Activation sequence**
- *Mobility unlock:* Not applicable.
- *Neural prime:* Not applicable — this IS the regulation tool.

**Cues**
- *Setup:* Lying down or seated.
- *Execution:* Double inhale through the nose — short sniff then a full inhale on top of it. Then a very long, slow exhale through the mouth.
- *Breathing:* The movement is the breathing. 3-5 cycles only.
- *Common mistakes:* More than 5 cycles, exhaling too quickly.

**Notes:** Night recovery Movement 1. The fastest known method to reduce acute physiological stress. The double inhale reinflates partially collapsed alveoli. The extended exhale activates the vagus nerve and drops heart rate within 1-3 cycles.
**Media:** status: missing

---

### Supine Thoracic Release
`supine_thoracic_release` · recovery, mobility · Phases: recovery, rehab

**Muscles:** thoracic extensors, rib cage (primary) · lats, pec minor (secondary)

**Equipment:** foam roller or rolled towel/yoga mat · Travel-viable: Yes (towel) · Bodyweight-only: No

| Substitution | Movement |
|---|---|
| No equipment | rolled_yoga_mat |
| Hotel | rolled_towel |
| Pain-modified | seated_thoracic_extension_over_chair |

**Progressions:** arms overhead during extension → add cervical rotation at top
**Regressions:** seated thoracic extension over chair back
**Contraindications:** acute thoracic disc herniation with extension pain
**Caution flags:** roller on lumbar spine (must be mid-back only) · forcing extension
**Tempo options:** 2 minutes, gravity-led

**Activation sequence**
- *Mobility unlock:* Not applicable — decompression work.
- *Neural prime:* Not applicable.

**Cues**
- *Setup:* Place foam roller perpendicular to spine at mid-back — T6-T8, behind the shoulder blades, not the lower back. Arms crossed or extended overhead.
- *Execution:* Allow gravity to produce thoracic extension over the roller. Breathe slowly. Let the upper body weight sink in over 2 minutes.
- *Breathing:* Slow nasal. Full exhale to let the chest sink on each breath.
- *Common mistakes:* Roller on lumbar spine, forcing extension aggressively, short duration (2 minutes minimum).

**Notes:** Night recovery Movement 3. Thoracic spine is chronically flexed from anterior-dominant training and desk work. 2 minutes of gravity-assisted extension over weeks significantly improves thoracic mobility, which transfers to pull-up overhead position and pressing shoulder stability.
**Media:** status: missing

---

### Exhale-Only Supine Reset
`exhale_only_supine_reset` · recovery · Phases: recovery

**Muscles:** diaphragm (primary) · TVA (passive, not trained)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | exhale_only_supine_reset |
| Hotel | exhale_only_supine_reset |
| Pain-modified | crocodile_breathing |

**Progressions:** none — recovery tool, not a progression
**Regressions:** crocodile breathing only
**Contraindications:** none
**Caution flags:** do not brace · do not treat as core training · do not count as training volume
**Tempo options:** breath-paced only — one extension per exhale

**Activation sequence**
- *Mobility unlock:* Not applicable.
- *Neural prime:* Not applicable — recovery only.

**Cues**
- *Setup:* Supine. Arms over chest. Knees at 90 degrees. Identical starting position to morning dead bug.
- *Execution:* Extend opposite arm and leg ONLY on the exhale. On the inhale, return. Movement is paced entirely by breath — no muscular exertion target. No bracing. No TVA loading.
- *Breathing:* The breath leads. The movement follows. Exhale = extend. Inhale = return.
- *Common mistakes:* Bracing, moving on the inhale, counting reps as training volume, trying to feel the TVA engage.

**Notes:** Night recovery Movement 4. Same position as morning F3 (dead bug) but entirely different intent. This is breath regulation using familiar movement as an anchor. Must be labeled "Exhale-Only Supine Reset" in the app — the label "dead bug" implies training intent and causes confusion.
**Media:** status: missing

---

### Crocodile Breathing
`crocodile_breathing` · recovery · Phases: recovery

**Muscles:** diaphragm, posterior intercostals (primary) · TVA (secondary)

**Equipment:** yoga mat · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | crocodile_breathing |
| Hotel | floor_or_bed |
| Pain-modified | crocodile_breathing |

**Progressions:** none — regulation tool
**Regressions:** seated diaphragmatic breathing
**Contraindications:** none
**Caution flags:** chest breathing (defeats the purpose)
**Tempo options:** 4-6 breaths per minute

**Activation sequence**
- *Mobility unlock:* Not applicable.
- *Neural prime:* Not applicable.

**Cues**
- *Setup:* Prone (face down). Arms folded under forehead.
- *Execution:* Breathe slowly and fully into the lower back and sides. Chest is mechanically restricted by the floor. Feel the lower back and sides expand laterally on each inhale. Exhale completely.
- *Breathing:* 4-6 breaths per minute. Fully into the back ribs. Chest stays still.
- *Common mistakes:* Trying to lift the chest (the floor prevents this — that is the design), breathing too fast.

**Notes:** Night recovery Movement 6. The prone position prevents chest breathing by design, forcing diaphragmatic mechanics. Direct training stimulus for diaphragm lateral and posterior expansion — the most efficient breathing pattern and strongest parasympathetic activator. 2 minutes significantly reduces resting heart rate before sleep.
**Media:** status: missing

---

### 4-7-8 Breath
`four_seven_eight_breath` · recovery · Phases: recovery

**Muscles:** diaphragm (primary) · autonomic nervous system (effect target)

**Equipment:** none · Travel-viable: Yes · Bodyweight-only: Yes

| Substitution | Movement |
|---|---|
| No equipment | four_seven_eight_breath |
| Hotel | four_seven_eight_breath |
| Pain-modified | extended_exhale_only |

**Progressions:** none
**Regressions:** extended exhale only (inhale 4s, exhale 8s, no hold)
**Contraindications:** none
**Caution flags:** light-headedness if hold is too long · no more than 4-5 cycles per session
**Tempo options:** inhale 4s, hold 7s, exhale 8s × 4-5 cycles

**Activation sequence**
- *Mobility unlock:* Not applicable.
- *Neural prime:* Not applicable.

**Cues**
- *Setup:* Supine or seated. Eyes closed if possible.
- *Execution:* Inhale through nose for 4 seconds. Hold for 7 seconds. Exhale through mouth (audible) for 8 seconds. Repeat 4-5 cycles.
- *Breathing:* The technique is the breathing. 7-second hold forces CO2 accumulation that triggers parasympathetic response. 8-second exhale activates the vagus nerve.
- *Common mistakes:* Shortening the hold, more than 5 cycles, silent exhale (the audible release helps drop tension).

**Notes:** Night recovery Movement 7 — the final movement before sleep. After 4-5 cycles most athletes report a distinct physical shift: temperature drops slightly, muscle tension releases. That is the target state. Technique from Dr. Andrew Weil via pranayama.
**Media:** status: missing

---

## Library Expansion Rule

Before an exercise appears in a generated workout, it must have:

- An exercise ID.
- Movement pattern tags.
- Required equipment.
- At least one regression.
- At least one substitution for the user's alternate mode if travel is enabled.
- Setup, execution, and common-mistake cues.
- A media object, even if status is `missing`.
- A corresponding row in `exercise-media-map.md`, even if status is `missing`.
- An activation sequence with at least a mobility unlock and neural prime.
