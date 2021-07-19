import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
from math import sqrt
import glob
import os
from tqdm import tqdm

# Features extraction using Shannon, Simpson, Margalef and McIntosh indexes.
# N = total number of individuals in the sample


def main():
    # RGB channels + gray scale
    colors = ['BLUE', 'GRAY', 'GREEN', 'RED']

    # for the images dataset already quantized
    bits = ['4bits', '5bits', '6bits', '7bits']

    for x in range(len(colors)):
        NoMelanoma(colors[x], bits[x])
        Melanoma(colors[x], bits[x])
        print('\n')


def NoMelanoma(color, bits):

    path_NoMelanoma_imgs = "E://PH2_Dataset//Quantization_HistEq//" + \
        bits+"//"+color+"//NaoMelanoma//*.png"
    path_features_NoMelanoma = "C://Users//alexw//Documents//UFPI//TCC//Caracteristicas//hist_eq_" + \
        bits+"_"+color+"_.libsvm"
    NaoMelanoma = read_images(path_NoMelanoma_imgs)

    for i in tqdm(range(len(NaoMelanoma)), desc=bits+'-'+color+'-NaoMelanoma'):
        scale_array = scale_levels(NaoMelanoma[i])
        N = population(scale_array)
        write_NoMelanoma_features(scale_array, N, path_features_NoMelanoma)


def Melanoma(color, bits):
    path_melanoma_imgs = "E://PH2_Dataset//Quantization_HistEq//" + \
        bits+"//"+color+"//Melanoma//*.png"
    path_features_melanoma = "C://Users//alexw//Documents//UFPI//TCC//Caracteristicas//hist_eq_" + \
        bits+"_"+color+"_.libsvm"
    Melanoma = read_images(path_melanoma_imgs)

    for i in tqdm(range(len(Melanoma)), desc=bits+'-'+color+'-Melanoma'):
        scale_array = scale_levels(Melanoma[i])
        N = population(scale_array)
        write_melanoma_features(scale_array, N, path_features_melanoma)


# write the features calculated from No Melanoma images
def write_NoMelanoma_features(vet, N, path):
    Sh = shannon(vet, N)
    Si = simpson(vet, N)
    Ma = margalef(vet, N)
    Mc = McIntosh(vet, N)
    with open(path, 'a') as arq:
        arq.write(str(0)+" 1:"+str(Ma)+" 2:"+str(Mc) +
                  " 3:"+str(Sh)+" 4:"+str(Si)+'\n')


# write the features calculated from Melanoma images
def write_melanoma_features(vet, N, path):
    Sh = shannon(vet, N)
    Si = simpson(vet, N)
    Ma = margalef(vet, N)
    Mc = McIntosh(vet, N)
    with open(path, 'a') as arq:
        arq.write(str(1)+" 1:"+str(Ma)+" 2:"+str(Mc) +
                  " 3:"+str(Sh)+" 4:"+str(Si)+'\n')


# Read images from the dataset
def read_images(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv.imread(file, 0) for file in filenames]
    return images


# Scroll through the image counting the number of individuals for each level of the scale
def scale_levels(img):
    scale = []
    for x in range(256):
        scale.append(0)

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            pixel = img.item(i, j)
            scale[pixel] += 1
    return scale


# sum the total number of individuals in the population
def population(scale_array):
    N = 0

    for x in range(1, 256):
        N = N + scale_array[x]

    return N


# calculate and return the Margalef index
def margalef(scale_array, N):
    S = 0

    for y in range(1, 256):
        if scale_array[y] != 0:
            S += 1

    return ((S-1)/ln(N))


def Ucalc(scale_array):
    def p(n):
        if n == 0:
            return 0
        else:
            return n**2

    return sqrt(sum(p(scale_array[i]) for i in range(1, 256) if scale_array[i] != 0))


# calculate and return the McIntosh index
def McIntosh(scale_array, N):

    U = Ucalc(scale_array)

    return ((N-U)/(N-sqrt(N)))


# calculate and return the Shannon index
def shannon(scale_array, N):
    def p(n, N):
        if n == 0:
            return 0
        else:
            return (float(n)/N)*ln(float(n/N), 10)

    return -sum(p(scale_array[i], N) for i in range(1, 256) if scale_array[i] != 0)


# calculate and return the Simpson index
def simpson(scale_array, N):
    def p(n, N):
        if n == 0:
            return 0
        else:
            return (float(n/N) ** 2)

    return 1-(sum(p(scale_array[n], N) for n in range(1, 256) if scale_array[n] != 0))


main()
