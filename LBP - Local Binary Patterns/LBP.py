import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
from os.path import isfile, join

def get_pixel(img, center, x, y):
    new_value = 0
    try:
        if img[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value

def lbp_calculated_pixel(img, x, y):
    '''
     64 | 128 |   1
    ----------------
     32 |   0 |   2
    ----------------
     16 |   8 |   4    
    '''    
    center = img[x][y]
    val_ar = []
    val_ar.append(get_pixel(img, center, x-1, y+1))     # top_right
    val_ar.append(get_pixel(img, center, x, y+1))       # right
    val_ar.append(get_pixel(img, center, x+1, y+1))     # bottom_right
    val_ar.append(get_pixel(img, center, x+1, y))       # bottom
    val_ar.append(get_pixel(img, center, x+1, y-1))     # bottom_left
    val_ar.append(get_pixel(img, center, x, y-1))       # left
    val_ar.append(get_pixel(img, center, x-1, y-1))     # top_left
    val_ar.append(get_pixel(img, center, x-1, y))       # top
    
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val    

def read_folder(path):
    filenames = glob.glob(path)
    filenames.sort()
    images = [cv2.imread(file) for file in filenames]
    return images

def Melanoma(img_lbp,i):
    cv2.imwrite("/home/alex/Área de Trabalho/teste_lbp/ISIC/Melanoma/ImgLBP_{:>03}.png".format(i),img_lbp)
    print("ISIC - LBP MELANOMA",i+1)

def NaoMelanoma(img_lbp,i):
    cv2.imwrite("/home/alex/Área de Trabalho/teste_lbp/ISIC/NãoMelanoma/ImgLBP_{:>03}.png".format(i),img_lbp)
    print("ISIC - LBP NAO MELANOMA",i+1)

def main():
    img_bgr = read_folder("/home/alex/Documentos/TCC2/ISIC/NaoMelanomaSegmentada/*.png")
    for cont in range(len(img_bgr)):
        height, width, channel = img_bgr[cont].shape
        img_gray = cv2.cvtColor(img_bgr[cont], cv2.COLOR_BGR2GRAY)
        
        img_lbp = np.zeros((height, width,3), np.uint8)
        for i in range(0, height):
            for j in range(0, width):
                 img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)

        #Melanoma(img_lbp,cont)
        NaoMelanoma(img_lbp,cont)
                                 
main()