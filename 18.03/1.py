for i in range(len(a)):
    f = False
    for j in range(a[i],len(a)):
        if a[j] == a[i]:
            print(a[j])
            f = True
            break
    if f == True:
        break