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
            # bboxC = detection.location_data.relative_bounding_box
            # ih, iw, ic = frame.shape
            # bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            # cv2.rectangle(frame, bbox, (225, 0, 0), 2)
            i = i + 1
            if i > 1:
                # cv2.putText(frame, "Anomaly Type: MULTIPLE FACES DETECTED", (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                #             (0, 0, 255), 2)
                return 1
    else:
        # cv2.putText(frame, "Anomaly Type: NO STUDENT DETECTED", (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
        #             (0, 0, 255), 2)
        return 0
