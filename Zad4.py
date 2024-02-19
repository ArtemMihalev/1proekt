clr1 = input()
clr2 = input()
if (clr1 ==  "красный" or clr2 == "красный") and (clr1 == "синий" or clr2 == "синий"):
    res = "фиолетовый"
elif (clr1 == "красный" or clr2 == "красный") and (clr1 == "жёлтый" or clr2 == "жёлтый"):
    res = "оранжевый"
elif (clr1 == "синий" or clr2 == "синий") and (clr1 == "жёлтый" or clr2 == "жёлтый"):
    res = "зелёный"
else:
    res = "ошибка"
print(res)
