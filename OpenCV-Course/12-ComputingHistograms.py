"""
Histograms
- visualize distribution of pixel intensities in an image
- can compute for greyscale and RGB images
- helpful in analyzing image and equalize image so that it is more uniform
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype="uint8")
"""
Histogram for greyscale image
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked', mask)

"""
cv.calcHist
1. list of images
2. number of channels - index of channel we want to compute histogram for
3. mask - optional, if we want to compute histogram for a subset of pixels
4. histogram size - number of bins in histogram 
5. Ranges of pixel values - 0-256 for greyscale images
"""
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

"""
Histogram for RGB image
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

plt.figure()
plt.title('RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i , col in enumerate(colors):
    hist = cv.calcHist([img], [i], None [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)