import cv2
import os
import numpy as np
from PIL import Image
import pickle

image_dir = "C:\\Users\\Harin\\Documents\s\Jarvis\\RecognitionModels\\Samples"
face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\Harin\\Documents\s\Jarvis\\RecognitionModels\\haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-")
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            pil_image = Image.open(path).convert("L")
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            faces = face_cascade.detectMultiScale(image_array, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

try:
    os.remove("C:\\Users\\Harin\\Documents\s\Jarvis\\RecognitionModels\\trainer.yml")
except Exception as e:
    pass
try:
    os.remove(
        "C:\\Users\\Harin\\Documents\s\Jarvis\\RecognitionModels\\labels.pickle")
except Exception as e:
    pass

with open("C:\\Users\\Harin\\Documents\s\Jarvis\\RecognitionModels\\labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save(
    "C:\\Users\\Harin\\Documents\s\Jarvis\RecognitionModels\\trainer.yml")
