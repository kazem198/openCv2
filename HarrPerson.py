import cv2
import numpy as np

cap = cv2.VideoCapture("./video/vtest.avi")
model = cv2.CascadeClassifier("./file/haarcascade_fullbody.xml")

while True:
    success, frame = cap.read()
    if success:

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        persons = model.detectMultiScale(
            gray_frame, 1.5, 2)
        for person in persons:
            x, y, w, h = person
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("frame", frame)
        if cv2.waitKey(50) & 0xFF == ord("q") or success == False:
            cv2.destroyAllWindows()
            break
cap.release()
