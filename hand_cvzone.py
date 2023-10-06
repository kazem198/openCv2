import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(staticMode=False, maxHands=2,
                        modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
points = []
while True:
    success, frame = cap.read()
    if success:
        hands, img = detector.findHands(frame, draw=True, flipType=True)
        if hands:
            # Information for the first hand detected
            hand1 = hands[0]  # Get the first hand detected
            # List of 21 landmarks for the first hand
            lmList1 = hand1["lmList"]
            # Bounding box around the first hand (x,y,w,h coordinates)
            bbox1 = hand1["bbox"]
            center1 = hand1['center']  # Center coordinates of the first hand
            # Type of the first hand ("Left" or "Right")
            handType1 = hand1["type"]

        # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            # Print the count of fingers that are up
        #     print(f'H1 = {fingers1.count(1)}', end=" ")

        # Calculate distance between specific landmarks on the first hand and draw it on the image
            length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                      scale=10)
            # detector.
            # print(lmList1[4][0:2])
            points.append(lmList1[8][0:2])

        # for point in points:
        #     cv2.circle(frame, point, 2, (255, 0, 0), 2)

        for i in range((len(points))):
            cv2.line(frame, points[i], points[i-1],
                     (255, 0, 0), 2, 1)

        cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or success == False:
        cv2.destroyAllWindows()
        break

    if key == ord("a"):
        points = []


cap.release()
