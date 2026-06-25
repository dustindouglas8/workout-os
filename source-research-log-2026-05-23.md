# Source Research Log — 2026-05-23

## Scope

Purpose: choose exercise cue/video sources for Workout OS before regenerating the HTML.

Current generated files found in `/Users/Veritas/Downloads`:
- `dustin_training_os_v5.html`
- `dustin_training_os_v6.html`

The current generated app should not keep generic links like `View on MuscleWiki`. Exercise media must be resolved through `exercise-media-map.md`.

---

## Sources Reviewed

| Source | URL | Decision |
|---|---|---|
| Fitbod Exercise Pages | https://fitbod.me/exercises | Good candidate for common strength exercises with exact pages. Use per-exercise URLs only. |
| Fitbod Pull-Up | https://fitbod.me/exercises/pull-up | Candidate exact match for `pull_up_strict`; local hollow-body cue still overrides. |
| Fitbod Kettlebell Goblet Squat | https://fitbod.me/exercises/goblet-squat | Candidate exact match for `kb_goblet_squat`. |
| Fitbod Ring Row | https://fitbod.me/exercises/ring-row | Candidate exact match for `ring_row`. |
| Fitbod Ring Dip | https://fitbod.me/exercises/ring-dip | Candidate exact match for `ring_dip`. |
| Fitbod Romanian Deadlift | https://fitbod.me/exercises/romanian-deadlift | Close variant only for `kb_romanian_deadlift`; not exact KB demo. |
| Fitbod Dumbbell Bulgarian Split Squat | https://fitbod.me/exercises/dumbbell-bulgarian-split-squat | Close variant only for `kb_bulgarian_split_squat`. |
| Fitbod Kettlebell Front Squat | https://fitbod.me/exercises/kettlebell-front-squat | Candidate exact match for `kb_front_squat`. |
| Fitbod Dual Kettlebell Front Squat | https://fitbod.me/exercises/dual-kettlebell-front-squat | Candidate exact match for dual-KB front squat variants. |
| Fitbod Kettlebell Swing | https://fitbod.me/exercises/kettlebell-swing | Candidate exact match for `kb_swing`; close variant for dead-stop swing. |
| Fitbod Push Press | https://fitbod.me/exercises/push-press | Close variant only for `kb_push_press`; source is barbell push press. |
| Fitbod Dead Hang | https://fitbod.me/exercises/dead-hang | Candidate exact match for `dead_hang`; close variant for towel hang. |
| Fitbod DB Curl | https://fitbod.me/exercises/dumbbell-bicep-curl | Candidate exact match for `db_curl`. |
| Fitbod DB Lateral Raise | https://fitbod.me/exercises/dumbbell-lateral-raise | Candidate exact match for `db_lateral_raise`. |
| Fitbod DB Back Fly | https://fitbod.me/exercises/dumbbell-back-fly | Close variant for `db_rear_delt_fly`; source appears chest-supported/incline-oriented. |
| Fitbod Floor Press | https://fitbod.me/exercises/floor-press | Close variant for `db_floor_press`; verify exact DB page later. |
| Fitbod Push-Up | https://fitbod.me/exercises/push-up | Candidate exact match for base push-up and close variant fallback for ring/decline variants. |
| NASM Exercise Library | https://www.nasm.org/exercise-library | Good authority source for exercise and stretch instructions. Use exact page URLs where available. |
| NASM Dead Bug | https://www.nasm.org/resource-center/exercise-library/dead-bug | Candidate exact match for `dead_bug`. |
| NASM Floor Bridge | https://www.nasm.org/resource-center/exercise-library/floor-bridge | Candidate exact match for `glute_bridge` under NASM naming. |
| NASM Glute Bridge Article | https://blog.nasm.org/how-to-do-a-glute-bridge | Related cue source for bridge setup and common mistakes. |
| NASM Stretches for Beginners | https://blog.nasm.org/stretches-for-beginners | Related cue source for kneeling hip flexor stretch. |
| NASM Dynamic Stretching | https://blog.nasm.org/dynamic-stretching | Warm-up sequencing reference, not direct per-exercise media. |
| ACE Exercise Library | https://www.acefitness.org/resources/everyone/exercise-library/video/ | Good public source, but use exact exercise pages/videos only. |
| ACE Dynamic Warm-Up PDF | https://www.acefitness.org/certifiednews/images/article/pdfs/Dynamic.pdf | Useful for warm-up drill cue validation. |
| PlainExercise | https://plainexercise.com | Good text/cue fallback, no video. |
| ExerciseDB OSS | https://oss.exercisedb.dev/docs | Structured exercise/GIF source; verify license/attribution before embedding. |
| EDB Exercise Intelligence | https://exercisedb.io/ | Best app-ready dataset candidate if paid source is acceptable. |
| Wrkout API | https://wrkout.xyz/ | Media-rich API candidate; verify pricing/terms. |
| Virtuagym Exercise Library | https://exercises.virtuagym.com/ | Broad free video fallback; exact URL review needed per exercise. |

---

## Decisions

1. Use `exercise-media-map.md` as the canonical mapping file.
2. Do not render generic provider links in active workout cards.
3. Keep local Workout OS cues as the primary coaching layer.
4. Use external media as supporting demonstration only when exact and reviewed.
5. Safety-sensitive movements stay `Media pending` until an exact, reviewed source is chosen.
6. Timed mobility drills need local cue definitions more than external links.

---

## Before Next HTML Rebuild

- Remove generic MuscleWiki-style links from warm-up cards.
- Add media resolution step: `exercise ID -> exercise-media-map.md -> reviewed source or media pending`.
- Show source/provider labels in Exercise Library.
- In the active workout flow, show only one primary media action per exercise.
- Keep source research and mapping changes in this log or a dated successor log.

---

## Generated Output

- Created `/Users/Veritas/Downloads/dustin_training_os_v7.html` from the current v6 HTML.
- Replaced generic MuscleWiki links with media-map based rendering.
- Added bottom-docked rest timer behavior so the user can keep scrolling during rest.
- Added set-load carry-forward: Set 2+ defaults to the most recent saved load from the same exercise.
- Clarified Saturday timed mobility prescriptions for pike and pancake work with total-duration language.
- Changed morning rehab controls from manual phase/day selectors to inferred context labels from Settings and Today.
- Added expandable ramp-set cue cards with purpose, dose, setup, execution, adjustment rule, and media-map actions.

Verification:
- `rg` found no remaining `MuscleWiki`, `musclewiki`, or `View on` strings in v7.
- Node syntax check passed for the embedded JavaScript.
