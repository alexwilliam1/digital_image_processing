# import the necessary packages
import imutils
import cv2
from math import sqrt

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("../PH2/Segmentadas/MelanomaSegmentada/IMD411_lesion.bmp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

print('POINTS \nextLeft: {} -> RED \nextRight: {} -> GREEN \nextTop: {} -> BLUE \nextBot: {} -> TEAL' .format(
    extLeft, extRight, extTop, extBot))

# print('{} {}' .format(extLeft[0], extLeft[1]))

# Show the axis with the biggest distance
print('\n--------------AXIS DIFF--------------')
print('AXIS X: {} - {} = {}'.format(extRight[0],
                                    extLeft[0], abs(extRight[0] - extLeft[0])))
print('AXIS Y: {} - {} = {}'.format(extBot[1],
                                    extTop[1], abs(extBot[1] - extTop[1])))

#difX, difY = 0

difX = abs(extRight[0] - extLeft[0])
difY = abs(extBot[1] - extTop[1])

print('\n----------DIAMETER CALC------------------')

# Diametro
# É a maior distância entre dois pontos (p1 = (x1, y1) e p2 = (x2, y2)) pertencentes
# ao contorno da região de interesse, que pode ser formalizada por:

# D = sqrt(((x1-x2)**2)+((y1-y2)**2))
# D = sqrt(pow((x1-x2),2)+pow((y1-y2),2))

if(difX > difY):
    D = sqrt(pow((extLeft[0] - extRight[0]), 2) +
             pow((extLeft[1] - extRight[1]), 2))
    print('Diameter if axis X is Bigger: {}' .format(D))
else:
    D = sqrt(pow((extTop[0] - extBot[0]), 2) +
             pow((extTop[1] - extBot[1]), 2))
    print('Diameter if axis Y is Bigger: {}' .format(D))


# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
cv2.circle(image, extRight, 6, (0, 255, 0), -1)
cv2.circle(image, extTop, 6, (255, 0, 0), -1)
cv2.circle(image, extBot, 6, (255, 255, 0), -1)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
