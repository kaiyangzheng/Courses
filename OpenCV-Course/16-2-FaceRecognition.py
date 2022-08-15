"""
Face Recognition
"""
import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('Haar_Face.xml')

people = []
for person in os.listdir('Faces/train'):
    people.append(person)
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')

img = cv.imread(r'Faces/val/ben_afflek/3.jpg')
cv.imshow('Person', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print('Label: ' + str(label))
    print('Confidence: ' + str(confidence))
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)


