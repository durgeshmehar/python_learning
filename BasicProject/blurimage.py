from PIL import Image, ImageFilter

before =Image.open("./r.jpg")
after=before.filter(ImageFilter.BoxBlur(100))
after.save("blur5.jpg")