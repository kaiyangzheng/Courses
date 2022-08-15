"""
Face Detection with Haar Cascades
- detects presence of a face in an image
- performed using classifier
    - classifier is an algorithm that is either positive or negative - face or not a cace
    - trained with thousands of faces
- opencv comes with pre-trained classifiers that can be used to detect faces
- 2 main classifiers:
    - Haar Cascades
    - LBP (Local Binary Pattern) 
        - more advanced classifier - not as prone to noise
"""
import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Person', img)

"""
Convert to grayscale
- doesn't use color information to detect faces
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""
Read in the classifier - Haar Cascades
"""
haar_cascade = cv.CascadeClassifier('Haar_Face.xml')

"""
One way to reduce sensitivity of the classifier to noise
- modify scaleFactor and minNeighbors
- scaleFactor - how much the image size is reduced at each image scale
- minNeighbors - how many neighbors each candidate rectangle should have to retain it
"""
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1)
print("Num faces found: " + str(len(faces_rect)))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Faces', img)
cv.waitKey(0)