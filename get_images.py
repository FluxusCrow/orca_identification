'''Module to extract all orca images from the Photo-identification 
Catalogue file. Images are saved under data/images/ as png.
'''

import fitz
import os
import sys

# change working directory to directory of this file
os.chdir(sys.path[0])

# create folder "data/images_original" if not existing already
if not "images_original" in os.listdir("data"):
    os.mkdir("data/images_original")

# get data
catalogue = "data/orca_catalogue_2019.pdf"
pdf = fitz.open(catalogue)

# Scans each pdf page for images and saves each image
for page in range(22,183):
    for img in pdf.get_page_images(page):
        xref = img[0]
        picture = fitz.Pixmap(pdf, xref)
        if not "p%s-%s.png" % (page, xref) in os.listdir("data/images_original"):
            picture.save("data/images_original/p%s-%s.png" % (page, xref), output="png")
            picture = None
