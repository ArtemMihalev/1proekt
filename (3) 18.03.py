def mag(a):
    b = a.split(".")
    res = b[2]
    res = res[-2:]
    if int(b[0]) * int(b[1]) == int(res):
        return True
    else:
        return False
print(mag("02.11.2022"))