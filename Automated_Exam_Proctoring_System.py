# Importing libraries
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
import sys
from identity_verification.Verify_Identity import recognition
import cv2
from head_position import Head_Position_Detection
from multi_face_detection import Multiple_Faces_Detection
from phone_detection import Phone_Detection
from speaking_detection import Speaking_Detection
import datetime
import csv

## Load Database
students = []
with open("Necessary Files\\Database.txt", "r") as f:
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

        # Checkbox
        self.checkbox = QtWidgets.QCheckBox(self)
        self.checkbox.setChecked(True)
        self.checkbox.setText("Choose Picture")
        self.checkbox.move(100, 300)
        self.checkbox.resize(140, 40)

        # Login Button
        self.button = QtWidgets.QPushButton("LOGIN", self)
        self.button.clicked.connect(self.clicked)
        self.button.setStyleSheet("color: white;" "background-color: #1070a2;" "border :1px solid #1070a2;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;" "letter-spacing : 5px")
        self.button.setFont(QFont('Bold', 10, weight=QFont.Bold))
        self.button.resize(140, 40)
        self.button.move(80, 340)

        # Invalid Identity Message
        self.errorlabel = QtWidgets.QLabel(self)
        self.errorlabel.resize(280, 40)
        self.errorlabel.setText("Invalid Identity! Username and Face Doesn't Match")
        self.errorlabel.move(10, 390)
        self.errorlabel.setAlignment(Qt.AlignCenter)
        self.errorlabel.setStyleSheet("color: white;" "background-color: red;" "border :1px solid red;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;")
        self.errorlabel.setVisible(False)

    def Blank_Label_Timer(self):
        self.blanklabel.setVisible(False)

    def Error_Label(self, text):
        self.blanklabel = QtWidgets.QLabel(self)
        self.blanklabel.resize(280, 40)
        self.blanklabel.setText(text)
        self.blanklabel.setAlignment(Qt.AlignCenter)
        self.blanklabel.move(10, 390)
        self.blanklabel.setStyleSheet("color: white;" "background-color: red;" "border :1px solid red;" "border-top-left-radius :4px;" "border-top-right-radius : 4px;" "border-bottom-left-radius : 4px;" "border-bottom-right-radius : 4px;")
        self.blanklabel.setVisible(True)
        blanklabeltimer = QTimer(self)
        blanklabeltimer.timeout.connect(self.Blank_Label_Timer)
        blanklabeltimer.start(5000)

    def Error_Label_Timer(self):
        self.errorlabel.setVisible(False)

    def clicked(self):
        username = self.userfield.text()
        password = self.passfield.text()
        if username == '' or password == '':
            self.Error_Label("Please Fill Up Username and Password")

        else:
            found_student = False
            for each_student in students:
                if "username" in each_student and "password" in each_student:
                    if each_student["username"] == username and each_student["password"] == password:
                        found_student = True
                        name_from_database = each_student["name"]
                        break

            if found_student:
                self.errorlabel.setVisible(False)

                if self.checkbox.isChecked():
                    name_from_recognition_system = recognition(take_picture=False)
                else:
                    name_from_recognition_system = recognition(take_picture=True)

                if name_from_recognition_system == name_from_database:
                    self.close()
                    cap = cv2.VideoCapture(0)

                    while True:
                        ret, frame = cap.read()
                        ## START OUTPUT WINDOW
                        output = cv2.imread('output.png')
                        output = cv2.resize(output, (500, 600))
                        cv2.putText(output, "Student Name: {}".format(name_from_recognition_system), (10, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                        now = datetime.datetime.now()
                        current_time = now.strftime("%H:%M:%S")

                        n = 250
                        if Multiple_Faces_Detection.MultipleFacesDetector(frame) == 1:
                            n += 50
                            cv2.putText(output, "Anomaly Type: Multiple Students at Desk", (10, n),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                            with open('detections.csv', mode='a', newline='') as f:
                                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                # write the data
                                writer.writerow([name_from_recognition_system, "Multiple Faces Detected", current_time])

                        elif Multiple_Faces_Detection.MultipleFacesDetector(frame) == 0:
                            n += 50
                            cv2.putText(output, "Anomaly Type: No Student at Desk", (10, n), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.7, (0, 0, 255), 2)
                            with open('detections.csv', mode='a', newline='') as f:
                                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                # write the data
                                writer.writerow([name_from_recognition_system, "No Faces Detected", current_time])

                        if Speaking_Detection.SpeakingDetection(frame) == 1:
                            n += 50
                            cv2.putText(output, "Anomaly Type: Student is Speaking", (10, n), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.7, (0, 0, 255), 2)
                            with open('detections.csv', mode='a', newline='') as f:
                                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                # write the data
                                writer.writerow([name_from_recognition_system, "Student Speaking", current_time])

                        if Head_Position_Detection.HeadPositionDetection(frame) == 1:
                            n += 50
                            cv2.putText(output, "Anomaly Type: Student is looking around", (10, n),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                            with open('detections.csv', mode='a', newline='') as f:
                                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                # write the data
                                writer.writerow([name_from_recognition_system, "Student Looking Around", current_time])

                        objectdetection_output, defect, score = Phone_Detection.PhoneDetection(frame)
                        if objectdetection_output == 1:
                            n += 50
                            defect_percentage = "{:.2%}".format(score)
                            cv2.putText(output, "Anomaly Type: {}, Accuracy: {}".format(defect, defect_percentage),
                                        (10, n), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                            with open('detections.csv', mode='a', newline='') as f:
                                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                # write the data
                                writer.writerow([name_from_recognition_system,
                                                 "Phone Usage Detected, Accuracy: {}".format(defect_percentage),
                                                 current_time])

                        ## END DETECTION TYPES
                        # cv2.imshow('Exam Proctoring System', cv2.resize(objectdetection_output, (800, 600)))
                        cv2.imshow("Exam Proctoring System", cv2.resize(frame, (800, 600)))
                        cv2.imshow('Output', output)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    cap.release()
                    cv2.destroyAllWindows()

                else:
                    self.invalidlabel = QtWidgets.QLabel(self)
                    self.invalidlabel.resize(280, 40)
                    self.invalidlabel.setText("Anomaly Type: Name and Face Not Matching,      Database Name: {}, "
                                              "Face Recognition Result: {}".format(name_from_database, name_from_recognition_system))
                    self.invalidlabel.setWordWrap(True)
                    self.invalidlabel.setAlignment(Qt.AlignCenter)
                    self.invalidlabel.move(10, 390)
                    self.invalidlabel.setStyleSheet("color: white;"
                                                    "background-color: red;"
                                                    "border :1px solid red;"
                                                    "border-top-left-radius :4px;"
                                                    "border-top-right-radius : 4px;"
                                                    "border-bottom-left-radius : 4px;"
                                                    "border-bottom-right-radius : 4px;")
                    self.invalidlabel.setVisible(True)
            else:
                self.Error_Label("Please Fill Up Correct Username and Password")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
