import numpy as np
import cv2 as cv
import sys
from math import sqrt
import glob


def main():
    imagesMelanoma = read("../PH2/Segmentadas/MelanomaSegmentada/*.bmp")
    imagesNaoMelanoma = read("../PH2/Segmentadas/NaoMelanomaSegmentada/*.bmp")

    for i in range(len(imagesMelanoma)):
        process(imagesMelanoma[i], i)
        print('Imagem {} gravada' .format(i))

    print('Imagens gravadas com sucesso!')


def read(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv.imread(file) for file in filenames]

    return images


def writeImages(image, i):
    cv.imwrite(
        '../PH2/Border/Melanoma/pic{:>04}.png'.format(i), image)


def process(src, i):

    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    # Load the image
    # src = cv.imread(
    #     '../PH2/Segmentadas/MelanomaSegmentada/IMD285_lesion.bmp', cv.IMREAD_COLOR)
    # src = cv.imread(
    #    '../PH2/Border/Melanoma/pic0021.png', cv.IMREAD_COLOR)

    src = cv.GaussianBlur(src, (3, 3), 0)

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale,
                      delta=delta, borderType=cv.BORDER_DEFAULT)
    # Gradient-Y
    # grad_y = cv.Scharr(gray,ddepth,0,1)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale,
                      delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    print(grad.shape)

    # vet = []
    # for i in range(256):
    #     vet.append(0)

    # for x in range(0, grad.shape[0]):
    #     for y in range(0, grad.shape[1]):
    #         pixel = grad.item(x, y)
    #         vet[pixel] += 1

    # a = 0
    # for x in range(0, len(vet)):
    #     if(vet[x] != 0):
    #         print("{0} -> {1}".format(a, vet[x]))
    #         a += 1

    # Diametro
    # É a maior distância entre dois pontos (p1 = (x1, y1) e p2 = (x2, y2)) pertencentes
    # ao contorno da região de interesse, que pode ser formalizada por:

    # D = sqrt(((x1-x2)**2)+((y1-y2)**2))
    # D = sqrt(pow((x1-x2),2)+pow((y1-y2),2))

    # cv.imshow(window_name, grad)
    # cv.waitKey(0)

    writeImages(grad, i)

    return 0


if __name__ == "__main__":
    main()
