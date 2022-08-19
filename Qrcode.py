# -*- coding: utf-8 -*-
"""

@author: Irfan
"""

import pyqrcode
import png
from pyqrcode import QRCode
#string which represents the qr code

I = "www.linkedin.com/in/irfan-ansari-644504236"
#Generate QR code

url = pyqrcode.create(I)
#create and save the svg file naming "myqr.svg"

url.svg("irfan.svg", scale = 8)
#Create and save the png file naming "myqr.png"
url.png("irfan.png", scale = 6)
