def delen(a):
    try:
        b = 100 / a
        return b
    except ValueError:
        print("Введена строка")
    except ZeroDivisionError:
        print("введено не то число")
print(delen(100))