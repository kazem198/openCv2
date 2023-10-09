import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = "image_Atendense"
images = []
calssNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    img = cv2.imread(f'{path}/{cl}')
    images.append(img)
    calssNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markattendance(name):
    with open("attendance.csv", "r+") as f:
        myDataList = f.readline()
        nameList = []
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')


encodeListKhown = findEncodings(images)
# print(len(encodeListKhown))

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgs)
    encodeCurFrame = face_recognition.face_encodings(imgs, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKhown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKhown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = calssNames[matchIndex]
            print(name)
            cv2.rectangle(img, (faceLoc[3]*4, faceLoc[0]*4),
                          (faceLoc[1]*4, faceLoc[2]*4), (255, 0, 0), 2)
            markattendance(name)

    cv2.imshow("frame", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
# imgElion = face_recognition.load_image_file("./images/elion.jpg")
# imgElion = cv2.cvtColor(imgElion, cv2.COLOR_BGR2RGB)

# imgTest = face_recognition.load_image_file("./images/elon2.jpg")
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# face_loc = face_recognition.face_locations(imgElion)[0]
# encode_elon = face_recognition.face_encodings(imgElion)[0]
# cv2.rectangle(imgElion, (face_loc[3], face_loc[0]),
#               (face_loc[1], face_loc[2]), (0, 255, 0), 2)

# face_locTest = face_recognition.face_locations(imgTest)[0]
# encode_elon_Test = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (face_locTest[3], face_locTest[0]),
#               (face_locTest[1], face_locTest[2]), (0, 255, 0), 2)

# result = face_recognition.compare_faces([encode_elon], encode_elon_Test)
# face_dis = face_recognition.face_distance([encode_elon], encode_elon_Test)
# cv2.putText(imgTest, f'{result} {round(face_dis[0],2)})', (
#     10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
# print(result, face_dis)

# cv2.imshow("elion", imgElion)
# cv2.imshow("imgTest", imgTest)
# cv2.waitKey(0)
