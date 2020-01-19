import cv2
import sys
from time import sleep

cascPath = "haarcascade_frontalface_alt.xml"
#haarcascade_frontalface_alt.xml - 9/10
# haarcascade_frontalface_alt.2xml - 8.10
# Front_Face_Trained.xml 6/10

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE,
        minSize=(30, 30),
    )

    # Display FPS
    timer = cv2.getTickCount()
    fps = (cv2.getTickFrequency() / (cv2.getTickCount() - timer)/10000)
    cv2.putText(img=frame, text="Fps : " + str(int(fps)), org=(10, 25), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(
        255, 255, 255), thickness=1)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
