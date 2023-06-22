# -*- coding: utf-8 -*-

import cv2
import numpy

if __name__ == '__main__':
    # part 6
    # 透视变换
    img = cv2.imread("Resources/4.jpg")
    card_width, card_height = 55, 90
    # 选区四点坐标
    points = numpy.float32([[184, 121], [238, 92], [224, 198], [279, 170]])
    # 目标四点坐标
    points2 = numpy.float32([[0, 0], [card_width, 0], [0, card_height], [card_width, card_height]])
    points3 = numpy.float32([[points[0][0], points[0][1]],
                             [points[0][0] + card_width, points[0][1]],
                             [points[0][0], points[0][1] + card_height],
                             [points[0][0] + card_width, points[0][1] + card_height]])
    # 选区画线
    cv2.line(img, (int(points[0][0]), int(points[0][1])), (int(points[1][0]), int(points[1][1])), (0, 255, 0), 3)
    cv2.line(img, (int(points[1][0]), int(points[1][1])), (int(points[3][0]), int(points[3][1])), (255, 0, 0), 3)
    cv2.line(img, (int(points[0][0]), int(points[0][1])), (int(points[2][0]), int(points[2][1])), (0, 0, 255), 3)
    cv2.line(img, (int(points[2][0]), int(points[2][1])), (int(points[3][0]), int(points[3][1])), (255, 255, 255), 3)
    # 目标画线
    cv2.line(img, (int(points2[0][0]), int(points2[0][1])), (int(points2[1][0]), int(points2[1][1])), (0, 255, 0), 3)
    cv2.line(img, (int(points2[1][0]), int(points2[1][1])), (int(points2[3][0]), int(points2[3][1])), (255, 0, 0), 3)
    cv2.line(img, (int(points2[0][0]), int(points2[0][1])), (int(points2[2][0]), int(points2[2][1])), (0, 0, 255), 3)
    cv2.line(img, (int(points2[2][0]), int(points2[2][1])), (int(points2[3][0]), int(points2[3][1])), (255, 255, 255),
             3)
    # 旋转变换
    matrix = cv2.getPerspectiveTransform(points, points2)
    img_matrix = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))
    matrix2 = cv2.getPerspectiveTransform(points, points3)
    img_matrix2 = cv2.warpPerspective(img, matrix2, (img.shape[1], img.shape[0]))
    cv2.startWindowThread()
    cv2.imshow("img", img)
    cv2.imshow("Matrix img", img_matrix)
    cv2.imshow("Matrix2 img", img_matrix2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
