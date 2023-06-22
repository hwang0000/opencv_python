# -*- coding: utf-8 -*-

import cv2
import numpy


def stackImages(scale, imgArray):
    """
    图像拼接函数
    :param scale:
    :param imgArray:
    :return:
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],
                                                (imgArray[0][0].shape[1],
                                                 imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = numpy.zeros((height, width, 3), numpy.uint8)
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = numpy.hstack(imgArray[x])
        ver = numpy.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = numpy.hstack(imgArray)
        ver = hor
    return ver


def empty(a):
    pass


if __name__ == '__main__':
    # part 8
    # 色调 饱和度 亮度
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
        imgStack = stackImages(0.5, ([img, imgHSV], [mask, imgResult]))

        cv2.imshow("mask img", imgStack)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
