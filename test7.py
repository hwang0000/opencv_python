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


if __name__ == '__main__':
    # part 7
    # 拼接
    img = cv2.imread("Resources/4.jpg")
    img2 = cv2.imread("Resources/3.jpg")
    # 水平拼接
    imgHor = numpy.hstack((img, img))
    # 垂直拼接
    imgVer = numpy.vstack((img, img))
    # 拼接函数
    imgStack = stackImages(0.5, ([img, img2, img], [img2, img, img]))
    cv2.startWindowThread()
    # cv2.imshow("img", img)
    # cv2.imshow("Horizontal img", imgHor)
    # cv2.imshow("Vertical img", imgVer)
    cv2.imshow("stackImages img", imgStack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
