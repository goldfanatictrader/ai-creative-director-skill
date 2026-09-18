# Example — Restrained Realization at Train Platform

## Creative intent
The audience should recognize a painful realization without melodrama.

## Shot spec

```yaml
shot_id: SC07_SH03
scene_id: SC07
duration_s: 6

purpose: "Show the instant she understands he is not coming."

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
  expression: "restrained shock"
  hands: "locked"
  torso: "locked"
  shoulders: "relaxed and unchanged"
  blink: "one natural blink after head settles"

camera:
  shot_size: "MCU"
  subject_orientation: "profile to three-quarter"
  position:
    horizontal_angle_deg: 35
    height_m: 1.45
    distance_m: 2.2
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

A woman stands on a train platform at cool dusk in light rain, shown in a medium close-up with a 65mm spherical lens at eye level. She begins in clean left profile, weight resting naturally on her left leg, right hand holding the same bag continuously, left arm relaxed. Her eyes shift first, then she slowly turns only her head about 25 degrees toward camera and settles into a restrained three-quarter gaze. One subtle inhale and one natural blink after the movement settles. Her shoulders, torso, hands, and feet remain unchanged. Locked tripod camera, stable framing, focus held on the eyes. Cool ambient dusk with warm station practicals behind her. Natural physically plausible human motion, restrained performance, no unnecessary gestures, no camera movement, no body morphing, no hand mutation, no wardrobe or prop change.
