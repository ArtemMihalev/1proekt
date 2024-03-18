a = "123"
b = int(list(a))
print(sum(b))
def delen(a):
    if isinstance(a) == True:
        if a / 100 != 0:
            a = a / 100
            return a
        else:
            return "ZeroDivisionError"
    elif isinstance(a) == False:
        return "ValueError"
a = 100
print(delen(a))