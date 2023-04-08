# Automated Exam Proctoring System
This is the code for my Final Year Project, where I created an Automated Exam Proctoring System. This system is made to maintain exam integrity for online exams taken from home during COVID-19, by utilizing students laptop camera. This system have 5 individual systems, where each of them detect different parts of cheating.

## Identity Verification System
In a physical examination hall with in-person proctors, the first thing they do before you enter the exam is to verify your identity with your student ID card. In my system, a login system is implemented where the student must enter their student ID and password. If the entered credentials match and are present in the database, the student's name will be fetched from the database. Subsequently, the student's laptop camera will take a picture of the student and analyze it through the facial recognition system. If the name in the database and the one obtained through facial recognition match, the student will be allowed to enter the exam.

## Multi-Face Detection System
During an exam, there should be only one student present at one desk at any given moment. If there is more than one student present at the desk, it can potentially mean that the student is cheating. I have used MediaPipe Face Detection library to detect the number of faces from the input video of the student's laptop camera. You can visit this link to learn more about it ([MediaPipe Face Detection](https://github.com/google/mediapipe/blob/master/docs/solutions/face_detection.md)).

## Speaking Detection System
It is universally agreed that during an exam, students should not be talking. If they are talking, then this could potentially mean they are passing on answers from the test questions. Therefore, I have used MediaPipe Face Mesh to extract out 8 important mouth points. With these mouth points and their respective coordinates, I have calculated the Mouth Aspect Ratio by using the formula:
$$MAR = \frac{d(C, D) + d(E, F) + d(G, H)}{d(A, B)}$$

where,

$$d(p, q) = \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}$$

represents the Euclidean distance between point $p$ and $q$. The points are represented in the image down below:
<p align="center">
  <img src="https://github.com/blank-ed/Automated_Exam_Proctoring_System/blob/master/Necessary%20Files/Mouth%20Aspect%20Ratio.png" width="200" height="auto">
</p>

I set the Mouth Aspect Ratio threshold value to 0.5, which means that if the calculated MAR is greater than 0.5, the student is talking. There are different papers that use different mouth points and I have listed down a few of them for your reference:
- Sri Mounika, T.V.N.S.R., Phanindra, P.H., Sai Charan, N.V.V.N., Kranthi Kumar Reddy, Y. and Govindu, S., 2022. Driver Drowsiness Detection Using Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and Driver Distraction Using Head Pose Estimation. In ICT Systems and Sustainability: Proceedings of ICT4SD 2021, Volume 1 (pp. 619-627). Springer Singapore ([link](https://link.springer.com/chapter/10.1007/978-981-16-5987-4_63).

