import cv2 as cv
import numpy as np
import glob
from os.path import isfile, join
from os import listdir
from matplotlib import pyplot as plt
import pylab as pl
import os


def main():
    melanoma_images = read_(
        "/home/alex/Documentos/TCC2/PH2Dataset/MelanomaSegmentada/*.bmp")
    for i in range(len(melanoma_images)):
        clahe(melanoma_images[i], i)

    naoMelanoma_images = read_(
        "/home/alex/Documentos/TCC2/PH2Dataset/NaoMelanomaSegmentada/*.bmp")
    for i in range(len(naoMelanoma_images)):
        clahe(naoMelanoma_images[i], i)


def read_(path):
    images = [cv.imread(file, 1) for file in glob.glob(path)]

    return images


def clahe(img, i):
    (bl, gr, re) = cv.split(img)
    zeros = np.zeros(img.shape[:2], dtype="uint8")

    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    blueEq = clahe.apply(bl)
    greenEq = clahe.apply(gr)
    redEq = clahe.apply(re)

    red = cv.merge([zeros, zeros, redEq])
    green = cv.merge([zeros, greenEq, zeros])
    blue = cv.merge([blueEq, zeros, zeros])

    write_clahe_melanoma_images(red, blue, green, i)
    write_clahe_naoMelanoma_images(red, blue, green, i)


def write_clahe_melanoma_images(red, blue, green, i):
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/RED/Melanoma/pic{:>04}.png".format(i), red)
    print("PH2 - CLAHE MELANOMA RED", i+1)
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/BLUE/Melanoma/pic{:>04}.png".format(i), blue)
    print("PH2 - CLAHE MELANOMA BLUE", i+1)
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/GREEN/Melanoma/pic{:>04}.png".format(i), green)
    print("PH2 - CLAHE MELANOMA GREEN", i+1)


def write_clahe_naoMelanoma_images(red, blue, green, i):
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/RED/NaoMelanoma/pic{:>04}.png".format(i), red)
    print("PH2 - CLAHE NAO MELANOMA RED", i+1)
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/BLUE/NaoMelanoma/pic{:>04}.png".format(i), blue)
    print("PH2 - CLAHE NAO MELANOMA BLUE", i+1)
    cv.imwrite(
        "/home/alex/Área de Trabalho/PH2/Clahe/GREEN/NaoMelanoma/pic{:>04}.png".format(i), green)
    print("PH2 - CLAHE NAO MELANOMA GREEN", i+1)


main()
