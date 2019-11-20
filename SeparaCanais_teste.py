import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
#Read image
im = cv.imread('/home/alex/Documentos/TCC2/PH2Dataset/MelanomaSegmentada/IMD058_lesion.bmp')

#Display image
#im.show()

#Applying a filter to the image
#im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
#im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB

#cv.imshow("test",im)

(b,g,r) = cv.split(im)

zeros = np.zeros(im.shape[:2], dtype = "uint8")

red = cv.merge([zeros,zeros,r])
green = cv.merge([zeros,g,zeros])
blue = cv.merge([b, zeros, zeros])

cv.imwrite("/home/alex/Documentos/TCC2/teste/resultado/test_red.png",red)
cv.imwrite("/home/alex/Documentos/TCC2/teste/resultado/test_green.png",green)
cv.imwrite("/home/alex/Documentos/TCC2/teste/resultado/test_blue.png",blue)
#cv.waitKey(0)


#Viewing EXIF data embedded in image
