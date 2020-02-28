import numpy as np
import cv2 as cv
import sys

'''# Let's load a simple image with 3 black squares 
image = cv.imread('../PH2/Segmentadas/MelanomaSegmentada/IMD285_lesion.bmp') 
  
# Grayscale 
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
  
# Find Canny edges 
edged = cv.Canny(gray, 30, 200) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv.findContours(edged,  
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
  
cv.imshow('Canny Edges After Contouring', edged) 
cv.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
cv.drawContours(image, contours, -1, (0, 255, 0), 3) 
  
cv.imshow('Contours', image) 
cv.waitKey(0) 
cv.destroyAllWindows() '''


def main():
    
    window_name = ('Sobel Demo - Simple Edge Detector')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    

    # Load the image
    src = cv.imread('../PH2/Segmentadas/MelanomaSegmentada/IMD285_lesion.bmp', cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image: ' + 'IMD285_lesion.bmp')
        return -1
    
    
    src = cv.GaussianBlur(src, (3, 3), 0)
    
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    # Gradient-Y
    # grad_y = cv.Scharr(gray,ddepth,0,1)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    
    cv.imshow(window_name, grad)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main()