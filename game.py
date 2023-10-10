import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import cvzone
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# x is the distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # AX^2 + BX + C

detector = HandDetector(staticMode=False, maxHands=1,
                        modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)
# game
cx, cy = 200, 200
color = (255, 0, 255)
counter = 0
score = 0
startTime = time.time()
totolTime = 200


while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    if time.time()-startTime < totolTime:

        hands, img = detector.findHands(img, )

        if hands:
            # Information for the first hand detected
            lmList1 = hands[0]["lmList"]  # Get the first hand detected
            x, y, w, h = hands[0]["bbox"]
            x1, y1 = lmList1[5][0:2]
            x2, y2 = lmList1[17][0:2]
            distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
            # print(distance)
            A, B, C = coff
            distanceCM = A*(distance)**2 + B*distance + C

            if distanceCM < 40:
                if x < cx < x+w and y < cy < y+h:
                    counter = 1

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 12)
            cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x+5, y-10), 2)

            if counter:
                counter += 1
                color = (0, 255, 0)
                if counter == 7:
                    print(counter)
                    cx = np.random.random_integers(100, 1100)
                    cy = np.random.random_integers(100, 600)
                    color = (255, 0, 255)
                    score += 1
                    counter = 0

        # Draw button
        cv2.circle(img, (cx, cy), 30, color, cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 20, (255, 255, 255), 2)
        cv2.circle(img, (cx, cy), 30, (50, 50, 50), 2)

        # game Hub
        cvzone.putTextRect(
            img, f'time: {int(totolTime-(time.time()-startTime))}', (1000, 75), scale=3, offset=30)
        cvzone.putTextRect(
            img, f'score: {str(score).zfill(2)}', (60, 75), scale=3, offset=30)
    else:
        cvzone.putTextRect(
            img, 'Game Over', (400, 400), scale=5, thickness=7, offset=30)
        cvzone.putTextRect(
            img, f'your score: {score}', (450, 500), scale=3,  offset=20)

        cvzone.putTextRect(
            img, "to restart please press 'r' ", (460, 575), scale=2,  offset=10)

    cv2.imshow("img", img)
    key = cv2.waitKey(1)

    if key == ord("r"):
        startTime = time.time()
        score = 0

    if key & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
