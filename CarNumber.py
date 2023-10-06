import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

img = cv2.imread("./images/pelak4.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bilateral = cv2.bilateralFilter(img_gray, 9, 25, 10)
# _, bilateral = cv2.threshold(img_gray, 110, 254, cv2.THRESH_BINARY)
canny = cv2.Canny(bilateral, 200, 240)
platLocation = []
# print(len(platLocation))
contours, _ = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for con in contours:
    peri = cv2.arcLength(con, True)
    conArea = cv2.contourArea(con)
    app = cv2.approxPolyDP(con, 0.02 * peri, True)
    # print(app.shape[0])

    if app.shape[0] == 4:
        if (peri > 200):
            cv2.drawContours(img, [app], -1, (0, 0, 255), 2)
            platLocation = con

            # print(img.shape)
            print(con.shape)
            # print(con[:, :, 0])
            x = con[:, :, 0]
            y = con[:, :, 1]
            y1, x1 = np.min(y), np.min(x)
            y2, x2 = np.max(y), np.max(x)
            cropedImg = img[y1:y2, x1:x2]


mask = np.zeros(img_gray.shape, np.uint8)
ploatmask = cv2.drawContours(mask, [platLocation], -1, 255, -1)
imgMsk = cv2.bitwise_and(ploatmask, ploatmask, mask=mask)


# y, x = np.where(ploatmask == 255)
# y1, x1 = np.min(y), np.min(x)
# y2, x2 = np.max(y), np.max(x)
# cropedImg = img[y1:y2, x1:x2]


cv2.imshow("img", img)
cv2.imshow("imgMsk", imgMsk)
cv2.imshow("bilateral", bilateral)
cv2.imshow("ploatmask", ploatmask)
cv2.imshow("cropedImg", cropedImg)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
