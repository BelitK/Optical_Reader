# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])
upper = np.array([45, 45, 45])
shapeMask = cv2.inRange(image, lower, upper)
# find the contours in the mask
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_LIST,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.imshow("Mask", shapeMask)
# loop over the contours
print(cnts)
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

#cropped_image = image[cnts[0][::-1], cnts[1][::-1]]
cv2.imshow("Image", image)
cv2.waitKey(0)
