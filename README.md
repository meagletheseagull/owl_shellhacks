# owl
Hackathon Challenge for Edge Compute Vision and Coordinate Interaction.

## Challenge

### Standard
Can you, given the coordinates and direction of a camera, determine the rotation and elevation needed to pan and tilt that camera to look at an arbitrary latitude/longitude/elevation coordinate.

### Bonus
* Can you deal with a camera that is moving so it would track a point... like an owl.
* Can you deal with a rotating camera?
* Can you main tracking even if gps is intermittent?


### Ultra Bonus
Given a bounding box in the camera's view, can you determine the coordinates of that rough location in latitude / longitude / altitude in the real world.

## Constraints
* Camera Coordinates will be in latitude / longitude / altitude
* Camera direction is not known but will need to be determined. How? Can you?
* Target coordinates will be in latitude / longitude / altitude
* Camera can only be controlled in roughly degrees off local center pan and tilt.
* GPS coordinates of camera will be provided
  * Will be live (if our test harness is working right.)
* Target coordinates will be provided
* Coordinates are limited to earth


