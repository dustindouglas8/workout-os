# Exercise Media Map

## Purpose

This is the canonical mapping between Workout OS exercise IDs and external cue/video/media sources.

The generated HTML must use this file when rendering exercise media links. It must not generate generic provider links such as `View on MuscleWiki` unless the URL points to the exact mapped exercise page.

If an exercise has no exact or approved source, the app shows local cues from `exercises.md` and the label `Media pending`.

---

## Source Registry

| Provider | Base URL | Use | Status | Notes |
|---|---|---|---|---|
| Fitbod Exercise Pages | https://fitbod.me/exercises | Common strength exercise videos and written instructions | candidate | Good for common strength movements; verify exact URL and equipment match per exercise. |
| NASM Exercise Library | https://www.nasm.org/exercise-library | Corrective, mobility, stretch, and common movement instructions | candidate | Good authority source. Some exact exercise pages exist; others are article-level. |
| ACE Exercise Library | https://www.acefitness.org/resources/everyone/exercise-library/video/ | Public exercise and warm-up education | candidate | Use for common exercises and warm-up education. |
| ACE Dynamic Warm-Up PDF | https://www.acefitness.org/certifiednews/images/article/pdfs/Dynamic.pdf | Warm-up drill cue validation | candidate | Use for warm-up logic and neuromuscular readiness drills, not exact exercise demos. |
| PlainExercise | https://plainexercise.com | Structured written cues, common mistakes, equipment notes | candidate | Good cue fallback; no video. |
| ExerciseDB OSS | https://oss.exercisedb.dev/docs | Structured exercise/GIF dataset | candidate | Check license/attribution before embedding or bundling media. |
| EDB Exercise Intelligence | https://exercisedb.io/ | App-ready structured dataset with GIFs, substitutions, progressions/regressions | candidate | Best paid/data-product option if we want durable app-level source coverage. |
| Wrkout API | https://wrkout.xyz/ | Exercise API with images/video/audio | candidate | Check pricing/API terms before dependency. |
| Virtuagym Exercise Library | https://exercises.virtuagym.com/ | Broad free video library by muscle/equipment | candidate | Useful fallback for common movements; exact URL review required. |

---

## Status Values

| Status | Meaning |
|---|---|
| missing | No useful media source found yet. |
| candidate | Source found, but not yet human-reviewed. |
| needs_review | Likely correct but needs visual/form review before approval. |
| approved | Correct movement, correct context, acceptable source. |
| rejected | Wrong movement, poor cueing, unstable URL, or bad licensing fit. |

## Match Values

| Match | Meaning |
|---|---|
| exact | Same movement and same equipment/context. |
| close_variant | Same pattern, different equipment or setup. |
| related | Useful cue/reference source, but not an exact demo. |
| missing | No source. |

---

## Initial High-Priority Mapping

These are the first records to resolve before the next HTML rebuild because they appear in Dustin's current week or in high-frequency warm-up/prehab blocks.

| Workout OS ID | Display Name | Status | Primary Source | Match | App Rendering Instruction | Notes |
|---|---|---|---|---|---|---|
| `ring_push_up` | Ring Push-Up | missing |  | missing | Show `Media pending`; use local cues. | Do not map to generic push-up unless labeled close variant. |
| `ring_fly` | Ring Fly | missing |  | missing | Show `Media pending`; use local cues. | Needs exact ring context or custom demo. |
| `slider_chest_fly` | Slider Chest Fly | missing |  | missing | Show `Media pending`; use local cues. | Common libraries may not have exact slider version. |
| `archer_push_up` | Archer Push-Up | missing |  | missing | Show `Media pending`; use local cues. | Exact calisthenics source needed. |
| `kb_push_press` | KB Push Press | needs_review | https://fitbod.me/exercises/push-press | close_variant | Label close variant; local kettlebell rack cue stays primary. | Fitbod page is barbell push press, not exact KB. |
| `decline_ring_push_up` | Decline Ring Push-Up | missing |  | missing | Show `Media pending`; use local cues. | Generic decline push-up is close variant only. |
| `band_external_rotation` | Band External Rotation | candidate | NASM / ACE exact page to verify | exact | Candidate only. | High-frequency prehab; needs clean shoulder cueing. |
| `ring_dip` | Ring Dip | needs_review | https://fitbod.me/exercises/ring-dip | exact | Candidate display after review. | Exact ring context. |
| `ring_row` | Ring Row | needs_review | https://fitbod.me/exercises/ring-row | exact | Candidate display after review. | Fitbod has exact ring row page. |
| `kb_single_arm_row` | KB Single-Arm Row | candidate | Fitbod / Virtuagym exact page to verify | close_variant | Use local cues until kettlebell exact URL is verified. | Dumbbell row source is close variant only. |
| `kb_romanian_deadlift` | KB Romanian Deadlift | needs_review | https://fitbod.me/exercises/romanian-deadlift | close_variant | Label as close variant if shown; local cues remain primary. | Fitbod page is barbell RDL; OK for hinge concept, not exact KB demo. |
| `pull_up_strict` | Pull-Up Strict | needs_review | https://fitbod.me/exercises/pull-up | exact | Candidate display after review. | Exact enough for strict pull-up; Workout OS hollow-body cue stays local. |
| `kb_goblet_squat` | KB Goblet Squat | needs_review | https://fitbod.me/exercises/goblet-squat | exact | Candidate display after review. | Exact movement. |
| `kb_front_squat` | KB Front Squat | needs_review | https://fitbod.me/exercises/kettlebell-front-squat | exact | Candidate display after review. | Exact enough; verify single vs dual KB wording. |
| `dual_kb_front_squat` | Dual KB Front Squat | needs_review | https://fitbod.me/exercises/dual-kettlebell-front-squat | exact | Candidate display after review. | Use if generated program specifies two kettlebells. |
| `kb_bulgarian_split_squat` | KB Bulgarian Split Squat | needs_review | https://fitbod.me/exercises/dumbbell-bulgarian-split-squat | close_variant | Label close variant; local KB setup cue stays primary. | Dumbbell version maps mechanics, not exact load. |
| `kb_swing` | KB Swing | needs_review | https://fitbod.me/exercises/kettlebell-swing | exact | Candidate display after review. | Use for `KB Swing dead stop` as close variant because dead-stop reset differs. |
| `single_arm_kb_swing` | Single-Arm KB Swing | needs_review | https://fitbod.me/exercises/single-arm-kettlebell-swing | exact | Candidate display after review. | Not currently primary but useful variant. |
| `nordic_hamstring_eccentric` | Nordic Hamstring Eccentric | missing |  | missing | Show `Media pending`; use local cues and contraindications. | Safety-sensitive; do not use random source. |
| `jefferson_curl` | Jefferson Curl | missing |  | missing | Show `Media pending`; use local cues and contraindications. | Safety-sensitive; exact source required before video display. |
| `skin_the_cat` | Skin the Cat | missing |  | missing | Show `Media pending`; use local cues and contraindications. | Ring-skill-specific; likely needs custom or expert-reviewed source. |
| `hip_flexor_kneeling_stretch` | Hip Flexor Kneeling Stretch | needs_review | https://blog.nasm.org/stretches-for-beginners | related | Use as cue validation, not exact demo link unless the generated UI labels it article/reference. | NASM article includes kneeling hip flexor stretch instructions. |
| `pogo_hop` | Pogo Hop | candidate | ACE Dynamic Warm-Up PDF | related | Use as warm-up reference only; local cues primary. | Dynamic warm-up source includes plyometric readiness drills, not necessarily pogo exact. |
| `dead_bug` | Dead Bug | needs_review | https://www.nasm.org/resource-center/exercise-library/dead-bug | exact | Candidate display after review. | Exact page with video and common mistakes. |
| `glute_bridge` | Glute Bridge | needs_review | https://www.nasm.org/resource-center/exercise-library/floor-bridge | exact | Candidate display after review. | NASM names it Floor Bridge; exact bodyweight bridge pattern. |
| `glute_bridge_article` | Glute Bridge Article | needs_review | https://blog.nasm.org/how-to-do-a-glute-bridge | related | Use as cue validation, not primary demo if exact page is used. | Good form/cue context. |
| `lateral_band_walk` | Lateral Band Walk | candidate | NASM / ACE exact page to verify | exact | Candidate only. | Needs band placement cue review. |
| `scapular_pull_up` | Scapular Pull-Up | missing |  | missing | Show `Media pending`; use local cues. | Exact movement matters; do not map to full pull-up. |
| `band_pull_apart` | Band Pull-Apart | candidate | ACE Dynamic Warm-Up PDF | exact | Candidate reference after review. | ACE PDF includes band dislocations; verify if using pull-apart separately. |
| `pike_stretch` | Pike Stretch | missing |  | missing | Show local cues only; must display total duration definition. | Current program needs active/passive sequence clarified. |
| `pancake_stretch` | Pancake Stretch | missing |  | missing | Show local cues only; must display total duration definition. | Current program needs holds/rounds clarified. |
| `dead_hang` | Dead Hang | needs_review | https://fitbod.me/exercises/dead-hang | exact | Candidate display after review. | Exact hang source; Workout OS decompression/grip cue stays local. |
| `db_curl` | DB Curl | needs_review | https://fitbod.me/exercises/dumbbell-bicep-curl | exact | Candidate display after review. | Generated as `DB Curl pyramid`; source is base curl. |
| `db_lateral_raise` | DB Lateral Raise | needs_review | https://fitbod.me/exercises/dumbbell-lateral-raise | exact | Candidate display after review. | Exact movement. |
| `db_rear_delt_fly` | DB Rear Delt Fly | needs_review | https://fitbod.me/exercises/dumbbell-back-fly | close_variant | Label close variant; local hip-hinge rear delt cue stays primary. | Fitbod page is chest-supported/incline-leaning back fly. |
| `db_floor_press` | DB Floor Press | needs_review | https://fitbod.me/exercises/floor-press | close_variant | Label close variant unless exact dumbbell floor press page is found. | Fitbod page is floor press, mostly barbell text with DB alternative. |
| `push_up_standard` | Push-Up | needs_review | https://fitbod.me/exercises/push-up | exact | Candidate display after review. | Useful fallback for push-up variants. |
| `scapular_push_up` | Scapular Push-Up | candidate | https://fitbod.me/exercises/scapular-push-up | exact | Candidate only; verify exact URL and no-elbow-bend cue. | Used in warm-up F-series and morning circuit. |
| `push_up_plus` | Push-Up Plus | candidate | https://fitbod.me/exercises/push-up-plus | exact | Candidate only; verify protraction cue at top. | Used Monday warm-up. Serratus prime. |
| `wall_slide` | Wall Slide | candidate | https://fitbod.me/exercises/wall-slide | exact | Candidate only; verify elbows-on-wall cue present. | Used Monday/Friday warm-up. Lower trap + serratus. |
| `shoulder_cars` | Shoulder CARs | missing |  | missing | Show `Media pending`; use local cues. | FRC-style exercise. No standard library coverage — needs custom or Kinstretch-source video. |
| `hip_cars` | Hip CARs | missing |  | missing | Show `Media pending`; use local cues. | FRC-style exercise. Pelvis-level cue is the critical differentiator. |
| `neck_cars` | Neck CARs | missing |  | missing | Show `Media pending`; use local cues. | Safety-sensitive — any sharp/radiating sensation is a stop cue. No standard library source. |
| `ankle_cars` | Ankle CARs | missing |  | missing | Show `Media pending`; use local cues. | FRC-style. Distinguish from passive ankle roll — active control throughout. |
| `hip_circle` | Hip Circle | candidate | https://fitbod.me/exercises/hip-circles | exact | Candidate only; verify large-range standing version. | Used Tuesday Zone 2 + Friday skill warm-up. |
| `worlds_greatest_stretch` | World's Greatest Stretch | candidate | https://fitbod.me/exercises/worlds-greatest-stretch | exact | Candidate only; verify lunge + rotation sequence present. | Used Tuesday Zone 2 warm-up. |
| `cat_cow` | Cat-Cow | candidate | https://fitbod.me/exercises/cat-cow | exact | Candidate only; verify full spinal range (not neck-only). | Saturday R1 across all phases. |
| `hip_90_90` | 90/90 Hip Stretch | candidate | https://fitbod.me/exercises/90-90-hip-stretch | exact | Candidate only; verify both IR and ER discussed. | Saturday warm-up + R2 Phase 2+. |
| `thoracic_rotation` | Thoracic Rotation | candidate | https://fitbod.me/exercises/thoracic-rotation | exact | Candidate only; verify movement from thoracic (not lumbar) cue. | Saturday + Tuesday warm-up. |
| `pigeon_prep` | Pigeon Prep | candidate | https://fitbod.me/exercises/pigeon-pose | close_variant | Label close variant — Fitbod page is full pigeon; program uses prep only. | Saturday warm-up. |
| `supine_knee_to_chest` | Supine Knee-to-Chest | candidate | https://www.nasm.org/resource-center/exercise-library/knee-to-chest | exact | Candidate only; verify NASM exact page exists. | Saturday warm-up spinal prep and night recovery. |
| `seated_forward_fold` | Seated Forward Fold | missing |  | missing | Show `Media pending`; use local cues. | Saturday warm-up pre-Jefferson curl spinal prep. Safety context: progression to Jefferson curl. |
| `supine_spinal_twist` | Supine Spinal Twist | candidate | https://www.nasm.org/resource-center/exercise-library/supine-spinal-twist | exact | Candidate only; verify NASM exact page exists. | Phase 3 Saturday R2 and night recovery Movement 5. |
| `ankle_roll` | Ankle Roll | missing |  | missing | Show `Media pending`; use local cues. | Ankle warm-up and used in tibialis raise activation sequence. Passive version; no standard library source. |
| `single_leg_soleus_raise` | Single-Leg Soleus Raise | candidate | https://fitbod.me/exercises/single-leg-calf-raise | close_variant | Label close variant — source is calf raise; soleus emphasis requires bent-knee cue from local library. | F4 morning circuit + ankle stiffness block. |
| `physiological_sigh` | Physiological Sigh | missing |  | missing | Show local cues only. No video source. | Night recovery Movement 1. Breathing regulation, not an exercise. No appropriate library source. |
| `supine_thoracic_release` | Supine Thoracic Release | missing |  | missing | Show local cues only. No video source. | Night recovery Movement 3. Equipment: foam roller. No standard library source covers 2-minute gravity protocol. |
| `exhale_only_supine_reset` | Exhale-Only Supine Reset | missing |  | missing | Show local cues only. No video source. | Night recovery Movement 4. Intentionally not a training exercise — no media appropriate. |
| `crocodile_breathing` | Crocodile Breathing | missing |  | missing | Show local cues only. No video source. | Night recovery Movement 6. Breathing regulation in prone. No standard library source. |
| `four_seven_eight_breath` | 4-7-8 Breath | missing |  | missing | Show local cues only. No video source. | Night recovery Movement 7 (final before sleep). Technique from Dr. Weil / pranayama. No video needed — audio cue or text only. |

---

## Current Generated Program Alias Map

Generated HTML labels may include protocols, combinations, holds, or phase variants. The generator should resolve these labels to the base mapped exercise below.

| Generated Label | Resolve To | Match | Rendering Instruction |
|---|---|---|---|
| `Band external rotation` | `band_external_rotation` | exact | Use mapped record if approved; otherwise local cues. |
| `Hip flexor kneeling stretch` | `hip_flexor_kneeling_stretch` | exact | Use local cues plus NASM related reference. |
| `Hip flexor kneeling stretch + posterior tilt` | `hip_flexor_kneeling_stretch` | exact | Local posterior-tilt cue overrides source. |
| `Dead bug` | `dead_bug` | exact | Use NASM source after review. |
| `Dead bug — exhale each rep` | `dead_bug` | exact | Local exhale cue overrides source. |
| `Dead bug + perturbation hold` | `dead_bug` | close_variant | Label as variant; local cue primary. |
| `Dead bug + 5lb DB press` | `dead_bug` | close_variant | Label as variant; local cue primary. |
| `Tibialis raise` | `tibialis_raise` | missing | Local cues only. |
| `Tibialis raise + single-leg calf raise` | `tibialis_raise` + `single_leg_soleus_raise` | combined | Local cues only; do not show one generic source. |
| `Single-leg soleus raise` | `single_leg_soleus_raise` | missing | Local cues only. |
| `Pogo hop` | `pogo_hop` | related | Local cues primary. |
| `Pogo + stick landing` | `pogo_hop` | close_variant | Local cues primary. |
| `Glute bridge` | `glute_bridge` | exact | Use NASM Floor Bridge after review. |
| `Glute bridge + knee drive` | `glute_bridge` | close_variant | Local cue primary. |
| `Single-leg glute bridge + 2s pause` | `glute_bridge` | close_variant | Label variant. |
| `Single-leg glute bridge + 20lb KB` | `glute_bridge` | close_variant | Label loaded variant. |
| `Lateral band walk` | `lateral_band_walk` | exact | Candidate only until exact source verified. |
| `Band pull-apart` | `band_pull_apart` | exact | Candidate only; verify exact source. |
| `Band pull-apart + ER combo` | `band_pull_apart` + `band_external_rotation` | combined | Local cues only unless both sources approved. |
| `Scapular pull-up` | `scapular_pull_up` | missing | Local cues only. |
| `Scapular pull-up + 2s hold` | `scapular_pull_up` | close_variant | Local cues only. |
| `Scapular push-up` | `scapular_push_up` | missing | Local cues only. |
| `Dead hang` | `dead_hang` | exact | Use Fitbod source after review. |
| `Dead hang grip` | `dead_hang` | close_variant | Local grip cue primary. |
| `Active hang + shoulder pack` | `dead_hang` | close_variant | Local active-pack cue primary. |
| `Active hang + hollow body vacuum` | `dead_hang` | close_variant | Local hollow/vacuum cue primary. |
| `Active hang → tuck → skin the cat` | `skin_the_cat` | close_variant | Local cues only; safety-sensitive. |
| `Ring Push-Up` | `ring_push_up` | missing | Media pending. |
| `Decline Ring Push-Up` | `decline_ring_push_up` | missing | Media pending. |
| `Ring Fly` | `ring_fly` | missing | Media pending. |
| `Archer Push-Up` | `archer_push_up` | missing | Media pending. |
| `Ring Dip` | `ring_dip` | exact | Use Fitbod source after review. |
| `Ring Row (horizontal pull)` | `ring_row` | exact | Use Fitbod source after review. |
| `Pull-Up` | `pull_up_strict` | exact | Use Fitbod source after review. |
| `Pull-Up (strict hollow body)` | `pull_up_strict` | exact | Local hollow-body cue overrides source. |
| `KB Goblet Squat` | `kb_goblet_squat` | exact | Use Fitbod source after review. |
| `Jump squat → KB goblet squat complex` | `kb_goblet_squat` | close_variant | Local complex cue primary. |
| `KB Front Squat` | `kb_front_squat` | exact | Use Fitbod source after review. |
| `KB Bulgarian Split Squat` | `kb_bulgarian_split_squat` | close_variant | Label DB source as close variant. |
| `KB Romanian Deadlift` | `kb_romanian_deadlift` | close_variant | Label barbell RDL source as close variant. |
| `KB Single-Arm Row` | `kb_single_arm_row` | close_variant | Local cue primary until exact KB row source found. |
| `KB Swing dead stop` | `kb_swing` | close_variant | Label variant; local dead-stop cue primary. |
| `KB Push Press` | `kb_push_press` | close_variant | Label barbell source as close variant. |
| `KB Suitcase Carry` | `kb_suitcase_carry` | missing | Local cues only. |
| `KB Woodchop high-to-low` | `kb_woodchop` | missing | Local cues only. |
| `KB Rotational Lunge` | `kb_rotational_lunge` | missing | Local cues only. |
| `Nordic hamstring curl (eccentric)` | `nordic_hamstring_eccentric` | missing | Safety-sensitive; media pending. |
| `Slider Hamstring Curl` | `slider_hamstring_curl` | missing | Local cues only. |
| `Slider Adductor Slide` | `slider_adductor_slide` | missing | Local cues only. |
| `Slider Lateral Lunge` | `slider_lateral_lunge` | missing | Local cues only. |
| `Slider Chest Fly` | `slider_chest_fly` | missing | Local cues only. |
| `Jefferson Curl` | `jefferson_curl` | missing | Safety-sensitive; media pending. |
| `Pike stretch (active + passive)` | `pike_stretch` | missing | Local cues only; total duration required. |
| `Pancake stretch` | `pancake_stretch` | missing | Local cues only; total duration required. |
| `Skin the Cat (rings)` | `skin_the_cat` | missing | Safety-sensitive; media pending. |
| `Shoulder dislocate` | `shoulder_dislocate` | related | Use ACE warm-up source only as reference unless exact source found. |
| `Shoulder CAR` | `shoulder_cars` | missing | Local cues only. FRC-style — no standard library. |
| `Shoulder CARs` | `shoulder_cars` | missing | Local cues only. FRC-style — no standard library. |
| `Wrist + shoulder CARs` | `wrist_cars` + `shoulder_cars` | combined | Local cues only. |
| `Neck CAR` | `neck_cars` | missing | Local cues only. Safety-sensitive — stop on any sharp/radiating sensation. |
| `Neck CARs` | `neck_cars` | missing | Local cues only. Safety-sensitive. |
| `Hip CAR` | `hip_cars` | missing | Local cues only. Pelvis-level cue is critical. |
| `Hip CARs` | `hip_cars` | missing | Local cues only. |
| `Ankle CAR` | `ankle_cars` | missing | Local cues only. Distinguish from passive ankle roll. |
| `Ankle CARs` | `ankle_cars` | missing | Local cues only. |
| `Scapular push-up` | `scapular_push_up` | candidate | Fitbod candidate — verify no-elbow-bend cue. |
| `Push-up plus` | `push_up_plus` | candidate | Fitbod candidate — verify protraction at top. |
| `Wall slide` | `wall_slide` | candidate | Fitbod candidate — verify elbows-on-wall cue. |
| `90/90 hip stretch` | `hip_90_90` | candidate | Fitbod candidate — verify IR + ER both addressed. |
| `90/90 hip internal rotation` | `hip_90_90` | close_variant | Local cues only. |
| `90/90 PAILs + RAILs` | `hip_90_90` | close_variant | Local FRC-style cue primary. |
| `90/90 flow IR + ER alternating` | `hip_90_90` | close_variant | Local cues only. |
| `World's greatest stretch` | `worlds_greatest_stretch` | candidate | Fitbod candidate — verify lunge + rotation sequence. |
| `Thoracic rotation` | `thoracic_rotation` | candidate | Fitbod candidate — verify thoracic (not lumbar) origin cue. |
| `Thread-the-needle` | `thread_the_needle` | missing | Local cues only. |
| `Cat-cow` | `cat_cow` | candidate | Fitbod candidate — verify full spinal range. |
| `Cat-cow + thoracic rotation` | `cat_cow` + `thoracic_rotation` | combined | Local cues only. |
| `Segmental cat-cow` | `cat_cow` | close_variant | Local cues only. |
| `Pigeon prep` | `pigeon_prep` | candidate | Fitbod full pigeon as close variant — program uses prep only. |
| `Supine knee-to-chest` | `supine_knee_to_chest` | candidate | NASM candidate — verify exact page exists. |
| `Seated forward fold` | `seated_forward_fold` | missing | Local cues only. Pre-Jefferson curl spinal prep. |
| `Supine spinal twist` | `supine_spinal_twist` | candidate | NASM candidate — verify exact page exists. |
| `Ankle roll` | `ankle_roll` | missing | Local cues only. Passive ankle mobility. |
| `Hip circle` | `hip_circle` | candidate | Fitbod candidate — verify large-range standing version. |
| `Physiological sigh` | `physiological_sigh` | missing | Local cues only. Breathing regulation — no media appropriate. |
| `Physiological Sigh × 2–3` | `physiological_sigh` | missing | Local cues only. |
| `Supine thoracic release` | `supine_thoracic_release` | missing | Local cues only. Equipment: foam roller. 2-minute gravity protocol. |
| `Exhale-only supine reset` | `exhale_only_supine_reset` | missing | Local cues only. Not a training exercise — no media appropriate. |
| `Exhale-Only Supine Reset × 6/side` | `exhale_only_supine_reset` | missing | Local cues only. |
| `Crocodile breathing` | `crocodile_breathing` | missing | Local cues only. Prone diaphragmatic regulation. |
| `4-7-8 breathing` | `four_seven_eight_breath` | missing | Local cues only. Text/audio cue only — no video needed. |
| `4-7-8 Breath` | `four_seven_eight_breath` | missing | Local cues only. |
| `Child's pose + lateral reach` | `childs_pose_lateral_reach` | missing | Local cues only. |
| `Inchworm + push-up` | `inchworm_push_up` | missing | Local cues only. |
| `Leg swings (front + lateral)` | `leg_swings` | missing | Local cues only. |
| `Hip circle` | `hip_circle` | missing | Local cues only. |
| `Hip circles + arm circles` | `hip_circle` + `arm_circles` | combined | Local cues only. |
| `Ab roller + 3s pause at extension` | `ab_roller` | missing | Local cues only. |
| `Hollow body hold` | `hollow_body_hold` | missing | Local cues only. |
| `Plank shoulder tap` | `plank_shoulder_tap` | missing | Local cues only. |
| `Plank shoulder tap + leg lift` | `plank_shoulder_tap` | close_variant | Local cues only. |
| `Cross-body crawl` | `cross_body_crawl` | missing | Local cues only. |
| `Anti-rotation chop` | `anti_rotation_chop` | missing | Local cues only. |
| `DB Curl pyramid` | `db_curl` | exact | Use Fitbod source after review; pyramid is local protocol. |
| `DB Lateral Raise` | `db_lateral_raise` | exact | Use Fitbod source after review. |
| `DB Rear Delt Fly` | `db_rear_delt_fly` | close_variant | Use close variant label. |
| `DB Floor Press` | `db_floor_press` | close_variant | Use close variant label. |
| `Towel hang (grip)` | `dead_hang` | close_variant | Local towel cue primary. |
| `Y-T-W prone (2lb DBs)` | `y_t_w_prone` | missing | Local cues only. |
| `Prone Y-T-W (2lb DBs)` | `y_t_w_prone` | missing | Local cues only. |
| `Yoga / Pilates session` | `external_practice` | missing | No media; user-owned practice. |
| `Tai Chi practice` | `external_practice` | missing | No media; user-owned practice. |
| `Tai Chi form practice` | `external_practice` | missing | No media; user-owned practice. |
| `Salsa (replaces cardio entirely)` | `external_practice` | missing | No media; user-owned practice. |
| `Shadow boxing (rounds)` | `shadow_boxing` | missing | Local cues only. |
| `Animal flow sequence` | `animal_flow_sequence` | missing | Local cues only unless custom source chosen. |
| `Jump rope / jog / march` | `zone_2_locomotion` | missing | Local cues only. |
| `Jump rope / march` | `zone_2_locomotion` | missing | Local cues only. |
| `Jump rope skill work` | `jump_rope_skill` | missing | Local cues only. |
| `Long walk` | `walk_zone_1` | missing | No media needed. |
| `Pneumatic leg sleeves` | `recovery_tool_pneumatic_sleeves` | missing | No exercise media. |

---

## Generator Rules

1. Read this file before rendering exercise media.
2. Prefer `approved` sources. `needs_review` may be shown only with a review label if we intentionally allow draft mode.
3. Never render `candidate`, `related`, or `missing` as a primary demo video.
4. `close_variant` sources must be labeled as close variants.
5. Safety-sensitive movements require local contraindications even if an external source exists.
6. Active workout cards should show at most one media action. The Exercise Library page may show all mapped sources.
7. If no exact reviewed source exists, show `Media pending` and local cues.
