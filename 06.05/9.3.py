import csv

itogo = 0

with open("spisok.csv","r",encoding = "utf-8") as file:
    spisok = csv.reader(file)
    next(spisok)
    for f in spisok:
        name = f[0]
        kolvo = int(f[1])
        cena = int(f[2])
        itogo += kolvo*cena
        print(name, " - ", kolvo, " шт за ", cena)
print(itogo)