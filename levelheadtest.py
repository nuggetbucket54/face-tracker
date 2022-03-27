import cv2, os, math, threading
import numpy as np
import mediapipe as mp
from gtts import gTTS
from playsound import playsound

#Set video capture device to default camera
camera = cv2.VideoCapture(0)
flag = True
angle = None

#text for text-to-speech
myobj = gTTS(text="Keep your head level while practicing!", lang="en", slow=False)
myobj.save("message.mp3")

#settings for the mediapipe drawing
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    

# 3D model points. These are generic 3d points for all faces
model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-225.0, 170.0, -135.0),     # Left eye left corner
                            (225.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner

                        ])

#timer function
def timerfunc():
    global angle

    #if head is too low/high, play the alert
    if angle not in range(-2,20):
        playsound("message.mp3")

    #perform this headcheck every 10 seconds
    threading.Timer(10.0, timerfunc).start()


while 1:
    #read default webcam footage
    ret, im = camera.read()
    
    #dimensions of webcam image
    size = im.shape

    #try except statement so that program doesn't crash when face is not detected
    try:
        #convert image from BGR to RGB for the face mesh
        im = cv2.cvtColor(cv2.flip(im, 1), cv2.COLOR_BGR2RGB)
        results = face_mesh.process(im)

        #convert image back to BGR after meshing
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

        
        #if facial landmarks can be placed (if there is a face)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=im,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)
        
        
        """
        #2D image points of the face
        #the coordinate of each landmark multiplied by the length/width of the image
        image_points = np.array([
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[4].x), int(size[0] * results.multi_face_landmarks[0].landmark[4].y)),     # Nose tip
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[152].x), int(size[0] * results.multi_face_landmarks[0].landmark[152].y)),     # Chin
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[359].x), int(size[0] * results.multi_face_landmarks[0].landmark[359].y)),     # Left eye left corner
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[130].x), int(size[0] * results.multi_face_landmarks[0].landmark[130].y)),     # Right eye right corner
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[287].x), int(size[0] * results.multi_face_landmarks[0].landmark[287].y)),     # Left Mouth corner
                                    (int(size[1] * results.multi_face_landmarks[0].landmark[57].x), int(size[0] * results.multi_face_landmarks[0].landmark[57].y))      # Right mouth corner
                                ], dtype="double")



        #details for camera 
        #details were deemed irrelevant since footage is not being analyzed very carefully
        focal_length = size[1]
        center = (size[1]/2, size[0]/2)
        camera_matrix = np.array(
                                [[focal_length, 0, center[0]],
                                [0, focal_length, center[1]],
                                [0, 0, 1]], dtype = "double"
                                )

        #using Perspective-n-Point formula to estimate pose of face (direction person is facing)

        dist_coeffs = np.zeros((4,1))
        (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs)

        (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

        for p in image_points:
            cv2.circle(im, (int(p[0]), int(p[1])), 3, (0,0,255), -1)

        #drawing a line that represents direction faced

        p1 = ( int(image_points[0][0]), int(image_points[0][1]))
        p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
        
        cv2.line(im, p1, p2, (255,0,0), 2)

        #simple trigonometry to determine the approximate angle the head is facing
        angle = int(math.degrees(math.asin((int(image_points[0][1])-int(nose_end_point2D[0][0][1]))/250)))
        
        #will paste an alert on the screen if the head is too high or too low
        if angle not in range(-2, 20):
            cv2.putText(im, "Keep your head level while practicing!", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
        #if the program has just been started, begin the timer
        if flag:
            timerfunc()
            flag = not flag
        """
    except:
        pass
    
    # Display image
    cv2.imshow("Levelhead", im)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
