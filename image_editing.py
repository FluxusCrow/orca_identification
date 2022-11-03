'''Module to extract the shape of fins and eye patterns and save them.
'''

import numpy as np
import cv2
import os
import sys
import math

# change working directory to directory of this file
os.chdir(sys.path[0])

# create folder "data/images_contour" if not existing already
if not "images_contour" in os.listdir("data"):
    os.mkdir("data/images_contour")

#cv2.imshow("test", edges)
#cv2.waitKey(0)

# Iterate through all images in "images_original", extract most dominant edges and save new file
for source_image in os.listdir("data/images_original"):
    if not source_image in os.listdir("data/images_contour"):
        img = cv2.imread(f"data/images_original/{source_image}")
        img = cv2.GaussianBlur(img, (3,3),0)
        edges = cv2.Canny(img, 200, 300)
        cv2.imwrite(f"data/images_contour/{source_image}", edges)
