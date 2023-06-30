# Face tracker
(Originally) a basketball trainer based on computer vision

This repo was originally created for my submission to TreasureHacks 2022: Levelhead. Levelhead used computer vision to determine the angle a person's head is facing and gave aural and visual alerts to promote good basketball practice etiquette. However, this code can be adapted for any use case involving calculating facial orientation angles.

OpenCV and mediapipe were first used to place facial landmarks on a user's head. Specific landmarks and their respective locations were then picked and passed through a Perspective and Point formula to determine the direction the user is facing. Next, a personally developed formula was used to determine the vertical component angle of the person's head. If facing too high/low, visual cues from OpenCV and audio cues from Playsound were used to tell the user to keep their head level while practicing.

<p align="center">
  <br>
  <img src="Levelhead.png"/>
  <br>
  the inner workings of levelhead; the image above shows:
</p>

- Face mesh created from mediapipe are shown with the white dots <br/>
- Points used in the point-to-perspective formula are shown as red dots <br/> 
- Perspective vector is shown with the blue line <br/>
- The vertical angle is shown with the green text in the top left (may be a bit inaccurate lol) <br/>

