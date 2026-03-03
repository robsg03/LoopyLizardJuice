# creating QR with logo of my ocmpany
#QRcode / Pillow
import qrcode
from PIL import Image

#Working with QRcode
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

url = "https://csumb.edu/"

QRcode.add_data(url)


QRcode.make(fit=True)

#QRimg = QRcode.make_image(fill_color= (0, 120, 0), back_color = "white" ). convert("RGB")
QRimg = QRcode.make_image(fill_color="forestgreen", back_color="white")

logo = Image.open("csumb_logo.jpg")

logo_size = QRimg.size[0] // 4

logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

pos = (
    (QRimg.size[0] - logo.size[0]) // 2,
    (QRimg.size[1] - logo.size[1]) // 2
)

QRimg.paste(logo, pos, logo)

QRimg.save("CSUMB_logo.png")
QRimg.show ()

#///////////////////////////
#New function HOW TO MERGE FILES IN PYTHON
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")

with open("merged15.pdf", "wb") as f:
    merger.write(f)

    merger.close()