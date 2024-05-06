from PIL import Image
img = Image.open("otkr.jpg")
new_img = img.crop((100, 100, 100, 100))
newname = "new.jpg"
new_img.save(newname)