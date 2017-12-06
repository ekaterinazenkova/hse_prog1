a = input("Введите слово: ")
list =[]
while a != "":
        list.append(a)
        a = input("Введите слово: ")

with open ("text.txt", "w", encoding="utf-8") as f:
        for i in range(len(list)):
            l = list[i]
            m = ""
            for n in range(len(l) - 1, -1, -1):
                m = m + l[n]
            for n in range(len(m)):
                if ((n + 1) % 3) != 0:
                    f.write(m[n])
            f.write("\n")
