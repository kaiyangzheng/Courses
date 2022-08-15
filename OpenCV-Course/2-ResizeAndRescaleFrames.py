import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos, and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread('Photos/cat.jpg')
cv.imshow('Image', rescaleFrame(img))

# reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)
