# Automated Exam Proctoring System
This is the code for my Final Year Project, where I created an Automated Exam Proctoring System. This system is made to maintain exam integrity for online exams taken from home during COVID-19, by utilizing students laptop camera. This system have 5 individual systems, where each of them detect different parts of cheating.

## Identity Verification System
In a physical examination hall with in-person proctors, the first thing they do before you enter the exam is to verify your identity with your student ID card. In my system, a login system is implemented where the student must enter their student ID and password. If the entered credentials match and are present in the database, the student's name will be fetched from the database. Subsequently, the student's laptop camera will take a picture of the student and analyze it through the facial recognition system. If the name in the database and the one obtained through facial recognition match, the student will be allowed to enter the exam.

## Multi-Face Detection System
During an exam, there should be only one student present at one desk at any given moment. If there is more than one student present at the desk, it can potentially mean that the student is cheating. I have used MediaPipe Face Detection library to detect the number of faces from the input video of the student's laptop camera. You can visit this link to learn more about it ([MediaPipe Face Detection](https://github.com/google/mediapipe/blob/master/docs/solutions/face_detection.md)).

## Speaking Detection System
It is commonly agreed that during an exam, students should not be talking. If they are talking, then this could potentially mean they are passing on answers from the test questions. Therefore, I have used MediaPipe Face Mesh to extract out 8 important mouth coordinates. With these mouth coordinates, I have calculated the Mouth Aspect Ratio formula, which is:
$$MAR = \frac{d(C, D) + d(E, F) + d(G, H)}{d(A, B)}$$

where,

$$d(p, q) = \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}$$

represents the Euclidean distance between point $p$ and $q$. The points are represented in the image down below:
![Mouth Aspect Ratio Landmarks](/path/to/image.jpg "Optional title")
