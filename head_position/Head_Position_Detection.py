import mediapipe as mp
from scipy.spatial import distance as dist
import numpy as np

def head_position_ratio(left_iris_coords, right_iris_coords, top_bottom_coords):
    # calculate center of iris
    left_center = tuple(np.mean(left_iris_coords, axis=0).astype(int))
    right_center = tuple(np.mean(right_iris_coords, axis=0).astype(int))

    left_right_distance = dist.euclidean(left_center, right_center) # calculate distance between left iris and right iris
    top_bottom_distance = dist.euclidean(top_bottom_coords[0], top_bottom_coords[1]) # calculate distance between top and bottom

    # calculate head position ratio
    hpr = (left_right_distance / top_bottom_distance)

    return hpr


def HeadPositionDetection(frame, hpr_threshold=0.33):
    mp_face_mesh = mp.solutions.face_mesh

    # Specify the important indices
    left_iris_indices = [474, 475, 476, 477]
    right_iris_indices = [469, 470, 471, 472]
    top_bottom_indices = [10, 152]

    with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
        frame.flags.writeable = False
        results = face_mesh.process(frame)
        frame.flags.writeable = True

        h, w = frame.shape[:2]
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]

            # get the coordinates of specified indices
            left_iris_coords = [(int(l.x * w), int(l.y * h)) for i, l in enumerate(landmarks.landmark) if i in left_iris_indices]
            right_iris_coords = [(int(l.x * w), int(l.y * h)) for i, l in enumerate(landmarks.landmark) if i in right_iris_indices]
            top_bottom_coords = [(int(l.x * w), int(l.y * h)) for i, l in enumerate(landmarks.landmark) if i in top_bottom_indices]

            # calculate the mouth aspect ratio
            hpr = head_position_ratio(left_iris_coords, right_iris_coords, top_bottom_coords)

            # if hpr is greater than threshold, student is looking around
            if hpr < hpr_threshold:
                return 1
            else:
                return 0
