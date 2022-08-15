"""
Face Recognition
- use opencv's built in face recognizer
- train on images in Faces train folder
"""
import os
import cv2 as cv
import numpy as np

p = []
for person in os.listdir('Faces/train'):
    p.append(person)

DIR = r'Faces/train'

haar_cascade = cv.CascadeClassifier('Haar_Face.xml')

features = []
labels = []

def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)
        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done')

features = np.array(features, dtype='object')
labels = np.array(labels)

# init face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train face recognizer on features and labels
face_recognizer.train(features, labels)

face_recognizer.save('face_recognizer.json')
np.save('features.npy', features)
np.save('labels.npy', labels)
