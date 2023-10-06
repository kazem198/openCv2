import cv2
import numpy as np
from tracker import *

tracker = EuclideanDistTracker()
cap = cv2.VideoCapture("./images/highway.mp4")
mog = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)


while True:
    success, frame = cap.read()
    # print(frame.)
    if success == True:
        # print(frame.shape)
        rio = frame[300:720, 400:850]
        # rio = cv2.bilateralFilter(rio, 3, 0, 0)
        # rio = cv2.GaussianBlur(rio, (1, 1), 0)
        # rio_gray = cv2.cvtColor(rio, cv2.COLOR_BGR2GRAY)
        mask = mog.apply(rio)
        _, thresh = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY_INV)

        andrio = cv2.bitwise_and(rio, rio, mask=thresh)
        andrio = cv2.bitwise_not(andrio)
        cv2.imshow("and", andrio)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)
        # print(len(contours))/
        cv2.imshow("rio", rio)
        cv2.imshow("mask", mask)
        cv2.imshow("thersh", thresh)
        detections = []
        for contour in contours:
            if cv2.contourArea(contour) > 100:

                x, y, w, h = cv2.boundingRect(contour)
                detections.append([x, y, w, h])
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        boxes_ids = tracker.update(detections)

        for box_id in boxes_ids:

            x, y, w, h, id = box_id
            print(x, y)

            cv2.putText(rio, str(id), (x, y),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        # cv2.rectangle(rio, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # cv2.imshow("mask", mask)
        cv2.imshow("frame", frame)

    if cv2.waitKey(20) == ord("q") or success == False:
        cv2.destroyAllWindows()
        break

cap.release()
