import cv2
import pickle
import cvzone
import numpy as np

width, height = 107, 48

with open("./file/carParkPos", "rb") as f:
    posList = pickle.load(f)


def checkParkingSpace(imgPro):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)
        # cvzone.putTextRect(img, str(count), (x, y+height-3),
        #                    scale=1, thickness=2, offset=0)
        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(
            img, pos, (pos[0]+width, pos[1]+height), color, thickness)

    cvzone.putTextRect(img, f'free: {spaceCounter}/ {len(posList)}', (100, 50),
                       scale=3, thickness=5, offset=20, colorR=(0, 200, 0))


cap = cv2.VideoCapture("./video/carPark.mp4")

while True:
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == cap.get(cv2.CAP_PROP_POS_FRAMES):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThershold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThershold, 5)

    kernel = np.ones((3, 3), np.uint8)
    imgdilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgdilate)

    cv2.imshow("img", img)
    cv2.imshow("imgGray", imgGray)
    cv2.imshow("imgBlur", imgBlur)
    cv2.imshow("imgThershold", imgThershold)
    cv2.imshow("imgMedian", imgMedian)
    cv2.imshow("imgdilate", imgdilate)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
