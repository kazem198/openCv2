import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import cvzone

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


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=False)

    if hands:
        # Information for the first hand detected
        lmList1 = hands[0]["lmList"]  # Get the first hand detected
        x, y, w, h = hands[0]["bbox"]
        x1, y1 = lmList1[5][0:2]
        x2, y2 = lmList1[17][0:2]
        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
        print(distance)
        A, B, C = coff
        distanceCM = A*(distance)**2 + B*distance + C
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 12)
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x+5, y-10), 2)

    cv2.circle(img, (cx, cy), 30, color, cv2.FILLED)
    cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
    cv2.circle(img, (cx, cy), 20, (255, 255, 255), 2)
    cv2.circle(img, (cx, cy), 30, (50, 50, 50), 2)

    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
