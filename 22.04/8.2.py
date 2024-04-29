from PIL import Image
paskha = Image.open("paskha.jpg")
novgod = Image.open("novgod.jpg")
f = {"paskha":paskha,
     "novgod":novgod}
vibor = input()
if vibor == "paskha":
    paskha.show()
elif vibor == "novgod":
    novgod.show()
else:
    print("Нет такого праздника")