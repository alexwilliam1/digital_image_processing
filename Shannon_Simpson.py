import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
import glob
import os

def main():

	# path4 = "/home/alex/Documentos/TCC2/teste/*.png"
	# carac4 = "/home/alex/Documentos/TCC2/teste/test.libsvm"
	# images = read(path4)
	# for i in range(len(images)):
		# (bl,gr,re) = cv.split(images[i])

		# zeros = np.zeros(images[i].shape[:2], dtype = "uint8")

		# red = cv.merge([zeros,zeros,re])
		# green = cv.merge([zeros,gr,zeros])
		# blue = cv.merge([bl, zeros, zeros])
		images = cv.imread("/home/alex/Área de Trabalho/PH2/RED/NaoMelanoma/PH2_RED106.png")
		cv.imshow("red",images)
		cv.waitKey(0)
		#print("IMAGEM",i+1)
		vetor = percorre(images)
		N = populacao(vetor)
		#write_mela(vetor,N,carac4)
		show(images,N,vetor)

def show(img,N,vet):
	#print("\nShannon index:: ",X)
	#print("Simpson index: ",D)
	Sh = shannon(vet,N)
	Si = simpson(vet,N)
	print("Shannon: ",Sh)
	print("Simpspn: ",Si)
	print("População contada: ",N)
	print("Total de pixels: ",img.size) #Total de Pixels
	print(img.shape) #Dimensoes X,Y
	print('-----------------------------------------------------')

def write_n_mela(vet,N,path):
	Sh = shannon(vet,N)
	Si = simpson(vet,N)
	with open(path,'a') as arq:
		arq.write(str(0)+" 1:"+str(Sh)+" 2:"+str(Si)+'\n')

def write_mela(vet,N,path):
	Sh = shannon(vet,N)
	Si = simpson(vet,N)
	with open(path,'a') as arq:
		arq.write(str(1)+" 1:"+str(Sh)+" 2:"+str(Si)+'\n')

def read(path):
	images = [cv.imread(file) for file in glob.glob(path)]

	return images

def percorre(img):
	vetor = []
	for x in range(256):
		vetor.append(0)

	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			pixel = img.item(i,j,2)
			#print(pixel)
			vetor[pixel] += 1

	#for a in range(0,256):
		#print("Nível {0} ===> {1}p" .format(a, vetor[a]))

	return vetor

def populacao(vet):
	N=0
	
	for x in range(1,256):
		N = N + vet[x]

	return N

def shannon(data,N):
	def p(n,N):
		if n is 0:
			return 0
		else:
			return (float(n)/N)*ln(float(n/N),10)

	return -sum(p(data[i],N) for i in range(1,256) if data[i] is not 0)

def simpson(data,N):
	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N) ** 2)

	return 1-(sum(p(data[n],N) for n in range(1,256) if data[n] is not 0))

main()
	