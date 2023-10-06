import cv2
import numpy as np
from tracker import *

tracker = EuclideanDistTracker()


cap = cv2.VideoCapture("./images/vtest.avi")
# cap = cv2.VideoCapture("../../highway.mp4")
mog = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)
points = []


def removeId(id):

    pointes = np.array(points)
    print("1", pointes)
    for po in pointes:
        # print(po[4])
        point = np.delete(po, np.where(po[4] < id))
        # points.clear()
        # points.append(point)
    print("2", point)
    # points = point
    # for p in points:
    # p.
    print("id", id)
    pass


while True:
    success, frame = cap.read()
    if success:
        # print(frame.shape)
        rio = frame[0:200, 0: 250]

        mask = mog.apply(rio)
        # mask = cv2.dilate(mask, None)
        mask = cv2.erode(mask, (5, 5))
        mask = cv2.GaussianBlur(mask, (25, 25), 0)
        ret, mask = cv2.threshold(
            mask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        detections = []
        for con in contours:

            area = cv2.contourArea(con)

            if (area > 300):
                x, y, w, h = cv2.boundingRect(con)
                detections.append([x, y, w, h])
            boxes_ids = tracker.update(detections)

        for box in boxes_ids:
            cv2.rectangle(
                rio, (box[0], box[1]), (box[0]+box[2], box[1]+box[3]), (255, 0, 0), 2)
            # print(box)
            points.append(box)
            removeId(box[4])
        for point in points:
            # print(points)
            cv2.circle(rio, (point[0]+point[2],
                       point[1]+point[3]), 1, (0, 0, 255), 1)

        cv2.imshow("cap", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("rio", rio)

        if (cv2.waitKey(100) & 0xFF == ord("q") or success == False):
            cv2.destroyAllWindows()
            break
cap.release()
