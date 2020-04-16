from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
import glob
rng.seed(12345)


def main():
    imagesMelanoma = read("../PH2/Segmentadas/MelanomaSegmentada/*.bmp")
    imagesNaoMelanoma = read("../PH2/Segmentadas/NaoMelanomaSegmentada/*.bmp")
    max_thresh = 500
    thresh = 80  # initial threshold

    for i in range(len(imagesMelanoma)):
        thresh_callback(thresh, imagesMelanoma[i])
        print('Imagem {} gravada' .format(i))

    print('Imagens gravadas com sucesso!')


def read(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv.imread(file) for file in filenames]
    grayImages = [cv.cvtColor(file, cv.COLOR_BGR2GRAY) for file in images]
    grayImages = [cv.blur(file, (3, 3)) for file in grayImages]

    return grayImages


def thresh_callback(val, image):
    threshold = val

    canny_output = cv.Canny(image, threshold, threshold * 2)

    contours, _ = cv.findContours(
        canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    biggest_contour = [None]*len(contours)

    for i, c in enumerate(contours):
        biggest_contour[i] = cv.approxPolyDP(c, 3, True)

        # Find the biggest contour on image
        biggest_contour[i] = max(contours, key=cv.contourArea)

        boundRect[i] = cv.boundingRect(biggest_contour[i])
        centers[i], radius[i] = cv.minEnclosingCircle(biggest_contour[i])

    drawing = np.zeros(
        (canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

    # for i in range(len(biggest_contour)):
    #     print(biggest_contour[i])s

    for i in range(len(biggest_contour)):
        color_circle = (0, 0, 255)
        color_obj = (230, 230, 230)
        cv.drawContours(drawing, biggest_contour, i, color_obj)
        # cv.circle(drawing, (int(centers[i][0]), int(
        #     centers[i][1])), int(radius[i]), color_circle, 2)

    # points = (int(centers[0][0]), int(centers[0][1]))
    # drawing = cv.arrowedLine(drawing, points, points, (255, 0, 0), 3)
    cen = centers[0]
    # print(biggest_contour[0])
    # print("Centro: ", int(centers[0][0]), int(centers[0][1]))
    # print("Raio: ", round(radius[0], 2))
    # print("Diametro: ", round(pow(radius[0], 2), 2))
    # print("Area do Circulo: ", round((3.14*(radius[0]**2)), 2))
    #cv.imshow('Contour', drawing)
    cv.imwrite(
        '../PH2/Border/Melanoma/pic{:>04}.png'.format(i), drawing)


if __name__ == "__main__":
    main()
