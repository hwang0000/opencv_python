# -*- coding: utf-8 -*-

import cv2

if __name__ == '__main__':
    # part 4
    # picture
    img = cv2.imread("Resources/3.jpg")
    # shape, y,x,rgb
    print(img.shape)
    # dsize x,y
    imgResize = cv2.resize(img, (480, 640))
    print(imgResize.shape)
    # 裁剪 y,x
    imgCropped = imgResize[0:320, 120:300]
    cv2.startWindowThread()
    cv2.imshow("img", img)
    cv2.imshow("Resize img", imgResize)
    cv2.imshow("Crop img", imgCropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
