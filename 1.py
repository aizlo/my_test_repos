while 1:
    i = input("Введите числа разделенные пробелом")
    i = i.split(" ")
    a = 0
    while a < len(i):
        i[a] = int(i[a])

        a = a + 1
    z = 0
    for c in i:
        z = z + c
    print(z)

