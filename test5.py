# -*- coding: utf-8 -*-

import cv2
import numpy

if __name__ == '__main__':
    # part 5
    # draw
    # 我的屏幕显示125%，所以实际大小 * 1.25
    img = numpy.zeros((400, 400, 3), numpy.uint8)
    print(img.shape)
    # 改色
    # b,g,r
    img[100:200, 200:300] = 255, 0, 0
    # 画线 img,start point,end point,color,line_thickness
    cv2.line(img, (0, 0), (200, 150), (0, 255, 0), 10)
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 1)
    # 矩形
    cv2.rectangle(img, (0, 0), (100, 50), (255, 255, 255), 3)
    # 填充矩形 cv2.FILLED或-1
    cv2.rectangle(img, (0, 50), (50, 100), (255, 255, 255), cv2.FILLED)
    # 圆形
    cv2.circle(img, (25, 75), 20, (0, 0, 255), 2)
    # 文字 img,text,start point,font,size,color,thickness
    cv2.putText(img, "OPENCV", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.startWindowThread()
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
