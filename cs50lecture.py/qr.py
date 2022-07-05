import os
import qrcode

img=qrcode.make("https://youtube.com/shorts/5X1vkalePEI?feature=share")
img.save("qr.png","PNG")
os.system("open qr.png")
