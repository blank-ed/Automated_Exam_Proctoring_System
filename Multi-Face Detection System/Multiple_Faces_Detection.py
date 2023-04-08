import cv2
import mediapipe as mp

def MultipleFacesDetector(frame):

    mpFaceDetection = mp.solutions.face_detection
    faceDetection = mpFaceDetection.FaceDetection()

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    i = 0
    if results.detections:
        for id, detection in enumerate(results.detections):
            i = i + 1
            if i > 1:
                return 1
    else:
        return 0
