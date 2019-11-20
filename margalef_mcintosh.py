import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
from math import sqrt
import glob
import os

def main():
	cor = "GRAY"
	PH2(cor)
	#ISIC(cor)

def PH2(cor):
	ph2NaoMela = "/home/alex/Área de Trabalho/PH2/4/"+cor+"/NaoMelanoma/*.png"
	caracNaoMela = "/home/alex/Documentos/TCC2/Caracteristicas/PH2_4bits_"+cor+"_.libsvm"
	NaoMelanoma = read(ph2NaoMela)
	print("-----BASE PH2 NÃO MELANOMA LIDA-----")
	for i in range(len(NaoMelanoma)):
		print("PH2 "+cor+" NAO MELANOMA:", i+1)
		vetor = percorre(NaoMelanoma[i])
		N = populacao(vetor)
		write_n_mela(vetor,N,caracNaoMela)
		show(NaoMelanoma[i],N)

	ph2Mela = "/home/alex/Área de Trabalho/PH2/4/"+cor+"/Melanoma/*.png"
	caracMela = "/home/alex/Documentos/TCC2/Caracteristicas/PH2_4bits_"+cor+"_.libsvm"
	Melanoma = read(ph2Mela)
	print("-----BASE PH2 MELANOMA LIDA-----")
	for i in range(len(Melanoma)):
		print("PH2 "+cor+" MELANOMA",i+1)
		vetor = percorre(Melanoma[i])
		N = populacao(vetor)
		write_mela(vetor,N,caracMela)
		show(Melanoma[i],N)

def ISIC(cor):
	isicNaoMela = "/home/alex/Área de Trabalho/ISIC/GRAY/NaoMelanoma/*.png"
	caracNaoMela = "/home/alex/Documentos/TCC2/Caracteristicas/Mar_McI_ISIC.libsvm"
	NaoMelanoma = read(isicNaoMela)
	print("-----BASE ISIC NÃO MELANOMA LIDA-----")
	for i in  range(len(NaoMelanoma)):
		print('ISIC NAO MELANOMA', i+1)
		vetor = percorre(NaoMelanoma[i])
		N = populacao(vetor)
		write_n_mela(vetor,N,caracNaoMela)
		show(NaoMelanoma[i],N)

	isicMela = "/home/alex/Área de Trabalho/ISIC/GRAY/Melanoma/*.png"
	caracMela = "/home/alex/Documentos/TCC2/Caracteristicas/Mar_McI_ISIC.libsvm"
	Melanoma = read(isicMela)
	print("-----BASE ISIC MELANOMA LIDA-----")
	for i in  range(len(Melanoma)):
		print('ISIC MELANOMA', i+1)
		vetor = percorre(Melanoma[i])
		N = populacao(vetor)
		write_mela(vetor,N,caracMela)
		show(Melanoma[i],N)

def show(img,N):
	#print("\nShannon index:: ",X)
	#print("Simpson index: " ,D)
	print("Total pixels da img:",img.size) #Total de Pixels
	print("População contada:   %d" % N)
	print(img.shape) #Dimensoes X,Y
	print("Índices extraídos e salvos com sucesso!")
	print('----------------------------------------------------')

def write_n_mela(vet,N,path):
	Sh = shannon(vet,N)
	Si = simpson(vet,N)
	Ma = margalef(vet,N)
	Mc = McIntosh(vet,N)
	with open(path,'a') as arq:
		arq.write(str(0)+" 1:"+str(Ma)+" 2:"+str(Mc)+" 3:"+str(Sh)+" 4:"+str(Si)+'\n')

def write_mela(vet,N,path):
	Sh = shannon(vet,N)
	Si = simpson(vet,N)
	Ma = margalef(vet,N)
	Mc = McIntosh(vet,N)
	with open(path,'a') as arq:
		arq.write(str(1)+" 1:"+str(Ma)+" 2:"+str(Mc)+" 3:"+str(Sh)+" 4:"+str(Si)+'\n')

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

def margalef(vetor,N):
	S=0

	for y in range(1,256):
		if vetor[y] != 0:
			S += 1 

	return ((S-1)/ln(N))

def Ucalc(vetor):
	def p(n):
		if n is 0:
			return 0
		else:
			return n**2

	return sqrt(sum(p(vetor[i]) for i in range(1,256) if vetor[i] is not 0))

def McIntosh(vetor,N):

	U = Ucalc(vetor)

	return ((N-U)/(N-sqrt(N)))

def shannon(vetor,N):
	def p(n,N):
		if n is 0:
			return 0
		else:
			return (float(n)/N)*ln(float(n/N),10)

	return -sum(p(vetor[i],N) for i in range(1,256) if vetor[i] is not 0)

def simpson(vetor,N):
	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N) ** 2)

	return 1-(sum(p(vetor[n],N) for n in range(1,256) if vetor[n] is not 0))

main()