import cv2
import numpy as np
import pickle

cap = cv2.VideoCapture("video/carPark.mp4")
width, height = 107, 48
with open("carParkPos", "rb") as f:
    posList = pickle.load(f)
# print(posList)


def detectCar(img):
    for pos in posList:
        x, y = pos
        # parkPos=x+width, y+height
        posImage = img[y:y+height, x: x+width]
        d = cv2.countNonZero(posImage)
        if (d > 600):

            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 3)
        else:
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 3)


while True:
    ret, frame = cap.read()

    gryFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gryFrame = cv2.GaussianBlur(gryFrame, (3, 3), 1)
    threshFrame = cv2.adaptiveThreshold(
        gryFrame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    # threshFrame = cv2.medianBlur(gryFrame, 1)

    detectCar(threshFrame)

    if ret:
        cv2.imshow("carParking", frame)
        cv2.imshow("filter", threshFrame)
        # cv2.imshow("blob", blob)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
