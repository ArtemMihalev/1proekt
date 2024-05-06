from PIL import Image, ImageFilter
import os
os.makedirs("newpapka", exist_ok = True)
def filter(mesto1, mesto2):
    image = Image.open(mesto1)
    new = image.filter(ImageFilter.SHARPEN)
    new.save(mesto2)

for file in os.listdir("06.05"):
    if file.endswith(".jpg"):
        path1 = os.path.join("06.05",file)
        path2 = os.path.join("newpapka",file)
        filter(path1,path2)
