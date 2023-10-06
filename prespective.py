import cv2
import numpy as np


img = cv2.imread("./images/prespective.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gray = cv2.bilateralFilter(img_gray, 9, 75, 75)
_, thersh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
thersh = cv2.erode(thersh, (3, 3), iterations=5)
# thersh = cv2.adaptiveThreshold(
#     img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 10)

edge = cv2.Canny(thersh, 200, 230)
# edge = cv2.GaussianBlur(edge, (5, 5), 0)
# edge = np.uint8(np.absolute(cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)))
# dilate = cv2.dilate(edge, (5, 5), iterations=7)
# cv2.imshow("dilate", dilate)

contours, _ = cv2.findContours(
    edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
points = []
# print(contours)
for con in contours:
    # area = cv2.contourArea(con, True)
    # arc = cv2.arcLength(con, True)
    # poly = cv2.approxPolyDP(con, .02*arc, True)
    # print(poly.shape)
    # areas.append(arc)
    # cv2.drawContours(img, [con], -1, (0, 0, 255), 2)
    x = cv2.minAreaRect(con)
    x = cv2.boxPoints(x)
    x = np.reshape(x, (4, 1, 2))
    x = np.int32(x)
    cv2.drawContours(img, [x], -1, (0, 0, 255), 2)
    points.append(x)
    print(x)

src = np.reshape(points[0], (4, 2))
print(src)

# masArea = np.argmax(areas)
# cv2.drawContours(img, contours[masArea], -1, (0, 0, 255), 5)
# print(contours[masArea].shape)
# print(contours[masArea])
# img_dis = np.ones((800, 800, 3), np.int32)
# src = np.reshape(poly, (4, 2))
# print(src)
# src = np.float32([[100, 60], [590, 70], [20, 600], [600, 600]])
dis = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

M = cv2.getPerspectiveTransform(np.float32(src), dis)
wrap = cv2.warpPerspective(img, M, (800, 800))
# wrap_gray = cv2.cvtColor(wrap, cv2.COLOR_BGR2GRAY)
# thersh = cv2.adaptiveThreshold(
#     wrap_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 10)
cv2.imshow("edge", edge)
cv2.imshow("wrap", wrap)
cv2.imshow("thersh", thersh)
cv2.imshow("img", img)
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
