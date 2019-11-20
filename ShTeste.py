import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
import glob
import os

def main():
	folders = glob.glob('/home/alex/Documentos/TCC2/PH2Dataset/PH2 Dataset images/IMD*/IMD*_Dermoscopic_Image/')
	imgnames_list = []
	for folder in folders:
		for f in glob.glob(folder+'*'):
			imgnames_list.append(os.path.basename(f))

	images = read()
	for i in  range(len(images)):
		print('IMAGEM', i+1)
		vetor = percorre(images[i])
		SH = shannon(vetor,images[i])
		SI = simpson(vetor,images[i])
		write_file(imgnames_list[i],SH,SI)
		show(images[i],SH,SI)
		#cv.imshow('Imagem',images[i])
		#cv.waitKey(0)	

def show(img,SH,SI):
	print("\nShannon index:: ",SH)
	print("Simpson index: ",SI)
	print(img.size) #Total de Pixels
	print(img.shape) #Dimensoes X,Y
	print('---------------------------------------------------------------------------')

def write_file(nameFile,SH,SI):
	ph2 = open('/home/alex/Documentos/TCC2/PH2Dataset/PH2_simp2.txt', 'r')
	for line in ph2:
		valores = line.split()
		if nameFile == valores[0]:
			if valores[1] != '2':
				with open("/home/alex/Documentos/TCC2/PH2Dataset/caracteristicas.libsvm",'a') as arq:
					arq.write(str(0)+" 1:"+str(SH)+" 2:"+str(SI)+'\n')
					print(valores[0])
				break
			else:
				with open("/home/alex/Documentos/TCC2/PH2Dataset/caracteristicas.libsvm",'a') as arq:
					arq.write(str(1)+" 1:"+str(SH)+" 2:"+str(SI)+'\n')
					print(valores[0])
				break
	
	print("Arquivo "+nameFile+" não encontrado na pasta!")
			
def read():
	folders = glob.glob('/home/alex/Documentos/TCC2/PH2Dataset/PH2 Dataset images/IMD*/IMD*_Dermoscopic_Image/')
	imagenames_list = []
	for folder in folders:
		for f in glob.glob(folder+'*.bmp'):
			imagenames_list.append(f)

	read_images = []

	for image in imagenames_list:
		read_images.append(cv.imread(image,0))

	return read_images

def percorre(img):
	vetor = []
	for x in range(256):
		vetor.append(0)

	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			pixel = img.item(i, j)
			#print(pixel)
			vetor[pixel] += 1

	#for a in range(0,256):
	#	print("Nível {0} ===> {1}p" .format(a, vetor[a]))
	return vetor

def shannon(data,img):
	def p(n,N):
		if n is 0:
			return 0
		else:
			return (float(n)/N)*ln(float(n/N),10)

	return -sum(p(data[i],img.size) for i in range(256) if data[i] is not 0)

def simpson(data,img):
	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N) ** 2)

	return 1-(sum(p(data[n],img.size) for n in range(len(data)) if data[n] is not 0))

main()