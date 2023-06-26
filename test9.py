# -*- coding: utf-8 -*-

import cv2
import numpy
import imgTools


def getContours(img1, img2):
    """
    获取轮廓
    :param img1:
    :param img2:
    :return:
    """
    contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    i = 0
    for cnt in contours:
        i = i + 1
        # 面积
        area = cv2.contourArea(cnt)
        print(area)
        if area >= 5000:
            # 画轮廓
            cv2.drawContours(img2, cnt, -1, (0, 255, 0), 3)
            # 弧长
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            # 拐点
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCor = len(approx)
            print(objCor)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img2, str(i), (int(x + w / 2), int(y + h / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


if __name__ == '__main__':
    # part 9
    img = cv2.imread("Resources/shape.png")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgBlank = numpy.zeros_like(img)

    imgCanny = cv2.Canny(imgBlur, 50, 50)
    imgContour = img.copy()
    getContours(imgCanny, imgContour)

    imgStack = imgTools.stackImages(0.7, ([img, imgGray, imgBlur],
                                          [imgCanny, imgBlank, imgContour]))
    cv2.startWindowThread()
    cv2.imshow("img", imgStack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





