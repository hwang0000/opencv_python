# -*- coding: utf-8 -*-

import cv2
import numpy
import imgTools


def empty(a):
    pass


if __name__ == '__main__':
    # part 8
    # HSV 色调 饱和度 亮度
    img = cv2.imread("Resources/3.jpg")
    img = cv2.resize(img, (300, 400))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.startWindowThread()
    # 创建HSV调节面板
    cv2.namedWindow("Trackbar")
    cv2.resizeWindow("Trackbar", 640, 330)
    cv2.createTrackbar("Hue min", "Trackbar", 0, 179, empty)
    cv2.createTrackbar("Hue max", "Trackbar", 179, 179, empty)
    cv2.createTrackbar("Sat min", "Trackbar", 0, 255, empty)
    cv2.createTrackbar("Sat max", "Trackbar", 255, 255, empty)
    cv2.createTrackbar("Val min", "Trackbar", 0, 255, empty)
    cv2.createTrackbar("Val max", "Trackbar", 255, 255, empty)

    while True:
        # 获取HSV
        h_min = cv2.getTrackbarPos("Hue min", "Trackbar")
        h_max = cv2.getTrackbarPos("Hue min", "Trackbar")
        s_min = cv2.getTrackbarPos("Sat min", "Trackbar")
        s_max = cv2.getTrackbarPos("Sat max", "Trackbar")
        v_min = cv2.getTrackbarPos("Val min", "Trackbar")
        v_max = cv2.getTrackbarPos("Val max", "Trackbar")
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = numpy.array([h_min, s_min, v_min])
        upper = numpy.array([h_max, s_max, v_max])
        # 蒙板
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)
        imgStack = imgTools.stackImages(1, ([img, imgHSV], [mask, imgResult]))

        cv2.imshow("mask img", imgStack)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
