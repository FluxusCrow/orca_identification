'''Module to extract the shape of fins and eye patterns and save them.
'''

import numpy as np
import cv2

# get image
img = cv2.imread("data/images/p29-96.png")

# extract the most dominant edges
edges = cv2.Canny(img, 200, 290)

#cv2.imshow("test", edges)
#cv2.waitKey(0)

# save the file
cv2.imwrite("data/test.png", edges)