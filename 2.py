try:
    a = [3, 4, 5]
    b = int(input('Введите число:\n'))
    c = a[0] /b
except (ZeroDivisionError) as e:
    print(e)

