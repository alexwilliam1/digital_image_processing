import cv2 as cv

img = cv.imread('../PH2/Segmentadas/MelanomaSegmentada/IMD285_lesion.bmp', 0)
img2 = cv.imread('../PH2/Segmentadas/MelanomaSegmentada/IMD285_lesion.bmp')
#img3 = cv.imread("/home/alex/Área de Trabalho/PH2/Histogram Equalization/GREEN/Melanoma/pic0000.png")
#img4 = cv.imread("/home/alex/Área de Trabalho/PH2/Histogram Equalization/GRAY/Melanoma/pic0000.png")
cv.imshow("blue quantized", img)
cv.imshow("blue", img2)
# cv.imshow("green",img3)
# cv.imshow("gray",img4)
cv.waitKey(0)
