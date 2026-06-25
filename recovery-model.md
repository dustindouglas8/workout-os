# Recovery Model

## Purpose

The recovery model decides how much training a user can productively absorb. It prevents Workout OS from treating Dustin's recovery needs as universal while still supporting users who need a recovery-biased program.

## Recovery Bias Levels

| Level | Use When | Programming Effect |
|---|---|---|
| Recovery-biased | Sleep is poor, pain is active, training age is low, stress is high, or readiness trends down. | Lower volume, fewer hard days, longer warm-ups, more frequent deloads, stricter Yellow/Red rules. |
| Standard | User has stable sleep, manageable soreness, and consistent training history. | Default block structure and normal readiness thresholds. |
| Performance-biased | User has strong recovery markers, high training age, and low pain. | Slightly more volume, more specialization, and harder top-end work. |

## Inputs

Recovery bias is selected from:

- Sleep average and sleep variability.
- Resting heart rate or HRV trend.
- Current pain and active injury status.
- Training age and recent consistency.
- Life stress and travel frequency.
- Weekly readiness trend.
- Session RPE trend.
- Missed or modified workouts.
- Nutrition sufficiency, especially protein and total calories.

## Default Selection Rules

Start **Recovery-biased** if any of these are true:

- Current pain is above 3/10 during daily life or training.
- Sleep averages below 6.5 hours for two consecutive weeks.
- RHR is 5+ bpm above baseline for three or more days.
- Training consistency has been below 3 days/week for the last month.
- User is returning after injury, illness, or a long layoff.
- Travel is weekly or sleep during travel is highly variable.

Start **Performance-biased** only if all of these are true:

- Sleep averages 7+ hours.
- Pain is 0-2/10 and not worsening.
- Training consistency has been stable for at least 8 weeks.
- User passes movement screens for the planned block.
- Readiness is Green on most training days.

Otherwise start **Standard**.

## Effects By Program Area

| Area | Recovery-Biased | Standard | Performance-Biased |
|---|---|---|---|
| Weekly hard days | 1-2 | 2-3 | 3 |
| Session cap | 30-45 min | 45-60 min | 60-75 min |
| Accessory volume | Minimal | Moderate | Moderate-high |
| Deload cadence | Every 3-4 weeks or auto-triggered | Every 4 weeks | Every 4-6 weeks if markers stay stable |
| Yellow day | Drop accessories and reduce compounds | Drop accessories, reduce one set | Reduce load or top set only |
| Red day | Rehab/prehab + walk only | Rehab/prehab + mobility/walk | Same as Standard |
| Progression speed | Slower gates | Normal gates | Faster only if tests pass |

## Daily Readiness

Readiness is checked before training, not before the morning rehab/prehab session.

Inputs:

- Sleep last night.
- RHR or HRV versus baseline.
- Joint pain and stiffness.
- Energy.
- Motivation/focus.
- Optional soreness and stress.

Outputs:

- **Green:** train as planned.
- **Yellow:** preserve the main pattern, reduce volume/load, drop accessories.
- **Red:** skip main session; perform recovery session only.

## Trend Rules

Single-day readiness changes the day. Multi-day trends change the program.

- Three Yellow days in seven days: reduce accessory volume for the next week.
- Two Red days in seven days: unscheduled deload or recovery week.
- Pain increases for two consecutive sessions in the same pattern: regress that pattern.
- RHR/HRV trend worsens for one week: lower intensity until baseline returns.
- Performance drops in two unrelated benchmarks: repeat the current phase or deload.

## Recovery Logs

The log must capture enough data to explain adjustments:

- Daily readiness color.
- Sleep hours.
- RHR/HRV if available.
- Pain location and score.
- Session RPE.
- Completed, modified, or skipped.
- Notes on travel, stress, illness, or poor nutrition.

## Guardrails

- Recovery-biased does not mean easy forever. It means the program earns intensity through stable markers.
- Performance-biased does not override Red days.
- Active injury changes exercise selection before it changes effort language.
- Medical symptoms, unexplained sharp pain, chest pain, fainting, or neurological symptoms require referral out, not program modification.
