import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
import glob
import os


def main():
    read_folder("/home/alex/Documentos/TCC2/ISIC/Melanoma/*.jpg")
    #img = cv.imread("/home/alex/Área de Trabalho/ISIC/GRAY/Melanoma/ISIC_GRAY72.png",0)
    # percorre(img)
    # print(4**2)


def read_folder(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [print(file) for file in filenames]
    # return images


def percorre(img):
    vetor = []
    te = 0
    N = 0

    for x in range(256):
        vetor.append(0)

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            pixel = img.item(i, j)
            vetor[pixel] += 1

    for y in range(1, 256):
        if vetor[y] != 0:
            te += 1

    for z in range(1, 256):
        N = N + vetor[z]

    for a in range(0, 256):
        print("Nível {0} ===> {1}p" .format(a, vetor[a]))
    # return vetor

    print("\nNumber of species present in the sample: ", te)
    print("Total number of individuals in the sample: ", N)


main()
