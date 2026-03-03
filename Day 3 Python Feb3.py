import qrcode
from PIL import Image
data = "https://www.youtube.com/watch?v=lsqbpw67hSs&list=RDlsqbpw67hSs&start_radio=1"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)
qr.add_data(data)
qr.make(fit=True)

apple = qr.make_image(
    fill_color="red",
    back_color="white"
)

apple.save("MyQRCode2.jpg")
apple = Image.open("MyQRCode2.jpg")
apple.show()
########################################
veg = [90, 99, 100]
for x in veg:
    print(x)
