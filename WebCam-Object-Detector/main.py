
import cv2


def main():
    video = cv2.VideoCapture(0)
    static_back = None
    while video.isOpened():
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if static_back is None:
            static_back = gray
            continue

        # Diff between Static BG and GausianBlur BG
        diff_frame = cv2.absdiff(static_back, gray)

        # If change in between static background and
        # current frame is greater than 30 it will show white color
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=0)

        # Finding contour of moving object
        (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            # Draw stroke around moving object
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 8)
            # making green rectangle arround the moving object
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.drawMarker(frame, (x, y), (0, 0, 255), thickness=3)

        # Frames per Second
        timer = cv2.getTickCount()
        fps = (cv2.getTickFrequency() /
               (cv2.getTickCount() - timer)/10000)
        cv2.putText(frame, "Fps : " + str(int(fps)), (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1)

        # Displaying image
        cv2.imshow("Threshold Frame", thresh_frame)
        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


if __name__ in "__main__":
    main()
