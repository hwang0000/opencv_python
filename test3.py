# -*- coding: utf-8 -*-

import cv2
import numpy

if __name__ == '__main__':
    # part 3
    # picture
    img = cv2.imread("Resources/3.jpg")
    img = cv2.resize(img, dsize=(600, 500))
    kernel = numpy.ones((5, 5), numpy.uint8)
    # 灰度 gray
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 高斯模糊
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0)
    # 边缘检测
    imgCanny = cv2.Canny(img, 100, 100)
    # 膨胀
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    # 腐蚀
    imgErode = cv2.erode(imgDilation, kernel, iterations=1)
    cv2.startWindowThread()
    cv2.imshow("Gray img", imgGray)
    cv2.imshow("Blur img", imgBlur)
    cv2.imshow("Canny img", imgCanny)
    cv2.imshow("Dilation img", imgDilation)
    cv2.imshow("Erode img", imgErode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
