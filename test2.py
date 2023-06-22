# -*- coding: utf-8 -*-

import cv2

if __name__ == '__main__':
    # part 2
    # video
    cap = cv2.VideoCapture("Resources/2.mp4")
    # 0 -- 摄像头
    # cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # set width and height
    # 仅摄像头生效?
    # 3 -- width
    # 4 -- height
    # cap.set(3, 640)
    # cap.set(4, 480)
    # for i in range(0, 20):
    #     print(f'cap get {i} : {cap.get(i)}')
    cv2.startWindowThread()
    isSuccess, img = cap.read()
    while isSuccess:
        cv2.imshow("Video", img)
        # press q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        isSuccess, img = cap.read()
