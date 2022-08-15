import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# 2. Paint parts of the image a certain color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red square', blank)

# 3. Draw a rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 4. Draw a circle
cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

# 5. Draw a line
cv.line(blank, (100, 250),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 6. Write text
cv.putText(blank, 'Hello', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow('Text', blank)


cv.waitKey(0)
