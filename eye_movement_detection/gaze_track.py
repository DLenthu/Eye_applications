import cv2

import numpy as np

cap = cv2.VideoCapture("2eyes_1.mp4")
ret,frame = cap.read()
roi = frame
gray_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
gray_roi = cv2.GaussianBlur(gray_roi,(13,13),0)
_,threshold = cv2.threshold(gray_roi,40,255,cv2.THRESH_BINARY_INV)
contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours,key = lambda x: cv2.contourArea(x),reverse = True)[:2]
x_1, y_1, w, h = cv2.boundingRect(contours[0])
x_2, y_2, w, h = cv2.boundingRect(contours[1])

while True:
    ret,frame = cap.read()
    roi = frame

    gray_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    gray_roi = cv2.GaussianBlur(gray_roi,(13,13),0)

    _,threshold = cv2.threshold(gray_roi,40,255,cv2.THRESH_BINARY_INV)

    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours,key = lambda x: cv2.contourArea(x),reverse = True)[:2]

    x1, y1, w1, h1 = cv2.boundingRect(contours[0])
    cv2.circle(roi,(x1 + int(w1/2),y1 + int(h1/2)),15,(255,0,0),2)
    cv2.line(roi,(x1 + int(w1/2),0),(x1 + int(w1/2),525),(0,255,0),2)
    cv2.line(roi,(0,y1 + int(h1/2)),(878,y1 + int(h1/2)),(0,255,0),2)

    x2, y2, w2, h2 = cv2.boundingRect(contours[1])
    cv2.circle(roi,(x2 + int(w2/2),y2 + int(h2/2)),15,(255,0,0),2)
    cv2.line(roi,(x2 + int(w2/2),0),(x2 + int(w2/2),525),(0,255,0),2)
    cv2.line(roi,(0,y2 + int(h2/2)),(878,y2 + int(h2/2)),(0,255,0),2)

    if (x1>x_1 and x2>x_2):
        print("looking right\n")
    if (x1<x_1 and x2<x_2):
        print("looking left\n")
    if (y1>y_1 and y2>y_2):
        print("looking down\n")
    if (y1<y_1 and y2<y_2):
        print("looking up\n")

    cv2.imshow("Threshold",threshold)

    cv2.imshow("Frame",roi)

    key = cv2.waitKey(30)
    if key == 27 & ret:
        break

cv2.destroyAllWindows()

