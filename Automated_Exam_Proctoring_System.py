# this is from pip or built in libraries
import time
import time as t
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
import sys
import cv2
import csv
import numpy as np

## Load Database
students = []
with open("Necessary Files/Database.txt", "r") as f:
    file_contents = f.read().split('=')[1]
    for each_student in eval(file_contents):
        students.append(each_student)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 300, 440)
        self.setWindowTitle("APProctor")
        self.setStyleSheet('background-color: white')
        self.initUI()

    def initUI(self):
        # APU Logo
        self.logolabel = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('Necessary Files/apulogo.png')
        self.logo_resized = self.pixmap.scaled(280, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logolabel.setPixmap(self.logo_resized)
        self.logolabel.adjustSize()
        self.logolabel.move(10, 10)

        # Extra Label 1
        self.extralabel_one = QtWidgets.QLabel(self)
        self.extralabel_one.setText("APProctor")
        self.extralabel_one.setFont(QFont('Bold', 15, weight=QFont.Bold))
        self.extralabel_one.setStyleSheet('color: #cccccc;')
        self.extralabel_one.adjustSize()
        self.extralabel_one.move(10, 120)

        # Extra Label 2
        self.extralabel_two = QtWidgets.QLabel(self)
        self.extralabel_two.setText("Your digital university")
        self.extralabel_two.setFont(QFont('Bold', 15, weight=QFont.Bold))
        self.extralabel_two.setStyleSheet('color: #cccccc;')
        self.extralabel_two.adjustSize()
        self.extralabel_two.move(10, 150)

        # Extra Label 3
        self.extralabel_three = QtWidgets.QLabel(self)
        self.extralabel_three.setText("exam proctorer")
        self.extralabel_three.setFont(QFont('Bold', 15, weight=QFont.Bold))
        self.extralabel_three.setStyleSheet('color: #cccccc;')
        self.extralabel_three.adjustSize()
        self.extralabel_three.move(10, 180)

        # Username Input Field
        self.userfield = QtWidgets.QLineEdit(self)
        self.userfield.setStyleSheet("border :1px solid #cccccc;" "border-top-left-radius :7px;" " border-top-right-radius : 7px; " " border-color: #cccccc #cccccc red #cccccc; " " padding-left: 10px;")
        self.userfield.setPlaceholderText('APKey')
        self.userfield.move(10, 220)
        self.userfield.resize(280, 40)

        # Password Input Field
        self.passfield = QtWidgets.QLineEdit(self)
        self.passfield.setStyleSheet("border :1px solid #cccccc;" "border-bottom-left-radius :7px;" " border-bottom-right-radius : 7px; " " border-color: red #cccccc #cccccc #cccccc; " " padding-left: 10px;")
        self.passfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passfield.setPlaceholderText('Password')
        self.passfield.move(10, 260)
        self.passfield.resize(280, 40)

        # Login Button
        self.button = QtWidgets.QPushButton("LOGIN", self)
        self.button.clicked.connect(self.clicked)
        self.button.setStyleSheet("color: white;" "background-color: #1070a2;" "border :1px solid #1070a2;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;" "letter-spacing : 5px")
        self.button.setFont(QFont('Bold', 10, weight=QFont.Bold))
        self.button.resize(140, 40)
        self.button.move(80, 320)

        # Error Message
        self.errorlabel = QtWidgets.QLabel(self)
        self.errorlabel.resize(280, 40)
        self.errorlabel.setText("Invalid Username or Password")
        self.errorlabel.move(10, 380)
        self.errorlabel.setAlignment(Qt.AlignCenter)
        self.errorlabel.setStyleSheet("color: white;" "background-color: red;" "border :1px solid red;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;")
        self.errorlabel.setVisible(False)

    def Blank_Label_Timer(self):
        self.blanklabel.setVisible(False)

    def Error_Label_Timer(self):
        self.errorlabel.setVisible(False)

    def clicked(self):
        username = self.userfield.text()
        password = self.passfield.text()
        if username == '' or password == '':
            self.blanklabel = QtWidgets.QLabel(self)
            self.blanklabel.resize(280, 40)
            self.blanklabel.setText("Please Fill Up Username and Password")
            self.blanklabel.setAlignment(Qt.AlignCenter)
            self.blanklabel.move(10, 380)
            self.blanklabel.setStyleSheet("color: white;" "background-color: red;" "border :1px solid red;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;")
            self.blanklabel.setVisible(True)
            blanklabeltimer = QTimer(self)
            blanklabeltimer.timeout.connect(self.Blank_Label_Timer)
            blanklabeltimer.start(5000)

        else:
            for each_student in students:
                if each_student["username"] == username and each_student["password"] == password:
                    print('yes')
                else:
                    self.blanklabel = QtWidgets.QLabel(self)
                    self.blanklabel.resize(280, 40)
                    self.blanklabel.setText("Please Fill Up Correct Username and Password")
                    self.blanklabel.setAlignment(Qt.AlignCenter)
                    self.blanklabel.move(10, 380)
                    self.blanklabel.setStyleSheet("color: white;" "background-color: red;" "border :1px solid red;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;")
                    self.blanklabel.setVisible(True)
                    blanklabeltimer = QTimer(self)
                    blanklabeltimer.timeout.connect(self.Blank_Label_Timer)
                    blanklabeltimer.start(5000)

        # cursordb = connectiondb.cursor()
        # loadname = f"select Name from user where username='{username}' and password='{password}'"
        # cursordb.execute(loadname)
        # data = cursordb.fetchone()
    #     if data is not None:
    #
    #         # these are my python files
    #         # import facerecognition
    #         # import multiplefaces
    #         # import objectdetection
    #         # import speakingdetection
    #         # import headposition
    #         # from headpostitionML import HeadpositionMachineLearning
    #         # end imports
    #
    #         name = data[0]
    #         self.errorlabel.setVisible(False)
    #         # recognition_result = facerecognition.recognition(name)
    #         # print(recognition_result)
    #         if name == 'Ilyas':
    #             self.close()
    #             # cap = cv2.VideoCapture(1)
    #             cap = cv2.VideoCapture(0)
    #             ## FOR TIME ON OUTPUT WINDOW
    #             exam_ends_time = datetime.datetime.now()
    #             extra_time = datetime.timedelta(hours=3)
    #             exam_ends_time_int = exam_ends_time + extra_time
    #             exam_ends_time = exam_ends_time_int.strftime("%H:%M:%S")
    #             ## END TIME FOR OUTPUT WINDOW
    #
    #             while True:
    #                 ret, frame = cap.read()
    #
    #                 ## START OUTPUT WINDOW
    #                 output = cv2.imread('output.png')
    #                 output = cv2.resize(output, (500,600))
    #                 now = datetime.datetime.now()
    #                 current_time = now.strftime("%H:%M:%S")
    #
    #                 time_remaining = exam_ends_time_int - now
    #                 time_remaining = str(time_remaining).split('.', 2)[0]
    #                 name = 'Ilyas'
    #                 cv2.putText(output, "Student Name: {}".format(name), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    #                 username = "TPXXXXXX"
    #                 cv2.putText(output, "TP Number: {}".format(username), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    #
    #                 cv2.putText(output, "Current Time: {}".format(current_time), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1,
    #                             (255, 255, 255), 2)
    #
    #                 cv2.putText(output, "Exam Ends at: {}".format(exam_ends_time), (10, 200), cv2.FONT_HERSHEY_SIMPLEX,
    #                             1, (255, 255, 255), 2)
    #                 cv2.putText(output, "Time Remaining: {}".format(time_remaining), (10, 250), cv2.FONT_HERSHEY_SIMPLEX,
    #                             1, (255, 255, 255), 2)
    #                 ## END OUTPUT WINDOW
    #
    #                 ## START DETECTION TYPES
    #
    #                 n = 250
    #                 # if multiplefaces.MultipleFacesDetector(frame) == 'many_faces':
    #                 #     n += 50
    #                 #     cv2.putText(output, "Anomaly Type: MULTIPLE FACES DETECTED", (10, n), cv2.FONT_HERSHEY_SIMPLEX,
    #                 #                 0.7, (0, 0, 255), 2)
    #                 #     with open('detections.csv', mode='a', newline='') as f:
    #                 #         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                 #         # write the data
    #                 #         writer.writerow([name, username, "Multiple Faces Detected", current_time])
    #                 #
    #                 # elif multiplefaces.MultipleFacesDetector(frame) == 'no_faces':
    #                 #     n += 50
    #                 #     cv2.putText(output, "Anomaly Type: NO STUDENT DETECTED", (10, n), cv2.FONT_HERSHEY_SIMPLEX,
    #                 #                 0.7, (0, 0, 255), 2)
    #                 #     with open('detections.csv', mode='a', newline='') as f:
    #                 #         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                 #         # write the data
    #                 #         writer.writerow([name, username, "No Faces Detected", current_time])
    #                 # #
    #                 # if speakingdetection.SpeakingDetection(frame) == 'mar':
    #                 #     n += 50
    #                 #     cv2.putText(output, "Anomaly Type: SPEAKING", (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
    #                 #                 (0, 0, 255), 2)
    #                 #     with open('detections.csv', mode='a', newline='') as f:
    #                 #         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                 #         # write the data
    #                 #         writer.writerow([name, username, "Student Speaking", current_time])
    #
    #                 # if headposition.HeadPosition(frame) == 'look_left':
    #                 #     n += 50
    #                 #     cv2.putText(output, 'Anomaly Type: STUDENT LOOKING LEFT', (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #                 # elif headposition.HeadPosition(frame) == 'look_right':
    #                 #     n += 50
    #                 #     cv2.putText(output, 'Anomaly Type: STUDENT LOOKING RIGHT', (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #
    #                 # objectdetection_output, defect, score = objectdetection.ObjectDetection(frame)
    #                 # if score > 0.8:
    #                 #     n += 50
    #                 #     defect_percentage = "{:.2%}".format(score)
    #                 #     cv2.putText(output, "Anomaly Type: {}, Accuracy: {}".format(defect, defect_percentage), (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
    #                 #                 (0, 0, 255), 2)
    #                 #     with open('detections.csv', mode='a', newline='') as f:
    #                 #         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                 #         # write the data
    #                 #         writer.writerow([name, username, "Phone Usage Detected, Accuracy: {}".format(defect_percentage), current_time])
    #
    #                 headpose_class, headpose_prob = HeadpositionMachineLearning(frame)
    #                 headpose_prob = str(round(headpose_prob[np.argmax(headpose_prob)], 2))
    #                 if headpose_class == 'Looking Left':
    #                     n += 50
    #                     cv2.putText(output, "Anomaly Type: STUDENT LOOKING LEFT", (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #                     n += 50
    #                     cv2.putText(output, "Accuracy: {}".format(headpose_prob), (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #                     with open('detections.csv', mode='a', newline='') as f:
    #                         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                         # write the data
    #                         writer.writerow([name, username, "Student Looking Left", current_time])
    #                 elif headpose_class == 'Looking Right':
    #                     n += 50
    #                     cv2.putText(output, "Anomaly Type: STUDENT LOOKING RIGHT", (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #                     n += 50
    #                     cv2.putText(output, "Accuracy: {}".format(headpose_prob), (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    #                     with open('detections.csv', mode='a', newline='') as f:
    #                         writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #                         # write the data
    #                         writer.writerow([name, username, "Student Looking Right", current_time])
    #                 elif headpose_class == 'Looking Front':
    #                     n += 50
    #                     cv2.putText(output, "Anomaly Type: STUDENT LOOKING FRONT", (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    #                     n += 50
    #                     cv2.putText(output, "Accuracy: {}".format(headpose_prob), (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    #
    #                 ## END DETECTION TYPES
    #
    #                 # cv2.imshow('Exam Proctoring System', cv2.resize(objectdetection_output, (800, 600)))
    #
    #                 cv2.imshow("Exam Proctoring System", cv2.resize(frame, (800,600)))
    #                 cv2.imshow('Output', output)
    #
    #                 if cv2.waitKey(5) & 0xFF == ord('q'):
    #                     break
    #
    #             cap.release()
    #             self.errorlabel.setVisible(False)
    #         else:
    #             self.invalidlabel = QtWidgets.QLabel(self)
    #             self.invalidlabel.resize(280, 40)
    #             self.invalidlabel.setText("Anomaly Type: Name and Face Not Matching,      Database Name: {}, "
    #                                       "Face Recognition Result: {}".format(name, recognition_result))
    #             self.invalidlabel.setWordWrap(True)
    #             self.invalidlabel.setAlignment(Qt.AlignCenter)
    #             self.invalidlabel.move(10, 380)
    #             self.invalidlabel.setStyleSheet("color: white;"
    #                                           "background-color: red;"
    #                                           "border :1px solid red;"
    #                                           "border-top-left-radius :4px;"
    #                                           "border-top-right-radius : 4px;"
    #                                           "border-bottom-left-radius : 4px;"
    #                                           "border-bottom-right-radius : 4px;")
    #             self.invalidlabel.setVisible(True)
    #
    #     else:
    #         self.errorlabel.setVisible(True)
    #         errorlabeltimer = QTimer(self)
    #         errorlabeltimer.timeout.connect(self.Error_Label_Timer)
    #         errorlabeltimer.start(5000)
    #     # # Test Section
    #     #
    #     # # End Test Section


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
