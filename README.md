# Automated Exam Proctoring System
This is the code for my Final Year Project, where I created an Automated Exam Proctoring System. This system is made to maintain exam integrity for online exams taken from home during COVID-19, by utilizing students laptop camera. This system have 5 individual systems, where each of them detect different parts of cheating.

## Identity Verification System
In a physical examination hall with in-person proctors, the first thing they do before you enter the exam is to verify your identity with your student ID card. In my system, a login system is implemented where the student must enter their student ID and password. If the entered credentials match and are present in the database, the student's name will be fetched from the database. Subsequently, the student's laptop camera will take a picture of the student and analyze it through the facial recognition system. If the name in the database and the one obtained through facial recognition match, the student will be allowed to enter the exam.

## Multi-Face Detection System
During an exam, there should only be one student present at one desk at any given moment. If there are more than 1 student present at the desk, this can potentially mean that the student is cheating. I have used MediaPipe Face Detection library to detect the number of faces from the input video of the students laptop camera. You can visit this link to learn more about [MediaPipe Face Detection](https://github.com/google/mediapipe/blob/master/docs/solutions/face_detection.md)
