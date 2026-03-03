#########################################################
#I am creating a qrcode with a logo of my company
#QRCode, Pillow also known as PIL

import qrcode
from PIL import Image

#***** WE ARE WORKING WITH CREATION OF QRCODE
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

url = "https://csumb.edu/"

QRcode.add_data(url) #now i added URL variable data to my QRcode i created above

QRcode.make(fit=True)

QRimg = QRcode.make_image(fill_color= (0, 128, 255), back_color="white").convert("RGB")

#****** WE ARE WORKING ON CSUMB LOGO *******
