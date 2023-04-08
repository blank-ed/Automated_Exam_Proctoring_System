# Automated Exam Proctoring System
This is the code for my Final Year Project, where I created an Automated Exam Proctoring System. This system is made to maintain exam integrity for online exams taken from home during COVID-19, by utilizing students laptop camera. This system have 5 individual systems, where each of them detect different parts of cheating.
For best **__user experience__**, clone this repo in your **__PyCharm Python IDE__** as all of the steps and directions are based on this. 

## Identity Verification System
In a physical examination hall with in-person proctors, the first thing they do before you enter the exam is to verify your identity with your student ID card. In my system, a login system is implemented where the student must enter their student ID and password. If the entered credentials match and are present in the database, the student's name will be fetched from the database. Subsequently, the student's laptop camera will take a picture of the student and analyze it through the facial recognition system. If the name in the database and the one obtained through facial recognition match, the student will be allowed to enter the exam.

This system takes in an image, runs it through the pre-trained model which is in the `Identity Verification System/Face Detector and Recognition Models` and outputs a name. If you don't specify the input image, then it will utilize your camera to take a picture of you. If you want to specify the input and use the pre-trained model, you can select the images from `Identity Verification System/Test Images` and choose any one of the person in there along with their respective image.

If you want to train your own facial recognition model, then in the `Identity Verification System/Dataset` folder, create a folder with the users *__first name__* and add their respective images in those folder. Then, run the `Identity Verification System/Train_Facial_Recognition_System.py` file. 

## Multi-Face Detection System
During an exam, there should be only one student present at one desk at any given moment. If there is more than one student present at the desk, it can potentially mean that the student is cheating. I have used MediaPipe Face Detection library to detect the number of faces from the input video of the student's laptop camera. You can visit this link to learn more about it ([MediaPipe Face Detection](https://github.com/google/mediapipe/blob/master/docs/solutions/face_detection.md)).

## Speaking Detection System
It is universally agreed that during an exam, students should not be talking. If they are talking, then this could potentially mean they are passing on answers from the test questions. Therefore, I have used [MediaPipe Face Mesh](https://github.com/google/mediapipe/blob/master/docs/solutions/face_mesh.md) to extract out 8 important mouth points. With these mouth points and their respective coordinates, I have calculated the Mouth Aspect Ratio by using the formula:
$$MAR = \frac{d(C, D) + d(E, F) + d(G, H)}{d(A, B)}$$

where,

$$d(p, q) = \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}$$

represents the Euclidean distance between point $p$ and $q$. The points are represented in the image down below:
<p align="center">
  <img src="https://github.com/blank-ed/Automated_Exam_Proctoring_System/blob/master/Necessary%20Files/Mouth%20Aspect%20Ratio.png" width="200" height="auto">
</p>

I set the Mouth Aspect Ratio threshold value to 0.5, which means that if the calculated MAR is greater than 0.5, the student is talking. There are different papers that use different mouth points and I have listed down a couple of them for your reference:
- Sri Mounika, T.V.N.S.R., Phanindra, P.H., Sai Charan, N.V.V.N., Kranthi Kumar Reddy, Y. and Govindu, S., 2022. Driver Drowsiness Detection Using Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and Driver Distraction Using Head Pose Estimation. In ICT Systems and Sustainability: Proceedings of ICT4SD 2021, Volume 1 (pp. 619-627). Springer Singapore. ([link](https://link.springer.com/chapter/10.1007/978-981-16-5987-4_63))
- Singh, A., Chandewar, C. and Pattarkine, P., 2018. Driver drowsiness alert system with effective feature extraction. Int. J. Res. Emerg. Sci. Technol, 5, pp.14-19. ([link](https://ijrest.net/downloads/volume-5/issue-4/pid-ijrest-54201808.pdf))

## Head Position Detection System
Additionally during an exam, students should not be looking around as well. If they are found to be turning their heads, then this could also potentially mean they are checking the answer sheets of their peers. Therefore, I have used [MediaPipe Face Mesh](https://github.com/google/mediapipe/blob/master/docs/solutions/face_mesh.md) to extract out important facial points from the left & right iris and top of the face & bottom of the face. With the 4 facial points each from the left & right iris, the center of the iris is calculated. Furthermore, the distance between the irises is calculated. The distance between the top of the face and the bottom of the face is also calculated. The Head Position Ratio is then calculated using the formula:
$$HPR = \frac{d(Left, Right)}{d(Up, Down)}$$

where,

$$d(p, q) = \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}$$

represents the Euclidean distance between point $p$ and $q$. The center of the irises are calculated by using the formula:
$$Center = (\frac{x_A + x_B + x_C + x_D}{4}, \frac{y_A + y_B + y_C + y_D}{4})$$

The points are represented in the image down below:
<p align="center">
  <img src="https://github.com/blank-ed/Automated_Exam_Proctoring_System/blob/master/Necessary%20Files/Head%20Position%20Ratio.png" width="200" height="auto">
</p>

I set the Head Position Ratio threshold value to 0.33, which means that if the calculated HPR is less than this, the student is looking around (left or right).

## Phone Detection System
During an exam, electronics devices should not be used by students. Therefore, I have used TensorFlow Object Detection API, using SSD-MobileNet, to train the model to detect my phone. The pre-trained models are located in the `Phone Detection System/Pre-Trained Models` folder. The files in this folder are as follows:
- `ckpt-3.data-00000-of-00001`: This is a binary file that contains the values of the trained model parameters (weights and biases) stored in a checkpoint file format. Checkpoint files are used to save and restore the state of a TensorFlow model during training or inference.
- `ckpt-3.index`: This is an index file that points to the locations of the variable values stored in the ckpt-3.data-00000-of-00001 file.
- `label_map.pbtxt`: This is a text file that contains a mapping between class names and integer IDs. It is used by the Object Detection API to map the output of the model (which is usually in the form of integer class IDs) back to human-readable class names. Right now there is only one class, which is `Phone`.
- `pipeline.config`: This is a configuration file that contains all the settings and hyperparameters used to train the model, as well as the model architecture and training data specifications. It is used by the Object Detection API to build the model graph and run the training or inference process.

After you clone the repo, follow the step by step guide to install TensorFlow Object Detection from [here](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#tensorflow-object-detection-api-installation). Here is a shorter and quicker version that I use:
- Clone this TensorFlow models [repo](https://github.com/tensorflow/models) into your project.
- Download protobuf from this [link](https://github.com/protocolbuffers/protobuf/releases), extract it and add `<PATH_TO_PROTOBUF/bin` to your PATH.
- Then in your command line, type: `cd models/research` and enter `protoc object_detection/protos/*.proto --python_out=.`
- Copy this by using the command: `cp object_detection/packages/tf2/setup.py .` and enter `python -m pip install .` (NOTE: depending on the IDEs, it can be cp or copy)

If you wish to create your own model and replace this one, you are more than welcome to do so. You can find a full video course down below for your reference. He explains everything in this video properly, from start to finish, on how to train a custom object detection model. I have also listed down additional links for your reference:
- [TensorFlow Object Detection Step-by-Step Guide](https://www.youtube.com/watch?v=yqkISICHH-U&t=0s)
- [Easier way to install CUDA and CuDNN](https://www.youtube.com/watch?v=hHWkvEcDBO0&t=0s)
