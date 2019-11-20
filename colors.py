import cv2 as cv
import glob as g
import numpy as np

def load_images3():

	pathMelaPH2 = "/home/alex/Documentos/TCC2/PH2Dataset/MelanomaSegmentada/*.bmp"
	pathNaoMelaPh2  ="/home/alex/Documentos/TCC2/PH2Dataset/NaoMelanomaSegmentada/*.bmp"
	pathMelaISIC = "/home/alex/Documentos/TCC2/Base de Imagens/Base de imagens/MelanomaSegmentada/*.png"
	pathNaoMelaISIC = "/home/alex/Documentos/TCC2/Base de Imagens/Base de imagens/NaoMelanomaSegmentada/*.png"

	list_path = g.glob(pathNaoMelaISIC)
	cont = 0
	cont1 = 0
	print(len(list_path))
	for i,value in enumerate(list_path):
		img = cv.imread(value)

		(bl,gr,re) = cv.split(img)

		zeros = np.zeros(img.shape[:2], dtype = "unit8")

		red = cv.merge([zeros,zeros,re])
		green = cv.merge([zeros,gr,zeros])
		blue = cv.merge([bl, zeros, zeros])
		
		cv.imwrite('/home/alex/Área de Trabalho/BLUE/ISIC/NaoMelanoma/ISIC_BLUE%d.png' % cont,blue)
		cv.imwrite('/home/alex/Área de Trabalho/RED/ISIC/Melanoma/ISIC_RED%d.png' % cont,red)
		cv.imwrite('/home/alex/Área de Trabalho/GREEN/ISIC/Melanoma/ISIC_GREEN%d.png' % cont,green)
		cont += 1
		print(value)

if __name__ == '__main__':  
    load_images3()
s