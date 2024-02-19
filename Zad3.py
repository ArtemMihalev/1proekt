def f(a):
    if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
        return True
    else:
        return False
year = int(input())
if f(year) == True:
    print("Год ", year, " - Високосный")
else:
    print("Этот год не високосный")