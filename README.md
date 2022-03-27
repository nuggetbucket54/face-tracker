# levelhead
(currently under work) a basketball trainer based on computer vision

![image](https://user-images.githubusercontent.com/55860775/160269657-4cf698f7-dd32-4f7e-862e-1b90c30b7600.png)

Levelhead uses computer vision to determine the angle a person's head is facing. If the user's head is tilted too high or low, Levelhead gives an aural and visual alert to keep their head level. So far this is literally just a program that detects when your head is not perfectly level to the camera (sadge)

OpenCV and mediapipe were first used to place facial landmarks on a user's head. Specific landmarks and their respective locations were then picked and passed through a Perspective and Point formula to determine the direction the user is facing. Next, a personally developed formula was used to determine the vertical component angle of the person's head. If facing too high/low, visual cues from OpenCV and audio cues from Playsound were used to tell the user to keep their head level while practicing.
