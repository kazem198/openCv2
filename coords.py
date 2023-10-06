import cv2
import pickle


# img = cv2.imread("images/carPark.png")
# width, height = 107, 48
# try:
#     with open("carParkPos", "rb") as f:
#         x = pickle.load(f)
#         print(x)

# except:
#     posList = []


# def on_mouse(event, x, y, unused, img):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, y)
#         posList.append((x, y))
#         with open("carParkPos", "wb") as f:
#             pickle.dump(posList, f)

#         # print(img)
#         cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
#     cv2.imshow("coords", img)


# cv2.imshow("coords", img)
# cv2.setMouseCallback("coords", on_mouse, param=img)
# # cv2.imshow("coords", img)
# if cv2.waitKey(0) & 0xFF == ord("q"):
#     cv2.destroyAllWindows()


with open("carParkPos", "rb") as f:
    x = pickle.load(f)
    print(x)
