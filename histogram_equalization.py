import cv2 as cv
import numpy as np
import glob
from os.path import isfile, join
from os import listdir
from matplotlib import pyplot as plt
import pylab as pl
import os

def read():
	# img = read_("/home/alex/Documentos/TCC2/Base de Imagens/Base de imagens/MelanomaSegmentada/*.png")
	# for i in range(len(img)):
	# 	histrogram_equalize(img[i],i)

	img2 = read_("/home/alex/Documentos/TCC2/Base de Imagens/Base de imagens/NaoMelanomaSegmentada/*.png")
	for i in range(len(img2)):
		histrogram_equalize(img2[i],i)
		
		
def histrogram_equalize(img,i):
	(bl,gr,re) = cv.split(img)
	zeros = np.zeros(img.shape[:2], dtype = "uint8")

	redEq = cv.equalizeHist(re)
	greenEq = cv.equalizeHist(gr)
	blueEq = cv.equalizeHist(bl)

	red = cv.merge([zeros,zeros,redEq])
	green = cv.merge([zeros,greenEq,zeros])
	blue = cv.merge([blueEq,zeros,zeros])

	#Melanoma(red,blue,green,i)
	NaoMelanoma(red,blue,green,i)


def Melanoma(red,blue,green,i):
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/RED/Melanoma/pic{:>04}.png".format(i),red)
	print("ISIC - EQUALIZED MELANOMA RED",i+1)
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/BLUE/Melanoma/pic{:>04}.png".format(i),blue)
	print("ISIC - EQUALIZED MELANOMA BLUE",i+1)
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/GREEN/Melanoma/pic{:>04}.png".format(i),green)
	print("ISIC - EQUALIZED MELANOMA GREEN",i+1)

def NaoMelanoma(red,blue,green,i):
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/RED/NaoMelanoma/pic{:>04}.png".format(i),red)
	print("ISIC - EQUALIZED NAO MELANOMA RED",i+1)
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/BLUE/NaoMelanoma/pic{:>04}.png".format(i),blue)
	print("ISIC - EQUALIZED NAO MELANOMA BLUE",i+1)
	cv.imwrite("/home/alex/Área de Trabalho/ISIC/Histogram Equalization/GREEN/NaoMelanoma/pic{:>04}.png".format(i),green)
	print("ISIC - EQUALIZED NAO MELANOMA GREEN",i+1)
	

def read_(path):
	images = [cv.imread(file,1) for file in glob.glob(path)]

	return images

read()