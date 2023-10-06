import cv2
import numpy as np

img = cv2.imread("./images/somatic.jpg")
canny = cv2.Canny(img, 180, 220)

contours, _ = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# print(contours.shape)
for con in contours:
    cv2.drawContours(img, con, -1, (0, 0, 255), 2)

print(len(contours))
cv2.imshow("img", img)
cv2.imshow("canny", canny)


if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
