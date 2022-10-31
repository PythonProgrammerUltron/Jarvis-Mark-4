import numpy as np
import cv2
import os
from PIL import Image
import pickle

face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
x = input("Enter your name: ")
count = 0
newSample = f"C:\\Users\\Harin\\Documents\\Jarvis\\RecognitionModels\\Samples\\{x}"
os.makedirs(newSample)

while True:
    ret, img = cap.read()
    cv2.imshow("Frame", img)

    if not ret:
        break

    k = cv2.waitKey(1)

    if k:
        break

    if k % 256 == 32:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            img_item = f"{newSample}\\Sample"+str(count)+".jpg"
            cv2.imwrite(img_item, roi_color)
            count += 1

cap.release
cv2.destroyAllWindows
