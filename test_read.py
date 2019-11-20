import cv2 as cv
import numpy as np
import glob
from os.path import isfile, join
from os import listdir
from matplotlib import pyplot as plt
import pylab as pl
import os

def read():
	cor = "BLUE"
	NaoMelan = "/home/alex/Área de Trabalho/ISIC/"+cor+"/NaoMelanoma/*.png"
	Melan = "/home/alex/Área de Trabalho/ISIC/"+cor+"/Melanoma/*.png"

	Mgrava = "/home/alex/Área de Trabalho/ISIC/Histogram Equalization/"+cor+"/Melanoma/"
	NMgrava  = "/home/alex/Área de Trabalho/ISIC/Histogram Equalization/"+cor+"/NaoMelanoma/"

	img = read_(Melan)
	for i in range(len(img)):
		imgEq = histrogram_equalize(img[i])
		cv.imwrite(Mgrava+"pic{:>04}.png".format(i),imgEq)

	img2 = read_(NaoMelan)
	for a in range(len(img2)):
		imgEq = histrogram_equalize(img2[i])
		cv.imwrite(NMgrava+"pic{:>04}.png".format(i),imgEq)
		
def histrogram_equalize(img):
	(bl,gr,re) = cv.split(img)
	zeros = np.zeros(img.shape[:2], dtype = "uint8")

	redEq = cv.equalizeHist(re)
	greenEq = cv.equalizeHist(gr)
	blueEq = cv.equalizeHist(bl)

	#red = cv.merge([zeros,zeros,redEq])
	#green = cv.merge([zeros,greenEq,zeros])
	blue = cv.merge([blueEq,zeros,zeros])
	
	return blue

def NaoMela(img,path,i):
	cv.imwrite(path+"pic{:>04}.png".format(i),img)
	#img = read_(path)
	#for i in range(len(img)):

		#cv.imshow("original blue",img[i])
		#cv.waitKey(0)

		#lab = cv.cvtColor(img[i],cv.COLOR_BGR2LAB)
		#cv.imshow("lab",lab)
		#cv.waitKey(0)

		# (l,a,b) = cv.split(lab)

		# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		# cl = clahe.apply(l)
		# ca = clahe.apply(a)
		# cb = clahe.apply(b)

		# im = cv.merge((cl,ca,cb))

		# cv.imshow("merge",im)

		# final = cv.cvtColor(im, cv.COLOR_LAB2BGR)
		# cv.imshow("final",final)
		# cv.waitKey(0)

		#red = cv.merge([zeros,zeros,redEq])
		#green = cv.merge([zeros,greenEq,zeros])
		#cv.imshow("red Equa",red)
		#cv.imshow("green Equa",green)
		#cv.imshow("blue Equa",blue)
		#cv.waitKey(0)

		# cl1 = clahe.apply(blue)
		# cl2 = clahe.apply(green)
		# cl3 = clahe.apply(red)
		

def Mela(path):
	img2 = read_(path)
	for i in range(len(img2)):

		(bl,gr,re) = cv.split(img2[i])
		zeros = np.zeros(img2[i].shape[:2], dtype = "uint8")

		redEq = cv.equalizeHist(re)
		greenEq = cv.equalizeHist(gr)
		blueEq = cv.equalizeHist(bl)

		#red = cv.merge([zeros,zeros,redEq])
		#green = cv.merge([zeros,greenEq,zeros])
		blue = cv.merge([blueEq,zeros,zeros])

		#calcEq = cv.equalizeHist(img2[i])
		# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		# cl1 = clahe.apply(blue)
		# cl2 = clahe.apply(green)
		# cl3 = clahe.apply(red)
		cv.imwrite( "/home/alex/Área de Trabalho/ISIC/Histogram Equalization/BLUE/Melanoma/pic{:>04}.png".format(i),blue)
		#cv.imwrite("/home/alex/Área de Trabalho/PH2/Clahe/GREEN/Melanoma/pic{:>04}.png".format(i),cl2)
		#cv.imwrite("/home/alex/Área de Trabalho/PH2/Clahe/RED/Melanoma/pic{:>04}.png".format(i),cl3)
		print("MELANOMA",i+1)

def read_(path):
	images = [cv.imread(file,1) for file in glob.glob(path)]

	return images

		# folders = glob.glob('/home/alex/Documentos/TCC2/PH2Dataset/PH2 Dataset images/IMD*/IMD*_Dermoscopic_Image/')
		# imgnames_list = []
		# for folder in folders:
		# 	for f in glob.glob(folder+'*'):
		# 		imgnames_list.append(os.path.basename(f))

		# x = 0

		# with open('/home/alex/Documentos/TCC2/PH2Dataset/PH2_simp2.txt', 'r') as ph2:
		# 	for line in ph2:
		# 		valores = line.split()
		# 		for w in range(len(imgnames_list)):
		# 			if valores[0] == imgnames_list[w]:
		# 				x = 1
		# 				break
		# 		if x == 0:
		# 			print(valores[0]+" não está na pasta")
					# 	#print(valores[0]+' '+valores[1]+' '+imgnames_list[w])
					# 	if valores[1] != '2':
					# 		with open("/home/alex/Documentos/TCC2/PH2Dataset/teste_caracteristicas.txt",'a') as arq:
					# 			arq.write(str(1)+" 1:"+str(20)+" 2:"+str(20)+'\n')
					# 		break
					# 	else:
					# 		with open("/home/alex/Documentos/TCC2/PH2Dataset/teste_caracteristicas.txt",'a') as arq:  
					# 			arq.write(str(-1)+" 1:"+str(99)+" 2:"+str(99)+'\n')
					# 		break
					# print(w)
			# folders = glob.glob('/home/alex/Documentos/TCC2/PH2Dataset/PH2 Dataset images/IMD*/IMD*_Dermoscopic_Image/')
		# imagenames_list = []
		# for folder in folders:
		# 	for f in glob.glob(folder+'*'):
		# 		imagenames_list.append(f)
		# 		print(os.path.basename(f))

	# 	read_images = []
	# 	#n = 0

	# 	for image in imagenames_list:
	# 		read_images.append(cv.imread(image,0))
	# 		#print("Imagem ",image," lida com sucesso!")
	# 		#n+=1
	# 	for i in range(len(read_images)):
	# 		x = MyImage(read_images[i])
	# 		print(str(x))

	# class MyImage:
	#     def __init__(self, img_name):
	#         self.img = cv.imread(img_name)
	#         self.__name = img_name

	#     def __str__(self):
	#         return self.__name
		# f = open('/home/alex/Documentos/TCC2/PH2Dataset/PH2_simp', 'r')
		# g = open('/home/alex/Documentos/TCC2/PH2Dataset/PH2_simp2.txt','a')

		# for line in f:
		# 	valores = line.split()
		# 	v = []
		# 	v.append(str(valores[0])+'.bmp '+str(valores[1]+'\n'))
		# 	g.writelines(v)
			
		# g.close()
		# f.close()
		# print(n)
		# images = [cv.imread(file) for file in glob.glob("/home/alex/Documentos/TCC2/*.jpg")]
		
		# for i in range(len(images)):
		# 	cv.imshow('img',images[i]) 
		# 	cv.waitKey(0) 

	# 	def show(img,X,D):
	# 	#print("\nShannon index:: ",X)
	# 	#print("Simpson index: ",D)
	# 	print(img.size) #Total de Pixels
	# 	print(img.shape) #Dimensoes X,Y
	# 	print('---------------------------------------------------------------------------')

	# def write_file(vet,img):
	# 	folders = glob.glob('/home/alex/Documentos/TCC2/PH2Dataset/PH2 Dataset images/IMD*/IMD*_Dermoscopic_Image/')
	# 	imgnames_list = []
	# 	for folder in folders:
	# 		for f in glob.glob(folder+'*'):
	# 			imgnames_list.append(os.path.basename(f))

	# 	) 

	# 	ph2 = open('/home/alex/Documentos/TCC2/PH2Dataset/PH2_simp2.txt', 'r')
	# 	for line in ph2:
	# 		valores = line.split()
	# 		for w in range(len(imgnames_list)):
	# 			if(valores[0] == imgnames_list[w]):
	# 				if(valores[1] != 2):
	# 					with open("/home/alex/Documentos/TCC2/PH2Dataset/teste_caracteristicas.txt",'a') as arqv:
	# 						arqv.write(str(0)+" 1:"+str(X)+" 2:"+str(D)+'\n')
	# 					#v  = []
	# 					#v.append(str(0)+" 1:"+str(X)+" 2:"+str(D)+'\n')
	# 					#arq.writelines(v)
	# 					#arq.close()
	# 				else:
	# 					with open("/home/alex/Documentos/TCC2/PH2Dataset/teste_caracteristicas.txt",'a') as arq:
	# 						arq.write(str(1)+" 1:"+str(X)+" 2:"+str(D)+'\n')
	# 					#v = []
	# 					#v.append(str(1)+" 1:"+str(X)+" 2:"+str(D)+'\n')
	# 					#arq.writelines(v)
	# 					#arq.close()
read()