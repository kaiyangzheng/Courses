"""
Blur Purpose
- smooth an image when it has a lot of noise
    - camera sensors, problems in lighting
- blur removes the noise

Kernel or Window
- Window drawn over a specific area of the image
- Window size - kernel size
    - number of rows and columns
- Blur is applied to middle pixel as result of pixels around it
"""

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Methods of Blurring

"""
Averaging
- define kernel window over a specific portion
- window will compute pixel intensity of middle pixel as the average of the surrounding pixel intensities
- process happens throughout image (slide right, then down)
- higher kernel size = more blur (more pixels to add into the average calculation)
"""

average = cv.blur(img, (7,7))
cv.imshow("Average Blur", average)

"""
Gaussian Blur
- same as averaging, except average of surrounding pixels is weighted by a gaussian distribution
- less blurring compared to averaging
- more natural than averaging
"""

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

"""
Median Blur
- same as average, except the middle pixel is replaced with the median of the surrounding pixels
- more effective in reducing noise
- used in advanced computer vision that depend on reduction of noise
- not meant for high kernel sizes - image looks like painting
"""

median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

"""
Bilateral Blur
- Most effective 
- applies blurring, but retains edges of the image
- larger sigmaSpace - more blur
"""

bilateral = cv.bilateralFilter(img, d=10, sigmaColor=35, sigmaSpace=25)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)