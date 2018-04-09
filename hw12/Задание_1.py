#Вариант 1
#Задание 1


with open("/Users/ekaterinazenkova/Desktop/Corpus.xml","r", encoding="utf-8") as f:
    line = f.readline()
    a = 0
    teg = "</teiHeader>"
    while line:
        if not teg in line:
            a += 1
        else:
            break
        line = f.readline()
        
with open("/Users/ekaterinazenkova/Desktop/text1.txt","w", encoding="utf-8") as o:
    o.write('Количество строк: ')
    o.write(str(a))



    


    

