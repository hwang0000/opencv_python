# -*- coding: utf-8 -*-
import time
import cv2
import numpy


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],
                                                (imgArray[0][0].shape[1],
                                                 imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = numpy.zeros((height, width, 3), numpy.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank]*rows
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
    print(f'cv2 ver: {cv2.__version__}')

    # part 1
    # # picture
    # img = cv2.imread("Resources/1.jpg")
    # # destroyAllWindows 防卡死，关闭imshow
    # # 配合 startWindowThread 一起使用
    # cv2.startWindowThread()
    # cv2.imshow("Output", img)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()
    # time.sleep(2)

    # part 2
    # # video
    # cap = cv2.VideoCapture("Resources/2.mp4")
    # # 0 -- 摄像头
    # # cap = cv2.VideoCapture(0)
    # # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # # set width and height
    # # 仅摄像头生效?
    # # 3 -- width
    # # 4 -- height
    # # cap.set(3, 640)
    # # cap.set(4, 480)
    # # for i in range(0, 20):
    # #     print(f'cap get {i} : {cap.get(i)}')
    # cv2.startWindowThread()
    # isSuccess, img = cap.read()
    # while isSuccess:
    #     cv2.imshow("Video", img)
    #     # press q to stop
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break
    #     isSuccess, img = cap.read()

    # part 3
    # # picture
    # img = cv2.imread("Resources/3.jpg")
    # img = cv2.resize(img, dsize=(600, 500))
    # kernel = numpy.ones((5, 5), numpy.uint8)
    # # 灰度 gray
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # 高斯模糊
    # imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0)
    # # 边缘检测
    # imgCanny = cv2.Canny(img, 100, 100)
    # # 膨胀
    # imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    # # 腐蚀
    # imgErode = cv2.erode(imgDilation, kernel, iterations=1)
    # cv2.startWindowThread()
    # cv2.imshow("Gray img", imgGray)
    # cv2.imshow("Blur img", imgBlur)
    # cv2.imshow("Canny img", imgCanny)
    # cv2.imshow("Dilation img", imgDilation)
    # cv2.imshow("Erode img", imgErode)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # part 4
    # # picture
    # img = cv2.imread("Resources/3.jpg")
    # # shape, y,x,rgb
    # print(img.shape)
    # # dsize x,y
    # imgResize = cv2.resize(img, (480, 640))
    # print(imgResize.shape)
    # # 裁剪 y,x
    # imgCropped = imgResize[0:320, 120:300]
    # cv2.startWindowThread()
    # cv2.imshow("img", img)
    # cv2.imshow("Resize img", imgResize)
    # cv2.imshow("Crop img", imgCropped)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # part 5
    # # draw
    # # 我的屏幕显示125%，所以实际大小 * 1.25
    # img = numpy.zeros((400, 400, 3), numpy.uint8)
    # print(img.shape)
    # # 改色
    # # b,g,r
    # img[100:200, 200:300] = 255, 0, 0
    # # 画线 img,start point,end point,color,line_thickness
    # cv2.line(img, (0, 0), (200, 150), (0, 255, 0), 10)
    # cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 1)
    # # 矩形
    # cv2.rectangle(img, (0, 0), (100, 50), (255, 255, 255), 3)
    # # 填充矩形 cv2.FILLED或-1
    # cv2.rectangle(img, (0, 50), (50, 100), (255, 255, 255), cv2.FILLED)
    # # 圆形
    # cv2.circle(img, (25, 75), 20, (0, 0, 255), 2)
    # # 文字 img,text,start point,font,size,color,thickness
    # cv2.putText(img, "OPENCV", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    # cv2.startWindowThread()
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # part 6
    # # 透视变换
    # img = cv2.imread("Resources/4.jpg")
    # card_width, card_height = 55, 90
    # # 选区四点坐标
    # points = numpy.float32([[184, 121], [238, 92], [224, 198], [279, 170]])
    # # 目标四点坐标
    # points2 = numpy.float32([[0, 0], [card_width, 0], [0, card_height], [card_width, card_height]])
    # points3 = numpy.float32([[points[0][0], points[0][1]],
    #                          [points[0][0] + card_width, points[0][1]],
    #                          [points[0][0], points[0][1] + card_height],
    #                          [points[0][0] + card_width, points[0][1] + card_height]])
    # # 选区画线
    # cv2.line(img, (int(points[0][0]), int(points[0][1])), (int(points[1][0]), int(points[1][1])), (0, 255, 0), 3)
    # cv2.line(img, (int(points[1][0]), int(points[1][1])), (int(points[3][0]), int(points[3][1])), (255, 0, 0), 3)
    # cv2.line(img, (int(points[0][0]), int(points[0][1])), (int(points[2][0]), int(points[2][1])), (0, 0, 255), 3)
    # cv2.line(img, (int(points[2][0]), int(points[2][1])), (int(points[3][0]), int(points[3][1])), (255, 255, 255), 3)
    # # 目标画线
    # cv2.line(img, (int(points2[0][0]), int(points2[0][1])), (int(points2[1][0]), int(points2[1][1])), (0, 255, 0), 3)
    # cv2.line(img, (int(points2[1][0]), int(points2[1][1])), (int(points2[3][0]), int(points2[3][1])), (255, 0, 0), 3)
    # cv2.line(img, (int(points2[0][0]), int(points2[0][1])), (int(points2[2][0]), int(points2[2][1])), (0, 0, 255), 3)
    # cv2.line(img, (int(points2[2][0]), int(points2[2][1])), (int(points2[3][0]), int(points2[3][1])), (255, 255, 255),
    #          3)
    # # 旋转变换
    # matrix = cv2.getPerspectiveTransform(points, points2)
    # img_matrix = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))
    # matrix2 = cv2.getPerspectiveTransform(points, points3)
    # img_matrix2 = cv2.warpPerspective(img, matrix2, (img.shape[1], img.shape[0]))
    # cv2.startWindowThread()
    # cv2.imshow("img", img)
    # cv2.imshow("Matrix img", img_matrix)
    # cv2.imshow("Matrix2 img", img_matrix2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # part 7
    # 拼接
    img = cv2.imread("Resources/4.jpg")
    # 水平拼接
    imgHor = numpy.hstack((img, img))
    # 垂直拼接
    imgVer = numpy.vstack((img, img))
    cv2.startWindowThread()
    cv2.imshow("img", img)
    cv2.imshow("Horizontal img", imgHor)
    cv2.imshow("Vertical img", imgVer)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





