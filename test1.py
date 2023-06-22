# -*- coding: utf-8 -*-

import time
import cv2


if __name__ == '__main__':
    print(f'cv2 ver: {cv2.__version__}')
    # part 1
    # picture
    img = cv2.imread("Resources/1.jpg")
    # destroyAllWindows 防卡死，关闭imshow
    # 配合 startWindowThread 一起使用
    cv2.startWindowThread()
    cv2.imshow("Output", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    time.sleep(2)
