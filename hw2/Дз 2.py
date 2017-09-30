a = input('Введите слово кириллицей:')

for i in range(len(a)-1,-1,-1):
    if a[i] == "з" or a[i] == "я":
        continue
    print(a[i])
