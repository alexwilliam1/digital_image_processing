import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
import glob
import os

def main():
	cor = "RED"
	PH2(cor)
	ISIC(cor)

def PH2(cor):
	ph2NaoMela = "/home/alex/Área de Trabalho/PH2/LBP/NãoMelanoma/*.png"
	caracNaoMela = "/home/alex/Documentos/TCC2/Caracteristicas/LBP_caracPH2.libsvm"
	NaoMelanoma = read(ph2NaoMela)
	print("-----BASE PH2 NÃO MELANOMA LIDA-----")
	for i in range(len(NaoMelanoma)):
		print('PH2 LBP NAO MELANOMA:', i+1)
		vetor = percorre(NaoMelanoma[i])
		N = populacao(vetor)
		write_n_mela(vetor,N,caracNaoMela)
		show(NaoMelanoma[i],N)

	ph2Mela = "/home/alex/Área de Trabalho/PH2/LBP/Melanoma/*.png"
	caracMela = "/home/alex/Documentos/TCC2/Caracteristicas/LBP_caracPH2.libsvm"
	Melanoma = read(ph2Mela)
	print("-----BASE PH2 MELANOMA LIDA-----")
	for i in range(len(Melanoma)):
		print('PH2 LBP MELANOMA',i+1)
		vetor = percorre(Melanoma[i])
		N = populacao(vetor)
		write_mela(vetor,N,caracMela)
		show(Melanoma[i],N)

def ISIC(cor):
	isicNaoMela = "/home/alex/Área de Trabalho/ISIC/LBP/NãoMelanoma/*.png"
	caracNaoMela = "/home/alex/Documentos/TCC2/Caracteristicas/LBP_caracISIC.libsvm"
	NaoMelanoma = read(isicNaoMela)
	print("-----BASE ISIC NÃO MELANOMA LIDA-----")
	for i in  range(len(NaoMelanoma)):
		print('ISIC LBP NAO MELANOMA', i+1)
		vetor = percorre(NaoMelanoma[i])
		N = populacao(vetor)
		write_n_mela(vetor,N,caracNaoMela)
		show(NaoMelanoma[i],N)

	isicMela = "/home/alex/Área de Trabalho/ISIC/LBP/Melanoma/*.png"
	caracMela = "/home/alex/Documentos/TCC2/Caracteristicas/LBP_caracISIC.libsvm"
	Melanoma = read(isicMela)
	print("-----BASE ISIC MELANOMA LIDA-----")
	for i in  range(len(Melanoma)):
		print('ISIC LBP MELANOMA', i+1)
		vetor = percorre(Melanoma[i])
		N = populacao(vetor)
		write_mela(vetor,N,caracMela)
		show(Melanoma[i],N)

def show(img,N):
	#print("\nShannon index:: ",X)
	#print("Simpson index: " ,D)
	print("Total pixels da img:",img.size) #Total de Pixels
	print("  População contada: %d" % N)
	print(img.shape) #Dimensoes X,Y
	print("Índices extraídos e salvos com sucesso!")
	print('----------------------------------------------------')

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
	filenames = glob.glob(path)
	filenames.sort()
	images = [cv.imread(file,0) for file in filenames]
	return images

def percorre(img):
	vetor = []
	for x in range(256):
		vetor.append(0)

	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			pixel = img.item(i,j)
			vetor[pixel] += 1
	#for a in range(0,256):
	#	print("Nível {0} ===> {1}p" .format(a, vetor[a]))
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