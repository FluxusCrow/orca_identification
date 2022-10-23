'''Module to extract all orca images from the Photo-identification 
Catalogue file. Images are saved under data/images/ as png.
'''

import fitz

# get data
catalogue = "data/orca_catalogue_2019.pdf"
pdf = fitz.open(catalogue)

# Scans each pdf page for images and saves each image
for page in range(22,183):
    for img in pdf.get_page_images(page):
        xref = img[0]
        picture = fitz.Pixmap(pdf, xref)
        picture.save("data/images/p%s-%s.png" % (page, xref), output="png")
        picture = None
