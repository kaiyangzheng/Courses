"""
Thresholding
- binarization of an image
- binary image - pixels are either 0 or 255 (black or white)

Simple way to do thresholding
- take a thresholding value and compare each pixel to the value
- if pixel intensity is less, set it to 0, otherwise set it to 255
- create a binary image 
"""

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

"""
Simple Thresholding
- grayscale image
- threshold value
- max value
- threshold type
"""
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh_inverse)

"""
Adaptive Thresholding
- downsides of simple thresholding
    - manually specify threshold value
- adaptive threshholding lets computer determine threshold value
arguments
- image
- max value
- adaptive method
- threshold type
- blockSize - kernel size for adaptive method
- c value - intensity of pixel neighborhood used to calculate threshold value
"""
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)