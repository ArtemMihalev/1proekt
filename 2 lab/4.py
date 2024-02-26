import random
s = ""
otvet = ""
k = 0
prav = 0
while k != 3:
    a = int(random.random() * 10)
    b = int(random.random() * 10)
    s = str(a) + " + " + str(b) + " ="
    print(s,end = "")
    otvet = int(input())
    if otvet == (a + b):
        print("верно")
        prav += 1
    else:
        print("неверно")
        k = k+1
print("Игра окончена. Правильных ответов: ", prav)
