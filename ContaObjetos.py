import numpy as np
import cv2 as cv
import sys
import queue
from matplotlib import pyplot as plt

img  = cv.imread('/home/alex/Documentos/TCC 2/teste/ISIC_0000026.jpg', 0)
#img[img  > 127] = 255
#img[img  <= 127] = 0

altura  = img.shape[0]
largura = img.shape[1]
print ("altura  ",  altura)
print ("largura ", largura)
print ("pixels  ", altura*largura)
print ("................")
print ("Contando Objetos")
print ("................")


def conheceVizinhanca(img, q, cont, visitado):
	while(q.qsize() > 0):
		pixel = q.get()
		x = pixel[0]
		y = pixel[1]
		if(x > 0 and x < altura and y > 0 and y < largura):
			img[x, y] = 200 - cont*2
			visitado[x, y] = True
			q.put([x+1, y])
			q.put([x-1, y])
			q.put([x, y+1])
			q.put([x, y-1])	

def contar(img):
	contador = 0
	visitado = img < 255

	for x in range (0, altura):
		for y in range (0, largura):
			if not visitado[x, y]:
				contador += 1
				q = queue.Queue()
				q.put([x, y])
				conheceVizinhanca(img, q, contador, visitado)
				cv.putText(img, str(contador), (y,x), cv.FONT_ITALIC, 0.4, 255, 2)
	print("Total: ", contador, "objeto(s)")
		 

def areas(img):
	hist, bin = np.histogram(img.ravel(), 256, [1,254])
	contador = 0

	for i in range (254, 1, -1):
		if hist[i] > 0:
			contador += 1
			print("Objeto {0:3d} --> Nivel de cinza".format(contador))
			print("{1:3d} --> area: {0:7d} pixels".format(hist[i]))
	print("Area Total: ", np.sum(hist), "pixels")
	return contador, np.max(hist)

contar(img)
contador, max = areas(img)
plt.hist(img.ravel(), 256,[1,254])
plt.xlabel('Nivel de Cinza')
plt.ylabel('Pixels')
plt.title('Histograma de niveis de cinza da imagem')
plt.axis([200-(1+contador*2), 200, 0, max+100])
plt.show()

cv.imshow("contados",img)
cv.imwrite("shapesMarcados.png",img)
cv.waitKey()
cv.destroyAllWindows()