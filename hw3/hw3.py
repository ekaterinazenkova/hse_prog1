a = list(input("Введите слово: "))
for i,sym in enumerate(a) :
    a = a[: -1]
    a = "".join(a)
    print(a)
