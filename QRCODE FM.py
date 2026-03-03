# creating QR with logo of my company
#QRcode / Pillow
import qrcode
from PIL import Image

#Working with QRcode
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=4
)

url = "https://instagram.com/asfarmersmarket_csumb/"
QRcode.add_data(url)
QRcode.make(fit=True)

#QRimg = QRcode.make_image(fill_color= (0, 120, 0), back_color = "white" ). convert("RGB")
QRimg = QRcode.make_image(fill_color="forestgreen", back_color="white").convert("RGBA")

logo = Image.open("asfmlogo.png").convert("RGBA")

logo_size = QRimg.size[0] // 3
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

pos = (
    (QRimg.size[0] - logo.size[0]) // 2,
    (QRimg.size[0] - logo.size[1]) // 2
)

QRimg.paste(logo, pos, logo)

QRimg.save("asfm_qr.png")
QRimg.show ()
