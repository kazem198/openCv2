import cv2
import numpy as np
# img = cv2.imread("../../eys.jpg")
# img = cv2.GaussianBlur(img, (3, 3), 1)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, mask = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY)

# eage = cv2.Canny(mask, 210, 370)
# cv2.imshow("mask", mask)
# cv2.imshow("eys", img)
# cv2.imshow("eage", eage)

# img = cv2.imread("../../line.jpg")
# img = cv2.GaussianBlur(img, (3, 3), 1)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gray = cv2.equalizeHist(img_gray)
# _, mask = cv2.threshold(img_gray, 250, 255, cv2.THRESH_BINARY)
# eage = cv2.Canny(mask, 300, 400)
# # mask = cv2.adaptiveThreshold(
# #     eage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
# lines = cv2.HoughLinesP(mask, 1, np.pi/180, 150)
# print(lines.shape)
# for line in lines:
#     print(line[0])
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow("img", img)
# cv2.imshow("gray", img_gray)
# cv2.imshow("mask", mask)
# cv2.imshow("eage", eage)
# if cv2.waitKey(0) & 0xFF == ord("q"):
#     cv2.destroyAllWindows()


# img = cv2.imread("../../road.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# soblx = cv2.Sobel(img_gray, cv2.CV_8U, 1, 0)
# soblx64 = np.uint8(np.absolute(cv2.Sobel(img_gray, cv2.CV_64F, 1, 0)))
# sobly64 = np.uint8(np.absolute(cv2.Sobel(img_gray, cv2.CV_64F, 0, 1)))
# sobly = cv2.Sobel(img_gray, cv2.CV_8U, 0, 1)
# print(soblx)

# cv2.imshow("img", img)
# cv2.imshow("soblx", soblx)
# cv2.imshow("sobly", sobly)
# cv2.imshow("soblx64", soblx64)
# cv2.imshow("sobly64", sobly64)


# lab = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=1)
# canny = cv2.Canny(img_gray, 220, 255)
# cv2.imshow("lab", lab)
# cv2.imshow("canny", canny)
img = cv2.imread("./images/noise.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ther = cv2.threshold(img_gray, 200, 250, cv2.THRESH_BINARY)

# corners = cv2.goodFeaturesToTrack(img_gray, 250, .5, 1)
# corners = np.int32(corners)
# # print(corners.shape)
# for i, [corner] in enumerate(corners):
#     x = corner[0]
#     y = corner[1]
#     cv2.circle(img, (x, y), 2, (0, 0, 255), 2)

blur = cv2.bilateralFilter(ther, 5, .8, .8)

cv2.imshow("img", img_gray)
cv2.imshow("blur", blur)
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
