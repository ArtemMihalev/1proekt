def f(a):
    if len(a) % 2 == 0:
        pol = int(len(a) / 2)
        b = list(a)
        s1 = 0
        s2 = 0
        for i in range(0,pol):
            s1 = s1 + int(b[i])
        for i in range(pol,len(a)):
            s2 = s2 + int(b[i])
        if s1 == s2:
            return True
        else:
            return False
    else:
        return "ошибка"
print(f("3333"))
