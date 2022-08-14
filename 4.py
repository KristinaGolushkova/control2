try:
    a = [66, 3, 5]
    b = int(input("Введите число:\n"))
    c = a[0] / b
    print(c)
except (ZeroDivisionError, ValueError) as e:
    print(e)
    if b == 0:
        print('Ошибка, деление на 0')
