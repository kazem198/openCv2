import cv2
import numpy as np

road = cv2.imread("./images/road.jpg")

car = cv2.imread("./images/car.jpg")
car = cv2.resize(car, (road.shape[1], road.shape[0]))
gray_car = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("final")


def noting(x):
    pass


cv2.createTrackbar("ka", "final", 10, 255, noting)

while True:
    x = cv2.getTrackbarPos("ka", "final")
    # _, mask_car = cv2.threshold(gray_car, x, 255, cv2.THRESH_BINARY)
    mask_car = cv2.adaptiveThreshold(
        gray_car, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, x)
    mask_carInv = cv2.bitwise_not(mask_car)
    road_car = cv2.bitwise_and(road, road, mask=mask_car)
    car_maskInv = cv2.bitwise_and(car, car, mask=mask_carInv)
    final = cv2.add(road_car, car_maskInv)

    cv2.imshow("gray_car", gray_car)
    cv2.imshow("car", car)
    cv2.imshow("road", road)
    cv2.imshow("mask_car", mask_car)
    cv2.imshow("mask_carInv", mask_carInv)
    cv2.imshow("road_car", road_car)
    cv2.imshow("car_maskInv", car_maskInv)
    cv2.imshow("final", final)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
