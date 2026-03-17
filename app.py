import streamlit as st
import qrcode
from PIL import Image  # allows us to use Image functions from Pillow library

# Optional improvement (not required):
# st.title("QR Code Generator")

data = st.text_input("Enter text or URL", "Python is fun")  # creates an input box; default text is "Python is fun"
img = qrcode.make(data)  # generate QR code from whatever user enters
img.save('MyQRCode1.jpg')  # save QR code as image file
img = Image.open("MyQRCode1.jpg")
# open the saved QR code image

st.image(img)
# display the QR code in the Streamlit web app