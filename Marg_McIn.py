import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln
from math import sqrt
import glob
import os

def main():
	img = cv.imread("/home/alex/Área de Trabalho/ISIC/GRAY/Melanoma/ISIC_GRAY72.png",0)
	vetor = [1212,48,56,58,0,1,0,3,0,0,62,2]
	N = populacaoTotal(vetor)
	S = especiesPresentes(vetor)
	margalef(S,N)
	print("McIntosh: ",McIntosh(N,vetor))


def populacaoTotal(vetor):
	N=0

	for x in range(1,12):
		N = N + vetor[x]

	print("\n\nNumero total de individuos da amostra (N): ",N)

	return N

def especiesPresentes(vetor):		
	S=0

	for y in range(1,12):
		if vetor[y] != 0:
			S += 1 

	print("Número de espécies presentes na amostra (S): ",S)

	return S

def percorre(img):
	vetor = []

	for x in range(256):
		vetor.append(0)

	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			pixel = img.item(i,j)
			vetor[pixel] += 1

	#for a in range(0,256):
		#print("Nível {0} ===> {1}p" .format(a, vetor[a]))

	return vetor

def margalef(S,N):
	print("Margalef: ",(S-1)/ln(N))

def Ucalc(vetor):
	def p(n):
		if n is 0:
			return 0
		else:
			return n**2

	return sqrt(sum(p(vetor[i]) for i in range(1,12) if vetor[i] is not 0))

def McIntosh(N,vetor):
	U = Ucalc(vetor)

	return ((N-U)/(N-sqrt(N)))

main()