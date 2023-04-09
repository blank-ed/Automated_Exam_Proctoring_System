# import the necessary packages
import numpy as np
import imutils
import pickle
import cv2
import easygui

# filename is the name of the user that will be automatically filled in when the user logs in from the main system
def recognition(take_picture=False):
    # Specify input takes a picture of the user from the camera instead of manually choosing an input image
    if take_picture:
        # Access Students Camera
        cap = cv2.VideoCapture(0)
        # Read Frames From Video
        ret, frame = cap.read()
        while True:
            # Take a Picture of Students Faces
            cv2.imwrite('identity_verification\\student.jpeg', frame)
            cv2.destroyAllWindows()
            break
        cap.release()

    # load our serialized face detector from disk
    print("Loading face detector...")
    detector = cv2.dnn.readNetFromCaffe('identity_verification\\Face Detector and Recognition Models\\deploy.prototxt',
                                        'identity_verification\\Face Detector and Recognition Models\\res10_300x300_ssd_iter_140000.caffemodel')
    # load our serialized face embedding model from disk
    print("Loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch('identity_verification\\Face Detector and Recognition Models\\openface_nn4.small2.v1.t7')
    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads(open('identity_verification\\Face Detector and Recognition Models\\Face_Recognition_Model.pickle', "rb").read())
    le = pickle.loads(open('identity_verification\\Face Detector and Recognition Models\\Label_Encoder.pickle', "rb").read())

    # Load the image containing Students Face, resize it to have a width of 600 pixels (while maintaining the aspect ratio), and then grab the image dimensions
    if take_picture:
        image = cv2.imread('identity_verification\\student.jpeg')
    else:
        image = cv2.imread(easygui.fileopenbox(default='identity_verification/Test Images'))
    image = imutils.resize(image, width=600)
    (h, w) = image.shape[:2]
    # construct a blob from the image
    imageBlob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)
    # apply OpenCV's deep learning-based face detector to localize faces in the input image
    detector.setInput(imageBlob)
    detections = detector.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the prediction
        confidence = detections[0, 0, i, 2]
        # filter out weak detections
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the face
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # extract the face ROI
            face = image[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]
            # ensure the face width and height are sufficiently large
            if fW < 20 or fH < 20:
                continue
            # construct a blob for the face ROI, then pass the blob through our face embedding model to obtain the 128-d quantification of the face
            faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
            embedder.setInput(faceBlob)
            vec = embedder.forward()
            # perform classification to recognize the face
            preds = recognizer.predict_proba(vec)[0]
            j = np.argmax(preds)
            name_from_recognition = le.classes_[j]
    # return the name of the detected user
    return name_from_recognition
