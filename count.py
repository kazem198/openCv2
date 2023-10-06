import cv2
import numpy as np
img = cv2.imread('./images/tot2.jpg')
# lowerb = np.array([236, 158, 125])
# upperb = np.array([255, 255, 255])
lower_red = np.array([150, 100, 80])
upper_red = np.array([180, 255, 255])
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(imgHsv, lower_red, upper_red)
# erode = cv2.erode(mask, (25, 25), iterations=15)
canny = cv2.Canny(mask, 250, 254)


cv2.imshow("img", img)
cv2.imshow("mask", mask)
# cv2.imshow("erode", erode)
cv2.imshow("canny", canny)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
