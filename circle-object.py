from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
rng.seed(12345)

def thresh_callback(val):
    threshold = val
    
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    biggest_contour = [None]*len(contours)

    for i, c in enumerate(contours):
        biggest_contour[i] = cv.approxPolyDP(c, 3, True)

        #### Find the biggest contour on image
        biggest_contour[i] = max(contours, key = cv.contourArea)

        boundRect[i] = cv.boundingRect(biggest_contour[i])
        centers[i], radius[i] = cv.minEnclosingCircle(biggest_contour[i])
    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    for i in range(len(contours)):
        color_circle = (0,0,255)
        color_obj = (230,230,230)
        cv.drawContours(drawing, biggest_contour, i, color_obj)
        cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color_circle, 2)

    cen = centers[0]
    print("Centro: ",centers[0][0],centers[0][1])
    print("Raio: ",radius[0])
    print("Diametro: ",pow(radius[0],2))
    print("Area do Circulo: ",(3.14*(radius[0]**2)))
    cv.imshow('Contours', drawing)
    
src = cv.imread('../PH2/Segmentadas/MelanomaSegmentada/IMD211_lesion.bmp')
    
# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)
max_thresh = 500
thresh = 80 # initial threshold
thresh_callback(thresh)
cv.waitKey()