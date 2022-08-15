import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], np.uint8)

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img = cv.merge([b, g, r])
cv.imshow('Merged', merged_img)

cv.waitKey(0)
