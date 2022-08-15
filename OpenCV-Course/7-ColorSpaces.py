import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale - show distribution of pixel intensities
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV - Hue Saturation Value - based on how humans think and concieve color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b* - L*a*b* is a color space that is more perceptually uniform than RGB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b*', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_brg = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_brg)

cv.waitKey(0)
