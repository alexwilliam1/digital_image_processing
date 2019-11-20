import sys
import cv2 as cv
import numpy as np
from math import log as ln

def main():
	vet = [10,2,8,20,10]

	X = sdi(vet)
	D = simpson(vet)

	print("Indice de Shannon para esta populacao: ", round(X, ndigits=4))
	print("Indice de Simpson para esta populacao: ", round(D, ndigits=4))

def sdi(data):
	N = 50

	print("LOG: ", ln(float(data[0]/N),10))

	for i in range(len(data)):
		print(data[i])

	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N)) * ln(float(n/N),10)

	return -sum(p(data[n], N) for n in range(len(data)) if data[n] is not 0)

def simpson(data):
	N=50

	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N) ** 2)

	return 1-(sum(p(data[n], N) for n in range(len(data)) if data[n] is not 0))

main()
		