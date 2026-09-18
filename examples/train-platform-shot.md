# Example — Restrained Realization at Train Platform

## Creative intent
The audience should recognize a painful realization without melodrama.

## Shot spec

```yaml
shot_id: SC07_SH03
scene_id: SC07
duration_s: 6
purpose: "Show the instant she understands he is not coming."

performance_requirement: required
reference_requirement: required

start_state:
  pose: "left profile"
  gaze: "toward the tracks"
  weight: "mostly on left leg"
  right_hand: "holding BAG_01"
  left_hand: "relaxed beside body"

action:
  primary: "eyes move first, then head turns about 25 degrees toward camera"
  secondary: "one restrained inhale"

performance:
  initial_pose: "left profile, shoulders relaxed"
  weight_distribution: "mostly on left leg"
  gaze: "toward the tracks, then slightly camera-left"
  primary_action: "eyes move first, then head turns about 25 degrees toward camera"
  secondary_action: "one restrained inhale"
  hands: "right hand holds BAG_01; left hand remains relaxed and still"
  torso: "locked"
  face: "restrained realization; no exaggerated brow or mouth change"
  breath: "one subtle inhale"
  final_pose: "restrained three-quarter head position"
  locked_body_parts:
    - torso
    - shoulders
    - hands
    - feet

camera:
  shot_size: "MCU"
  subject_orientation: "profile to three-quarter"
  position:
    horizontal_angle_deg: 35
    height_m: 1.45
    distance_m: 2.2
  orientation:
    yaw_deg: 0
    pitch_deg: 0
    roll_deg: 0
  lens:
    focal_length_mm: 65
    lens_type: "spherical"
  movement:
    type: "locked"
  stabilization: "tripod"
  framing_lock: true
  focus:
    target: "eyes"
    behavior: "stable continuous focus"

motion:
  subject_primary: 1
  subject_secondary: 1
  camera: 0
  environment:
    - "light rain"
    - "distant train-platform activity"

lighting:
  ambient: "cool dusk"
  practicals: "warm station lights behind subject"
  continuity: "light direction unchanged from previous shot"

end_state:
  pose: "three-quarter"
  gaze: "slightly camera-left"
  hands: "unchanged"
  torso: "unchanged"

continuity:
  character:
    character_id: CHAR_01
    identity_state: LOCKED
  wardrobe:
    wardrobe_id: WARD_01
  props:
    BAG_01:
      owner: CHAR_01
      hand: right
      state: unchanged
  spatial:
    screen_direction: "camera-left"
    camera_side: "same side of axis as previous shot"
    eyeline: "slightly camera-left"
    location_geometry_state: "LOC_PLATFORM_01"
  temporal:
    time_of_day: "dusk"
    elapsed_story_time: "continuous"
    weather_state: "light rain"
    lifecycle_state: "SC07_CONTINUOUS"
  lighting:
    source_direction: "unchanged from previous shot"
    practical_state: "warm station lights on"
  narrative:
    audience_knows:
      - "she is waiting for him"
    character_knowledge:
      CHAR_01:
        - "she now realizes he is not coming"
    unresolved_setups: []

references:
  - CHAR_01_IDENTITY_MASTER
  - WARD_01
  - BAG_01
  - LOC_PLATFORM_01

constraints:
  - "no hand movement"
  - "no torso rotation"
  - "no exaggerated expression"
  - "no camera movement"
  - "no face drift"
  - "no wardrobe change"

complexity_score: 3
generation_status: READY
```

## Compiled prompt

A woman stands on a train platform at cool dusk in light rain, shown in a medium close-up with a natural compressed portrait perspective and restrained depth of field. She begins in clean left profile, weight resting naturally on her left leg, right hand holding the same bag continuously, left arm relaxed. Her eyes shift first, then she slowly turns only her head about 25 degrees toward camera and settles into a restrained three-quarter gaze. One subtle inhale and one natural blink after the movement settles. Her shoulders, torso, hands, and feet remain unchanged. Locked tripod framing, stable focus held on the eyes. Cool ambient dusk with warm station practicals behind her. Natural physically plausible human motion, restrained performance, no unnecessary gestures, no camera movement, no body morphing, no hand mutation, no wardrobe or prop change.
