import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
color = (255, 0, 255)


cx, cy, w, h = 100, 100, 200, 200


class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, bbox1):
        cx, cy = self.posCenter
        w, h = self.size

        if (cx-(w//2) < bbox1[0] < (cx+(w//2))) and (cy-(h//2) < bbox1[1] < cy+(h//2)):
            color = (0, 255, 0)
            self.posCenter = bbox1


recList = []
for i in range(5):
    recList.append(DragRect([i*250+150, 150]))

# rect = DragRect([150, 150])

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame, flipType=False)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = lmList1[8][0:2]

        length, info, img = detector.findDistance(
            lmList1[8][0:2], lmList1[12][0:2], frame, color=(255, 0, 255))
        # print(length)
        if length < 50:
            # rect.update(bbox1)
            for rect in recList:
                rect.update(bbox1)
            # call update here

            # else:
            #     color = (255, 0, 255)
        # print(bbox1)
    for rect in recList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(frame, (cx-(w//2), cy-(h//2)),
                      (cx+(w//2), cy+(h//2)), color, cv2.FILLED)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break


cap.release()
