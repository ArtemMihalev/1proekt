from PIL import Image
img = Image.open("otkr.jpg")
new_img = img.crop((100, 100, 100, 100))
new_img.save("new.jpg")