# Camera Bible

## Camera intent
Camera movement must answer a narrative need.

Observe → static  
Approach → push-in  
Withdraw → pull-back  
Follow → tracking  
Reveal → slide / pan / crane reveal  
Instability → controlled handheld  
Scale → wide / crane / aerial

## Coordinates
Translation:
- X = left / right
- Y = up / down
- Z = forward / backward

Rotation:
- yaw = pan
- pitch = tilt
- roll = horizon rotation

## Camera height
- floor
- ankle
- knee
- hip
- waist
- chest
- shoulder
- eye
- above head
- elevated
- aerial

## Horizontal relationship
0° frontal  
15–25° slight three-quarter  
30–45° three-quarter  
90° profile  
120–150° rear three-quarter  
180° back

## Movement
Rotation: pan, tilt, roll  
Translation: dolly, truck, pedestal, crane  
Relative: track, follow, lead, orbit, arc  
Optical: zoom, rack focus  
Complex: crane+push, orbit+rise, reveal

## Movement geometry
Specify:
- direction
- displacement
- radius if orbiting
- arc degrees
- duration
- speed
- easing
- subject framing behavior

## Stabilization
- locked tripod
- tripod pan/tilt
- slider
- dolly
- Steadicam
- gimbal
- shoulder
- controlled handheld
- documentary handheld
- crane
- drone
- motion control

## Inertia
Real cameras have mass.
Prefer gradual acceleration and deceleration unless the shot intentionally snaps.

## Framing stability
Define:
- locked framing
- dynamic reframing
- constant subject size
- rule-of-thirds lock
- loose operator follow
- human lag

## Horizontal position is not optional
Always state one of the horizontal-relationship values explicitly (frontal / three-quarter / profile / rear three-quarter / back) plus which side. A shot description that only gives size + subject ("close-up of hand gripping X") without horizontal position routinely resolves into a physically impossible camera placement — most often a frontal shot that would require the camera to float in front of the subject/object facing back toward it. This is one of the most common real-world causes of "this doesn't look like a real camera position" feedback. See `ai-video-failure-bible.md` → Camera angle ambiguity.

## Global camera failures to prevent
- random zoom
- spontaneous orbit
- horizon drift
- focal-length morphing
- camera clipping
- impossible path
- teleportation
- unexplained reframing
