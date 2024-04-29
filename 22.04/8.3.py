from PIL import Image, ImageDraw, ImageFont
img = Image.open("otkr.jpg")
name = input()
new_img = img.crop((100, 100, 100, 100))
draw = ImageDraw.Draw(new_img)
text = name + " , поздравляю!"
font = ImageFont.truetype("arial.ttf", 28)
draw.text((100,100),text, fill = red, font = font)
new_name = "new.png"
new_img.save(new_name)