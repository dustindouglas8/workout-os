# Progressions And Testing

## Purpose

This file defines how Workout OS decides whether a user should advance, repeat, deload, or pivot. It connects daily logs, weekly logs, phase tests, and block reviews.

## Decision Model

Use **gate + coach override**:

- The system recommends a decision from objective markers.
- The user or coach can override the recommendation.
- Overrides must be logged with a reason.

## Daily Log

Captured after each training session:

| Field | Type | Purpose |
|---|---|---|
| Date | Auto | History key. |
| Planned session | Auto | Compare plan to execution. |
| Completed status | Completed / Modified / Skipped | Adherence. |
| Readiness color | Green / Yellow / Red | Recovery context. |
| Session RPE | 1-10 | Internal load. |
| Pain score | 0-10 | Safety trend. |
| Pain location | Text | Pattern-specific regression trigger. |
| Main lift result | Text or structured | Progress tracking. |
| Notes | Text | Context: sleep, stress, travel, form. |

## Weekly Log

Captured once per week:

| Field | Purpose |
|---|---|
| Bodyweight average | Recomp trend. |
| Waist or photo notes | Optional body comp context. |
| Sleep average | Recovery trend. |
| RHR or HRV trend | Autonomic recovery. |
| Training days completed | Adherence. |
| Yellow/Red count | Recovery load. |
| Top pain location | Safety. |
| Best performance note | Momentum and objective progress. |

## Phase Review

Every 3-4 weeks, run tests and assign one result:

| Result | Criteria |
|---|---|
| Advance | Benchmarks are stable/improving, pain is controlled, and readiness is acceptable. |
| Repeat | Some targets missed but recovery is stable and the goal remains correct. |
| Deload | Fatigue, pain, or readiness suggests adaptation is not landing. |
| Pivot | Current block goal no longer matches the user's constraints or outcomes. |

## General Advancement Gates

Advance only if most are true:

- Adherence is 80% or better.
- Pain is 0-3/10 and not trending upward.
- No unexplained sharp pain during benchmark movements.
- Readiness is Green or Yellow most days.
- Sleep and RHR/HRV are stable enough to absorb the next phase.
- At least two performance or movement-quality markers improved or held steady.

Repeat or deload if:

- Two Red days occur in one week.
- Pain rises in the same pattern for two consecutive exposures.
- Sleep average drops below 6.5 hours for two weeks.
- Performance drops in two unrelated benchmarks.
- User needs repeated Yellow modifications to finish ordinary sessions.

## Block Review

At the end of each 8-12 week block:

1. Compare starting and ending benchmarks.
2. Review body composition trend if recomp is a goal.
3. Review pain and readiness trends.
4. Decide whether the next block should increase intensity, hold intensity, reduce load, or pivot goal.
5. Finalize the next block and revise the annual roadmap.

## Benchmark Categories

### Strength

- Strict pull-up max or best clean submax set.
- Push-up, ring push-up, or press benchmark.
- Squat or split-squat benchmark.
- Hinge benchmark.
- Carry benchmark.

### Recovery

- Sleep average.
- RHR or HRV trend.
- Joint pain score.
- Energy average.
- Yellow/Red count.

### Recomp

- Bodyweight trend.
- Waist measurement or photo notes.
- Strength retention or improvement.
- Protein adherence.

### Mobility / Rehab

- Ankle dorsiflexion or pogo quality.
- Single-leg balance.
- Hip flexor position test.
- Shoulder overhead position or controlled articular rotation quality.
- Spine/hip comfort in daily life.

### Conditioning

- Zone 2 pace at nasal breathing.
- Resting HR trend.
- Time to recover after conditioning.

## Example Exercise Gates

### Strict Pull-Up

| Gate | Next Step |
|---|---|
| 3x5 clean full-ROM reps | Add one rep per set over time. |
| 3x8 clean reps | Add tempo or light vest. |
| Tempo 3x6 clean | Increase load or complexity. |
| Pain or form breakdown | Regress to band-assisted, eccentric, or row variation. |

### Nordic Hamstring

| Gate | Next Step |
|---|---|
| 3x10s isometric lean with no cramping | Assisted eccentric. |
| 2x4 with 5-second controlled lowering | Reduce assistance. |
| 3x5 full eccentrics with control | Add partial concentric. |
| Hamstring pain or cramping | Regress to bridge isometric or slider curl. |

### Ankle Stiffness

| Gate | Next Step |
|---|---|
| 20 bilateral pogos with no heel collapse | Add reps. |
| 30 clean bilateral pogos | Add low-volume single-leg pogos. |
| Single-leg pogos clean and pain-free | Add sport/skill-specific footwork. |
| Achilles or patellar soreness | Return to tibialis/soleus only and retest. |

### Stability Ball Core / Rehab

| Gate | Next Step |
|---|---|
| Ball crunch 2x12 with no neck pulling or low-back irritation | Add 1-2 reps per set until 2x20. |
| Stir-the-pot 2x8 circles each direction with no lumbar sag | Add circles or move feet slightly farther back. |
| Stability ball hamstring curl 2x10 with hips level | Progress to slower eccentric or single-leg eccentric. |
| Any back pinch, neck strain, or hip cramping | Regress to dead bug, glute bridge, or static plank. |

### Recomp Block

Advance to strength/specialization if:

- Bodyweight or waist trend moves in the desired direction.
- Strength is stable or improving.
- Protein adherence is consistent.
- Recovery markers are not deteriorating.
- Pain is stable or improved.

Repeat recomp if:

- Body comp changes are absent but adherence was poor.
- Strength and recovery are stable.
- User still wants body composition as the primary goal.

Pivot out of recomp if:

- Recovery is worsening despite adherence.
- Calories are too low to support training.
- Strength is dropping across multiple patterns.

## Intra-Phase Intensity Wave

Every 3–4 week loading phase follows the same intensity pattern regardless of block type. This is the week-by-week RPE and RIR target that tells the athlete how hard to push *this specific week* — separate from the phase-to-phase advancement gates.

### The Wave

| Week in Phase | Label | RPE Target | RIR Target | Volume | Intent |
|---|---|---|---|---|---|
| Week 1 | Intro load | 6–7 | 4–5 | 90% of target | Technique first. Form should feel easy. Leave a lot in the tank. |
| Week 2 | Moderate load | 7–8 | 2–4 | 100% of target | Push to moderate effort. Last rep should feel challenging but clean. |
| Week 3 | Peak load | 8–9 | 1–2 | 105–110% of target | The hardest week of the phase. Last rep requires full intent. |
| Week 4 | Deload / Test | 4–5 | 6+ | 50% of target | Consolidation week. Not a rest week — a measurement week. |

### How It Renders in the App

Each daily session header shows a badge pulled from this table:

> **This week: Moderate load · RPE 7–8 · RIR 2–4**

This badge is calculated from `current_week_in_phase` in the config. It applies to every working set — the athlete does not need to track percentages or calculate loads. They use RIR as the primary autoregulation tool: if the set ends and they had 4+ reps in reserve, add a rep or increase load next session.

### Explosive and Skill Work — Different Scale

Explosive movements (jump squat complex, KB swing, pogo) and skill work (boxing, salsa, Tai Chi) do not use RPE/RIR. They use a 3-point quality scale:

| Label | Meaning |
|---|---|
| Quality 1 — Pattern | Focus is form, timing, and control. Effort is never the goal. |
| Quality 2 — Expression | Pattern is automatic. Push power or precision within form limits. |
| Quality 3 — Performance | Full output. Used only when pattern is solid and readiness is Green. |

Explosive work escalates quality level by phase, not by week-in-phase — the pattern must be owned before power is added.

### Warm-Up Ramp Sets

Every primary compound exercise (pull-up, goblet squat, Bulgarian split squat, ring push-up, RDL) gets 1–2 ramp-up sets before working sets. Ramp sets are not logged as working volume.

| Ramp set | Load | Reps | Intent |
|---|---|---|---|
| Ramp 1 | ~50% of working weight (or bodyweight if the working set uses bodyweight + vest) | 5 | Feel the pattern. Confirm joint readiness. |
| Ramp 2 | ~75–80% of working weight | 3–4 | Prime the neuromuscular path. Stop 6+ RIR. |

Ramp sets come after the activation sequence (mobility unlock + neural prime from exercises.md) and before the first logged working set. Total ramp time: 2–3 minutes per primary exercise. For days with multiple primary exercises, ramp only the first exercise of each pattern — subsequent exercises in the same pattern inherit the neural prime from the first.

### Time Budget

| Block | Duration |
|---|---|
| Ankle stiffness block (every session) | 4 min |
| Activation sequence + ramp sets (first primary exercise) | 4–5 min |
| Working sets | 42–50 min |
| Post-session log | 2 min |
| **Total** | **≤ 60 min** |

The warm-up budget is 8–9 minutes total. It does not inflate the session because the ankle block was already in the program. The activation sequence and ramp sets replace the generic "3 sets at 50% load" that athletes were already doing intuitively — it just makes them deliberate and muscle-specific.

---

## Override Log

When overriding a recommendation, record:

- System recommendation.
- Chosen action.
- Reason.
- Risk accepted.
- Date to review the override.
