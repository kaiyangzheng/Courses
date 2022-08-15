"""
Gradient and Edge Detection

Gradient
- Edge-like regions present in an image
- different from edges - edges are edges of a line, gradient is the change in intensity of an image
"""
import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""
Laplacion method
- computes the image gradient using the Laplacian operator
"""
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

"""
Sobel method
- computes gradient in x and y direction
"""
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

"""
Canny method
- used in most cases to detect edges in an image
- sobel for more advanced edge detection
"""
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)