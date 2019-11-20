import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
from math import sqrt
import glob
import os

#testar com 7, 6, 5 e 4

def main():
	cor = "GRAY"
	lerPath = "/home/alex/Área de Trabalho/PH2/"+cor+"/Melanoma/*.png"
	lerPath_Nm = "/home/alex/Área de Trabalho/PH2/"+cor+"/NaoMelanoma/*.png"
	
	gravaPath = "/home/alex/Área de Trabalho/PH2/4/"+cor+"/Melanoma/"
	gravaPath_Nm = "/home/alex/Área de Trabalho/PH2/4/"+cor+"/NaoMelanoma/"
	
	BitsQuantizacao = 4
	bitsOriginal = 8
	
	melanoma(cor,lerPath,gravaPath,bitsOriginal,BitsQuantizacao)
	NaoMelanoma(cor,lerPath_Nm,gravaPath_Nm,bitsOriginal,BitsQuantizacao)

def melanoma(cor,lerPath,gravaPath,bitsOriginal,BitsQuantizacao):
	img = read(lerPath)
	for i in range(len(img)):
		imgQuantized = quantizar(img[i],bitsOriginal,BitsQuantizacao)
		writeImg(imgQuantized,gravaPath,i)
		print("PH2 - QUANTIZED 4bits - MELANOMA - "+cor,i+1)

def NaoMelanoma(cor,lerPath_Nm,gravaPath_Nm,bitsOriginal,BitsQuantizacao):
	img = read(lerPath_Nm)
	for i in range(len(img)):
		imgQuantized = quantizar(img[i],bitsOriginal,BitsQuantizacao)
		writeImg(imgQuantized,gravaPath_Nm,i)
		print("PH2 - QUANTIZED 4bits - NAO MELANOMA - "+cor,i+1)

def read(path):
	filenames = glob.glob(path)
	filenames.sort()
	images = [cv.imread(file) for file in filenames]
	return images

def writeImg(img,path,i):
	cv.imwrite(path+"img_4_{:>03}.png".format(i),img)
	
def quantizar(img, bitsOriginal, BitsQuantizacao):
    portencia = pow(2,(bitsOriginal-BitsQuantizacao))
    linha, coluna, profundidade = img.shape
    for prof in range(profundidade):
        for lin in range(linha):
            for col in range(coluna):
                img[lin,col,prof] = int((img[lin,col,prof])/portencia)
    return img

main()