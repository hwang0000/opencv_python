# -*- coding: utf-8 -*-

import cv2
import numpy


if __name__ == '__main__':
    # part 10
    # 人脸识别
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    img = cv2.imread("Resources/5.jpg")
    img = cv2.resize(img, (300, 450))
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.startWindowThread()
    isSuccess, img2 = cap.read()
    while isSuccess:
        capGray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(imgGray, 1.1, 4)
        # print(face)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        faceCap = faceCascade.detectMultiScale(capGray, 1.1, 4)
        for (x, y, w, h) in faceCap:
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("img", img)
        cv2.imshow("video", img2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        isSuccess, img2 = cap.read()
