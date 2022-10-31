# Modules Imported


from ast import Return
import os
from os.path import exists
import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
from mss import mss
import mediapipe as mp
import autopy
import pickle
from imutils.video import VideoStream
from imutils.video import fps
import argparse
import time
from datetime import datetime
import math
import pyautogui
import pyttsx3
import playsound
import random
from random import randint
import pyjokes
import speech_recognition as sr
import smtplib
import wikipedia
from googlesearch import *
import urllib
import urllib.request
import re
import webbrowser
import pywhatkit
import requests

# voice setup
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# PathofDriver = "C:\\Users\\Harin\\Documents\\Jarvis\\chromedriver.exe"
# driver = webdriver.Chrome(PathofDriver, options=chrome_options)
# driver.maximize_window()

# Website = f'https://ttsmp3.com/text-to-speech/British%20English/'

# driver.get(Website)
# ButtonSelection = Select(driver.find_element(
#     by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')

# GUI Structure and Design


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("background.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.Bg_rt = QtWidgets.QLabel(self.centralwidget)
        self.Bg_rt.setGeometry(QtCore.QRect(0, -3, 231, 199))
        self.Bg_rt.setText("")
        self.Bg_rt.setPixmap(QtGui.QPixmap("bg_rt.png"))
        self.Bg_rt.setScaledContents(True)
        self.Bg_rt.setObjectName("Bg_rt")
        self.Bg_lft = QtWidgets.QLabel(self.centralwidget)
        self.Bg_lft.setGeometry(QtCore.QRect(502, 405, 301, 197))
        self.Bg_lft.setText("")
        self.Bg_lft.setPixmap(QtGui.QPixmap("bg_lft.png"))
        self.Bg_lft.setScaledContents(True)
        self.Bg_lft.setObjectName("Bg_lft")
        self.patch = QtWidgets.QLabel(self.centralwidget)
        self.patch.setGeometry(QtCore.QRect(510, 420, 141, 111))
        self.patch.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.978, y1:0.965909, x2:0.039, y2:0, stop:0 rgba(18, 12, 14, 255), stop:1 rgba(10, 38, 49, 255));")
        self.patch.setText("")
        self.patch.setScaledContents(True)
        self.patch.setObjectName("patch")
        self.User_Information = QtWidgets.QTextBrowser(self.centralwidget)
        self.User_Information.setGeometry(QtCore.QRect(510, 443, 141, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.User_Information.setFont(font)
        self.User_Information.setStyleSheet("background:transparent;\n"
                                            "color: rgb(0, 254, 253);\n"
                                            "border:none;")
        self.User_Information.setObjectName("User_Information")
        self.User_Pic = QtWidgets.QLabel(self.centralwidget)
        self.User_Pic.setGeometry(QtCore.QRect(665, 440, 78, 79))
        self.User_Pic.setText("")
        self.User_Pic.setScaledContents(True)
        self.User_Pic.setObjectName("User_Pic")
        self.Camera_Feed = QtWidgets.QLabel(self.centralwidget)
        self.Camera_Feed.setGeometry(QtCore.QRect(50, 68, 431, 313))
        self.Camera_Feed.setStyleSheet("background:transparent;\n"
                                       "border:none;")
        self.Camera_Feed.setText("")
        self.Camera_Feed.setScaledContents(True)
        self.Camera_Feed.setObjectName("Camera_Feed")
        self.Date = QtWidgets.QTextBrowser(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(530, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setStyleSheet("background:transparent;\n"
                                "color: rgb(0, 254, 253);\n"
                                "border:none;")
        self.Date.setObjectName("Date")
        self.Time = QtWidgets.QTextBrowser(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(640, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet("background:transparent;\n"
                                "color: rgb(0, 254, 253);\n"
                                "border:none;")
        self.Time.setObjectName("Time")
        self.Status = QtWidgets.QTextBrowser(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(610, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setStyleSheet("background:transparent;\n"
                                  "color: rgb(0, 254, 253);\n"
                                  "border:none;")
        self.Status.setObjectName("Status")
        self.StatusImg = QtWidgets.QLabel(self.centralwidget)
        self.StatusImg.setGeometry(QtCore.QRect(530, 147, 81, 61))
        self.StatusImg.setText("")
        self.StatusImg.setScaledContents(True)
        self.StatusImg.setObjectName("StatusImg")
        self.JarvisName = QtWidgets.QLabel(self.centralwidget)
        self.JarvisName.setGeometry(QtCore.QRect(486, 283, 231, 171))
        self.JarvisName.setText("")
        self.JarvisName.setPixmap(QtGui.QPixmap("JarvisName.png"))
        self.JarvisName.setScaledContents(True)
        self.JarvisName.setObjectName("JarvisName")
        self.Version = QtWidgets.QLabel(self.centralwidget)
        self.Version.setGeometry(QtCore.QRect(690, 362, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Version.setFont(font)
        self.Version.setStyleSheet("color:rgb(10, 38, 48)")
        self.Version.setObjectName("Version")
        self.LensButton = QtWidgets.QPushButton(self.centralwidget)
        self.LensButton.setGeometry(QtCore.QRect(600, 230, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LensButton.setFont(font)
        self.LensButton.setStyleSheet("background-color: rgb(2, 254, 253);\n"
                                      "color: rgb(10, 38, 47);\n"
                                      "border-radius:10px;")
        self.LensButton.setObjectName("LensButton")
        self.RecognitionMode = QtWidgets.QPushButton(self.centralwidget)
        self.RecognitionMode.setGeometry(QtCore.QRect(600, 270, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RecognitionMode.setFont(font)
        self.RecognitionMode.setStyleSheet("background-color: rgb(2, 254, 253);\n"
                                           "color: rgb(10, 38, 47);\n"
                                           "border-radius:10px;")
        self.RecognitionMode.setObjectName("RecognitionMode")
        self.ScanningMode = QtWidgets.QPushButton(self.centralwidget)
        self.ScanningMode.setGeometry(QtCore.QRect(600, 310, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ScanningMode.setFont(font)
        self.ScanningMode.setStyleSheet("background-color: rgb(2, 254, 253);\n"
                                        "color: rgb(10, 38, 47);\n"
                                        "border-radius:10px;")
        self.ScanningMode.setObjectName("ScanningMode")
        self.Patch_2 = QtWidgets.QLabel(self.centralwidget)
        self.Patch_2.setGeometry(QtCore.QRect(527, 217, 218, 137))
        self.Patch_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.852, x2:0, y2:0.097, stop:0 rgba(19, 40, 57, 255), stop:1 rgba(4, 65, 83, 255));")
        self.Patch_2.setText("")
        self.Patch_2.setObjectName("Patch_2")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(150, 460, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Run.setFont(font)
        self.Run.setStyleSheet("color: rgb(10, 38, 47);\n"
                               "border-radius:10px;\n"
                               "background-color: rgb(70, 255, 156);")
        self.Run.setObjectName("Run")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(280, 460, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("color: rgb(10, 38, 47);\n"
                                "border-radius:10px;\n"
                                "background-color: rgb(255, 96, 82);")
        self.Exit.setObjectName("Exit")
        self.Background.raise_()
        self.Patch_2.raise_()
        self.Bg_rt.raise_()
        self.Bg_lft.raise_()
        self.patch.raise_()
        self.User_Information.raise_()
        self.User_Pic.raise_()
        self.Date.raise_()
        self.Time.raise_()
        self.Status.raise_()
        self.StatusImg.raise_()
        self.JarvisName.raise_()
        self.Version.raise_()
        self.LensButton.raise_()
        self.RecognitionMode.raise_()
        self.ScanningMode.raise_()
        self.Run.raise_()
        self.Camera_Feed.raise_()
        self.Exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.User_Information.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Time.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
                                       "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.Version.setText(_translate("MainWindow", "Ver: 2.0"))
        self.LensButton.setText(_translate("MainWindow", "Lens"))
        self.RecognitionMode.setText(_translate("MainWindow", "Recognise"))
        self.ScanningMode.setText(_translate("MainWindow", "Scan"))
        self.Run.setText(_translate("MainWindow", "RUN"))
        self.Exit.setText(_translate("MainWindow", "Exit"))


Camera = cv2.VideoCapture(1)


# GUI Working


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint)
        self.ui.setupUi(self)

        self.ui.Run.clicked.connect(self.Run)
        self.ui.Exit.clicked.connect(self.Exit)
        self.ui.LensButton.clicked.connect(self.Lens)
        self.ui.RecognitionMode.clicked.connect(self.Recognition)
        self.ui.ScanningMode.clicked.connect(self.Scanning)

        self.ui.movie = QtGui.QMovie(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\background.png")
        self.ui.Background.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "DC:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\bg_rt.png")
        self.ui.Bg_rt.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\bg_lft.png")
        self.ui.Bg_lft.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\dp.jpg")
        self.ui.User_Pic.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.User_Information.setText("NAME: HARI NICKLE \n"
                                         "OCCUPATION: YOUTUBER \n"
                                         "EDUCATION: SECONDARY LEVEL")
        self.ui.User_Information.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.User_Information.show()
        self.ui.movie = QtGui.QMovie(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\JarvisName.png")
        self.ui.JarvisName.setMovie(self.ui.movie)
        self.ui.movie.start()

    def Run(self):
        startExecution.start()

    def Exit(self):
        quit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def CameraOutput(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.ui.Camera_Feed.setPixmap(QPixmap.fromImage(img))
        self.ui.Camera_Feed.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def Lens(self):
        playsound.playsound(
            "C:\\Users\\Harin\\Documents\\Jarvis\\BackgroundMusic\\dink.mp3")

        self.ui.StatusImg.setPixmap(QtGui.QPixmap(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\camera.png"))
        self.ui.StatusImg.setScaledContents(True)
        self.ui.StatusImg.show()

        self.ui.Status.setText("EYE VIEW")
        self.ui.Status.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.Status.show()

        timer = QTimer(self)
        timer.timeout.connect(self.RealTimeClock)
        timer.start(1000)

        pTime = 0
        cTime = 0

        cap = Camera

        while (cap.isOpened()):
            ret, frame = cap.read()

            if ret == True:
                cTime = time.time()
                Fps = 1 / (cTime - pTime)
                pTime = cTime

                formatted_string = "{:.2f}".format(Fps)
                Fps = float(formatted_string)

                self.CameraOutput(frame, 1)

                cv2.waitKey()

        cap.release()
        cv2.destroyAllWindows()

    def Recognition(self):
        playsound.playsound(
            "C:\\Users\\Harin\\Documents\\Jarvis\\BackgroundMusic\\dink.mp3")

        self.ui.StatusImg.setPixmap(QtGui.QPixmap(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\Recogniser.png"))
        self.ui.StatusImg.setScaledContents(True)
        self.ui.StatusImg.show()

        self.ui.Status.setText("RECOGNITION MODE")
        self.ui.Status.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.Status.show()

        timer = QTimer(self)
        timer.timeout.connect(self.RealTimeClock)
        timer.start(1000)

        pTime = 0
        cTime = 0

        face_cascade = cv2.CascadeClassifier(
            "C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(
            "C:\\Users\\Harin\\Document\\Jarvis\\RecognitionModels\\trainer.yml")

        labels = {"person_name": 1}
        with open("C:\\Users\\Harin\\Document\\Jarvis\\RecognitionModels\\labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}

        cap = Camera

        while (cap.isOpened()):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]

                color1 = (57, 255, 20)
                color2 = (0, 0, 128)
                stroke = 2
                width = x + w
                height = y + h

                id_, conf = recognizer.predict(roi_gray)
                if conf >= 4 and conf <= 85:
                    font = cv2.FONT_HERSHEY_COMPLEX
                    name = labels[id_]
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1,
                                color1, stroke, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (width, height),
                                  color1, stroke)

                else:
                    font = cv2.FONT_HERSHEY_COMPLEX
                    unknown = "Unknown"
                    stroke = 2
                    cv2.putText(frame, unknown, (x, y), font,
                                1, color2, stroke, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (width, height),
                                  color2, stroke)

            if ret == True:
                cTime = time.time()
                Fps = 1 / (cTime - pTime)
                pTime = cTime

                formatted_string = "{:.2f}".format(Fps)
                Fps = float(formatted_string)

                self.CameraOutput(frame, 1)

                cv2.waitKey()
        cap.release()
        cv2.destroyAllWindows()

    def Scanning(self):
        playsound.playsound(
            "C:\\Users\\Harin\\Documents\\Jarvis\\BackgroundMusic\\dink.mp3")

        self.ui.StatusImg.setPixmap(QtGui.QPixmap(
            "C:\\Users\\Harin\\Documents\\Jarvis\\GUIComponents\\scan.png"))
        self.ui.StatusImg.setScaledContents(True)
        self.ui.StatusImg.show()

        self.ui.Status.setText("SCANNING MODE")
        self.ui.Status.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.Status.show()

        timer = QTimer(self)
        timer.timeout.connect(self.RealTimeClock)
        timer.start(1000)

        pTime = 0
        cTime = 0

        thres = 0.45
        nms_threshold = 0.2
        cap = Camera

        classNames = []
        classFile = "C:\\Users\\Harin\\Document\\Jarvis\\ScaningModels\\coco.names"
        with open(classFile, 'rt') as f:
            classNames = [line.rstrip() for line in f]

        configPath = "C:\\Users\\Harin\\Documents\\Jarvis\\ScaningModels\\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        weightsPath = "C:\\Users\\Harin\\Document\\Jarvis\\ScaningModels\\frozen_inference_graph.pb"

        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        while True:
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            bbox = list(bbox)
            confs = list(np.array(confs).reshape(1, -1)[0])
            confs = list(map(float, confs))

            indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

            for i in indices:
                i = i[0]
                box = bbox[i]
                x, y, w, h = box[0], box[1], box[2], box[3]
                cv2.rectangle(img, (x, y), (x+w, h+y),
                              color=(0, 255, 0), thickness=2)
                cv2.putText(img, classNames[classIds[i][0]-1].upper(), (box[0]+10, box[1]+30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cTime = time.time()
            Fps = 1 / (cTime - pTime)
            pTime = cTime

            formatted_string = "{:.2f}".format(Fps)
            Fps = float(formatted_string)

            self.CameraOutput(img, 1)

            cv2.waitKey(1)

    def showDate(self):
        label_date = datetime.now().strftime("%a, %b %d, %Y")
        self.ui.Date.setText(label_date)
        self.ui.Date.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.Date.show()

    def RealTimeClock(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.ui.Time.setText(label_time)
        self.ui.Time.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ui.Time.show()


# AI Program Speaking


def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    lengthcode = len(Text)

    if lengthcode > 30:
        engine.setProperty('rate', 200)

    else:
        engine.setProperty('rate', 170)

    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")


# User Audio Input


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 50
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        r = requests.post('https://api.carterapi.com/v0/chat', json={
            'api_key': 'xMu1tKqB5xNqbSWlQHOhuLQW7DHNRxqE',
            'query': query,
            'uuid': "user-id-123",
        })
        agent_response = r.json()
        speak(agent_response['output']['text'])

    except Exception as e:
        print("Say that again please!")
        return "None"
    query = query.lower()
    return query


# Greeting Function


def Wish():
    strTime = datetime.now().strftime("%H:%M:%S")
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(
            f"Good Morning Sir! its {strTime}. Please tell me how may I help you?")

    elif hour >= 12 and hour < 18:
        speak(
            f"Good Afternoon Sir! its {strTime}. Please tell me how may I help you?")

    else:
        speak(
            f"Good Evening Sir! its {strTime}. Please tell me how may I help you?")


# Program Introduction


def Intro():
    speak("Allow me to introduce myself! I am JARVIS, a Virtual Artificial Intelligence. And I am here to assist you with a variety of tasks since best I can! 24 Hours a day, 7 days a week. Importing all prefrences from Home Interface, Systems are now fully operational!")


# Online E-Mail Sending


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email Address', 'Your Email Password')
    server.sendmail('Your Email Address', to, content)
    server.close()


# Program Quiting


def quit():
    sys.exit()


class MainThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # face_cascade = cv2.CascadeClassifier(
        #     "C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\haarcascade_frontalface_default.xml")
        # recognizer = cv2.face.LBPHFaceRecognizer_create()
        # recognizer.read(
        #     "C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\trainer.yml")

        # labels = {"person_name": 1}
        # with open("C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\labels.pickle", 'rb') as f:
        #     og_labels = pickle.load(f)
        #     labels = {v: k for k, v in og_labels.items()}

        # cap = Camera

        # ret, frame = cap.read()

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(
        #     gray, scaleFactor=1.5, minNeighbors=5)

        # for (x, y, w, h) in faces:
        #     roi_gray = gray[y:y+h, x:x+w]

        #     id_, conf = recognizer.predict(roi_gray)
        #     if conf >= 4 and conf <= 85:
        #         name = labels[id_]
        #         name = "{}".format(name.upper(), cv2.FONT_HERSHEY_COMPLEX)

        self.TaskExecution()

        # else:
        #     unknown = "Unknown"
        #     unknown = "{}".format(
        #         unknown.upper(), cv2.FONT_HERSHEY_COMPLEX)

        #     speak(
        #         "Facial Recognition Failed! Unauthorized users are not permitted to access this app.")

    def TaskExecution(self):
        speak("Allow me to introduce myself! I am JARVIS, a Virtual Artificial Intelligence. And I am here to assist you with a variety of tasks since best I can! 24 Hours a day, 7 days a week. Importing all prefrences from Home Interface, Systems are now fully operational!")

        while True:
            self.query = takeCommand()

            # Logic for executing tasks based on query
            if "hello" in self.query:
                speak("Hello Sir! How may I help you?")

            # time
            elif 'time' in self.query:  # tell time
                strTime = datetime.now().strftime("%H:%M:%S")
                speak(f"{strTime}")

            # introduce yourself
            elif 'introduce yourself' in self.query or 'your introduction' in self.query or 'who are you' in self.query:
                Intro()

            # play music
            elif 'play' in self.query:
                song = self.query.replace('play', '')
                speak('Playing ' + song)
                pywhatkit.playonyt(song)

            # youtube
            elif 'youtube' in self.query:
                speak("Opening Youtube")
                webbrowser.open("youtube.com")
                # wait for 1 second
                time.sleep(1)
                # pywhatkit pres tab 3 times
                pywhatkit.press("tab")
                pywhatkit.press("tab")
                pywhatkit.press("tab")

            # wake up
            elif 'wake up' in self.query:
                speak("I am already awake sir!")
                # pywhatkit play Should I stay or should I go
                pywhatkit.playonyt("Should I stay or should I go")

            # Start a new project on github
            elif 'start a new project' in self.query:
                speak("Starting a new project on github")
                webbrowser.open("github.com")


startExecution = MainThread()


app = QtWidgets.QApplication(sys.argv)
Jarvis = Main()
display_monitor = 1
monitor = QDesktopWidget().screenGeometry(display_monitor)
Jarvis.move(monitor.left(), monitor.top())
Jarvis.show()
exit(app.exec_())
