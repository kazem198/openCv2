import cv2
import numpy as np

img = cv2.imread("./images/face.jpg")
img_eynak = cv2.imread("./images/eynak.png", 0)
img_eynak = cv2.resize(img_eynak, (img.shape[1], img.shape[0]))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
model_face = cv2.CascadeClassifier(
    "./file/haarcascade_frontalface_default.xml",)
model_smil = cv2.CascadeClassifier("./file/haarcascade_smile.xml")
faces = model_face.detectMultiScale(img_gray, 1.02, 2, minSize=(80, 80))


_, thersh = cv2.threshold(img_eynak, 1, 255, cv2.THRESH_BINARY_INV)
erode = cv2.erode(thersh, (5, 5), iterations=2)
dilete = cv2.dilate(thersh, (5, 5), iterations=2)
# print(faces)
for face in faces:
    # print(face)
    x, y, w, h = face
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.circle(img, (int(x+w/2), int(y+h/2)), 3, (0, 255, 0), 1)

    print(dilete.shape)
    print(img.shape)
    bitAnd = cv2.bitwise_and(img, img, mask=dilete)
    # face_RIO = img[y:y+h, x:x+w]

    # face_rio_gray = cv2.cvtColor(face_RIO, cv2.COLOR_BGR2GRAY)
#     print(face_RIO.shape)


cv2.imshow("img", img)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("dilate", dilete)

if (cv2.waitKey(0) & 0xFF == ord("q")):
    cv2.destroyAllWindows()
