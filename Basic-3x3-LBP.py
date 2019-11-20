import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob
from os.path import isfile, join

def main():
    img = read_folder("/home/alex/Documentos/TCC2/PH2Dataset/MelanomaSegmentada/*.bmp")
    for i in range(len(img)):
        img2 = img[i]
        lbp(img[i],img2,i)

def read_folder(path):
    images = [cv2.imread(file,0) for file in glob.glob(path)]

    return images

def thresholded(center, pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out

def get_pixel_else_0(l, idx, idy, default=0):
    try:
        return l[idx,idy]
    except IndexError:
        return default

def lbp(img, transformed_img, i):
    for x in range(0, len(img)):
        for y in range(0, len(img[0])):
            center        = img[x,y]
            top_left      = get_pixel_else_0(img, x-1, y-1)
            top_up        = get_pixel_else_0(img, x,   y-1)
            top_right     = get_pixel_else_0(img, x+1, y-1)
            right         = get_pixel_else_0(img, x+1, y)
            left          = get_pixel_else_0(img, x-1, y)
            bottom_left   = get_pixel_else_0(img, x-1, y+1)
            bottom_right  = get_pixel_else_0(img, x+1, y+1)
            bottom_down   = get_pixel_else_0(img, x,   y+1)

            values = thresholded(center, [top_left, top_up, top_right, right, bottom_right, bottom_down, bottom_left, left])

            weights = [1, 2, 4, 8, 16, 32, 64, 128]
            res = 0
            for a in range(0, len(values)):
                res += weights[a] * values[a]

            transformed_img.itemset((x,y), res)

        #print(x)

    Melanoma(transformed_img,i)
    #NaoMelanoma(transformed_img,i)

def Melanoma(img_lbp,i):
    cv2.imwrite("/home/alex/Área de Trabalho/teste_lbp/ImgLBP_{:>04}.png".format(i),img_lbp)
    print("PH2 - LBP MELANOMA",i+1)

def NaoMelanoma(img_lbp,i):
    cv2.imwrite("/home/alex/Área de Trabalho/PH2/LBP/NãoMelanoma/ImgLBP_{:>04}.png".format(i),img_lbp)
    print("PH2 - LBP NAO MELANOMA",i+1)

main()