mesto = int(input())
if mesto % 2 == 0 and mesto <= 20:
    print("купе нижнее")
elif mesto % 2 != 0 and mesto <= 20:
    print("купе верхнее")
elif mesto % 2 == 0 and mesto >= 20:
    print("плацкарт нижнее")
elif mesto % 2 != 0 and mesto >= 20:
    print("плацкарт верхнее")
