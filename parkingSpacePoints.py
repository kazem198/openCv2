import cv2
import pickle

width, height = 107, 48

try:
    with open("./file/carParkPos", "rb") as f:
        posList = pickle.load(f)
        print(len(posList))
except:
    posList = []


def carPosition(events, x, y, flag, prop):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            if pos[0] < x < pos[0]+width and pos[1] < y < pos[1]+height:
                posList.pop(i)

    with open("./file/carParkPos", "wb") as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread("./images/carPark.png")

    for pos in posList:
        cv2.rectangle(
            img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)

    cv2.imshow("img", img)

    cv2.setMouseCallback("img", carPosition)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
