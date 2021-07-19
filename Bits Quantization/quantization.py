import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
from math import sqrt
import glob
import os
from tqdm import tqdm


def main():

    BitsQuantizacao = 4  # used 4,5,6,7
    bitsOriginal = 8

    colors = ['BLUE', 'GRAY', 'GREEN', 'RED']

    for x in range(len(colors)):
        execute(colors[x], bitsOriginal, BitsQuantizacao)


def execute(cor, bitsOriginal, BitsQuantizacao):
    lerPath = "E://PH2_Dataset//HistogramEqualization//"+cor+"//Melanoma//*.png"
    lerPath_Nm = "E://PH2_Dataset//HistogramEqualization//"+cor+"//NaoMelanoma//*.png"

    gravaPath = "E://PH2_Dataset//Quantization_HistEq//" + \
        str(BitsQuantizacao)+"bits//"+cor+"//Melanoma//"
    gravaPath_Nm = "E://PH2_Dataset//Quantization_HistEq//" + \
        str(BitsQuantizacao)+"bits//"+cor+"//NaoMelanoma//"

    melanoma(cor, lerPath, gravaPath, bitsOriginal, BitsQuantizacao)
    NaoMelanoma(cor, lerPath_Nm, gravaPath_Nm, bitsOriginal, BitsQuantizacao)


def melanoma(cor, lerPath, gravaPath, bitsOriginal, BitsQuantizacao):
    img = read(lerPath)
    for i in tqdm(range(len(img)), desc=cor+' Melanoma', ncols=100):
        imgQuantized = quantizar(img[i], bitsOriginal, BitsQuantizacao)
        writeImg(imgQuantized, gravaPath, i, BitsQuantizacao)


def NaoMelanoma(cor, lerPath_Nm, gravaPath_Nm, bitsOriginal, BitsQuantizacao):
    img = read(lerPath_Nm)
    for i in tqdm(range(len(img)), desc=cor+' NaoMelanoma', ncols=100):
        imgQuantized = quantizar(img[i], bitsOriginal, BitsQuantizacao)
        writeImg(imgQuantized, gravaPath_Nm, i, BitsQuantizacao)


def read(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv.imread(file) for file in filenames]
    return images


def writeImg(img, path, i, BitsQuantizacao):
    cv.imwrite(path+"img_"+str(BitsQuantizacao)+"_{:>03}.png".format(i), img)


def quantizar(img, bitsOriginal, BitsQuantizacao):
    portencia = pow(2, (bitsOriginal-BitsQuantizacao))
    linha, coluna, profundidade = img.shape
    for prof in range(profundidade):
        for lin in range(linha):
            for col in range(coluna):
                img[lin, col, prof] = int((img[lin, col, prof])/portencia)
    return img


main()
