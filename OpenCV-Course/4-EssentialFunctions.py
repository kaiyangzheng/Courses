import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

# Converting an image to greyscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur - removes noise in image

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding the image

eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize the image

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
