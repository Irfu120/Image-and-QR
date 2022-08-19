# -*- coding: utf-8 -*-
"""

@author: Irfan
"""
# convert images to pdf
# pip install fpdf
from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
    pdf.output("yourfile.pdf","F")











