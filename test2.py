import cv2

cap = cv2.VideoCapture("./video/vtest.avi")
# substract = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=100)
# substract = cv2.createBackgroundSubtractorKNN(history=100, detectShadows=False)
success, first_frame = cap.read()
first_frameg = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

while True:
    success, frame = cap.read()
    if success:
        grayf = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = cv2.absdiff(first_frameg, grayf)
        total = sum(sum(mask))
        print(total)
        # mask = substract.apply(frame)

        cv2.imshow("cap", frame)
        cv2.imshow("mask", mask)

    if cv2.waitKey(100) & 0xFF == ord("q") or success == False:
        break
    #    cv2.destroyAllWindows()

cap.release()
