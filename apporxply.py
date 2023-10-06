import cv2
import numpy as np


img = cv2.imread("./images/apporox.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
for con in contours:
    arc = cv2.arcLength(con, True)
    poly = cv2.approxPolyDP(con, 0.02 * arc, True)
    # print(poly.shape[0])
    (x, y), r = cv2.minEnclosingCircle(con)
    print(x, y)
    pos = np.ravel(poly)
    cv2.putText(img, str(poly.shape[0]), (int(x), int(y)),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # print(np.ravel(poly[0]))

cv2.imshow("thresh", mask)


cv2.imshow('img', img)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
