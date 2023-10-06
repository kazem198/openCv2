import cv2
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume
currentVolumeDb = volume.GetMasterVolumeLevel()
# volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
volume.SetMasterVolumeLevel(currentVolumeDb, None)
print(currentVolumeDb)
# NOTE: -6.0 dB = half volume !

vol = [-65.25, 0.0]

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam)

detector = HandDetector(staticMode=False, maxHands=1,
                        modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

pTime = 0
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(frame, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    hands, img = detector.findHands(frame, draw=True, flipType=False)

    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        # Bounding box around the first hand (x,y,w,h coordinates)
        bbox1 = hand1["bbox"]
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        # Print the count of fingers that are up
        # print(f'H1 = {fingers1.count(1)}', end=" ")

        # Calculate distance between specific landmarks on the first hand and draw it on the image
        length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255),
                                                  scale=10)
        x = np.interp(length, [15, 200], [450, 300])
        # print(x)
        cv2.rectangle(frame, (50, 450), (100, 300), (0, 255, 0), 1)
        cv2.rectangle(frame, (50, 450), (100, int(x)), (0, 255, 0), -1)

        y = np.interp(length, [15, 200], [-65.25, 0.0])
        volume.SetMasterVolumeLevel(y, None)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
