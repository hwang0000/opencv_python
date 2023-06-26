# -*- coding: utf-8 -*-

import cv2
import numpy
import imgTools


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
    imgStack = imgTools.stackImages(0.5, ([img, img2, img], [img2, img, img]))
    cv2.startWindowThread()
    # cv2.imshow("img", img)
    # cv2.imshow("Horizontal img", imgHor)
    # cv2.imshow("Vertical img", imgVer)
    cv2.imshow("stackImages img", imgStack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
