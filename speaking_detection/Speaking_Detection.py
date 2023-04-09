import mediapipe as mp
from scipy.spatial import distance as dist


def mouth_aspect_ratio(mouth_coords):
    # compute the euclidean distances between the two sets of vertical mouth landmarks (x, y)-coordinates
    A = dist.euclidean(mouth_coords[2], mouth_coords[4])  # 37 84
    B = dist.euclidean(mouth_coords[0], mouth_coords[1])  # 0 17
    C = dist.euclidean(mouth_coords[5], mouth_coords[7])  # 267 314

    # compute the euclidean distance between the horizontal mouth landmark (x, y)-coordinates
    D = dist.euclidean(mouth_coords[3], mouth_coords[6])  # 61 291

    # compute the mouth aspect ratio
    mar = (A + B + C) / (3.0 * D)

    # return the mouth aspect ratio
    return mar


def SpeakingDetection(frame, mar_threshold=0.5):
    mp_face_mesh = mp.solutions.face_mesh
    # Specify the important mouth indices
    mouth_indices = [0, 17, 37, 61, 84, 267, 291, 314]
    with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5,
                               min_tracking_confidence=0.5) as face_mesh:
        frame.flags.writeable = False
        results = face_mesh.process(frame)
        frame.flags.writeable = True

        h, w = frame.shape[:2]
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]
            # get the coordinates of only the mouth indices
            mouth_coords = [(int(l.x * w), int(l.y * h)) for i, l in enumerate(landmarks.landmark) if i in mouth_indices]

            # calculate the mouth aspect ratio
            mar = mouth_aspect_ratio(mouth_coords)

            # if mar is greater than threshold, student is speaking
            if mar > mar_threshold:
                return 1
            else:
                return 0
