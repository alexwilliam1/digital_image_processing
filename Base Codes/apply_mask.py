import cv2
import numpy as np
import glob
from os.path import isdir, isfile, join
import os
from os import listdir
 
def main():
    img = read_images("/home/alex/Área de Trabalho/teste_lbp/ISIC/NãoMelanoma/*.png")
    mask = read_masks("/home/alex/Documentos/TCC2/ISIC/MascaraNaoMelanoma/*.png")
   # show(img[24],mask[24])
    for i in range(len(img)):
        apply(img[i],mask[i],i)

def read_images(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv2.imread(file,0) for file in filenames]
    return images

def read_masks(path):
	filenames = glob.glob(path)
	filenames.sort()
	masks = [cv2.imread(file,0) for file in filenames]
	return masks

def apply(img, mask, i):
	res = cv2.bitwise_and(img,img,mask = mask)
	cv2.imwrite("/home/alex/Área de Trabalho/a/ImgLBP_{:>03}.png".format(i),res)
	print("ISIC - LBP MELANOMA",i+1)

def show(img,mask):
	cv2.imshow("imagem lbp",img)
	cv2.imshow("mascara",mask)
	cv2.waitKey(0)

main()