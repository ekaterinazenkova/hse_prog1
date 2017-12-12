print("Задание3")
list = []
word = input("Введите слово: ")
while word != "":
    list.append(word)
    word = input("Введите слово: ")
#with open("/Users/ekaterinazenkova/Desktop/control_languages.txt", 'r', encoding="utf-8") as f: (этот путь был на моём компьютере)
with open("control_languages.txt", 'r', encoding="utf-8") as f:
    for word in list:
#        print (word)
        language_exist = 0
        line = f.readline()
        while line:
            line = line.rsplit('    ', 1)
            if word in line[0]:
                print(line[0]+"-"+line[1]+"-"+line[2])
                language_exist = 1
            line = f.readline()
        if language_exist == 0: print("Языка в списке нет!")

    
    
    
