import cv2

# again we have to use the trained model
cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# we will use real-time video (camera) - 0 means open the default camera
video_capture = cv2.VideoCapture(0)

# setting the width and height of the video window
video_capture.set(3, 640)
video_capture.set(4, 480)

while True:

    # returns the next video frame (the img is the important)
    ret, img = video_capture.read()

    # transform into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # using face detection algorithm with the trained classifier
    detected_faces = cascade_classifier.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

    # draw the faces (rectangles) in every video frame
    for (x, y, width, height) in detected_faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 10)

    # title of the video window
    cv2.imshow('Real-Time Face Detection', img)

    # we wait for a key to be pressed - press 'ESC' to quit
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

# destroy and release the camera etc.
video_capture.release()
cv2.destroyAllWindows()
