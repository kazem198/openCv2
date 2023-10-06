import cv2
import numpy as np

cap = cv2.VideoCapture("./video/solidWhiteRight.mp4")
# success, frame = cap.read()
# cv2.imwrite("Range.jpg", frame)
while True:
    success, frame = cap.read()
    if success:
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        colorLow = np.array([0, 0, 225])
        colorup = np.array([255, 100, 255])
        hsvFrame = cv2.GaussianBlur(hsvFrame, (15, 15), 0, 0)
        mask = cv2.inRange(hsvFrame, colorLow, colorup)
        _, thersh = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        canny = cv2.Canny(thersh, 200, 254)
        # contours, _ = cv2.findContours(
        # canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # for con in contours:
        # cv2.drawContours(frame, [con], -1, (255, 0, 0), 2)
        lines = cv2.HoughLinesP(canny, 1, np.pi/180, 80)
        if lines is not None:
            # preLine = []
            # for line in lines:
            #     x1, y1, x2, y2 = line[0]
            #     print("line", line[0])
            #     cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 10)
            #     preLine.append(line[0])
            #     print("preLine", preLine[0])
            #     if (x1-preLine[0][0] > 100):
            #         cv2.line(frame, (x1, y1),
            #                  (preLine[0][0], preLine[0][1]), (0, 255, 0), 3)
            #     preLine.clear()

            for i in range(len(lines)):
                x1, y1, x2, y2 = lines[i][0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 10)
                if (x1-lines[i-1][0][0] > 100):
                    # print(lines[i][0][2])
                    cv2.line(frame, (x1, y1),
                             (lines[i-1][0][0], lines[i-1][0][1]), (0, 255, 0), 3)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("thersh", thersh)
        cv2.imshow("canny", canny)

    if (cv2.waitKey(100) & 0xFF == ord("q") or success == False):
        cv2.destroyAllWindows()
        break


cap.release()
