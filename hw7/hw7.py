with open("/Users/ekaterinazenkova/Desktop/Body piercing.txt", "r", encoding="utf-8") as f:
    text =""
    line = f.readline()
    while line:
        line = line.strip() #удаляю пробелы в начале и конце строки
        text += line # это так покороче записывают: text = text + line
        line = f.readline()
   
 
   
    text = text.lower()
    words = text.split(' ')
    d = 0
    for word in words:
        s = word[-3:]
        if s == "ing":
            d += 1

            
    k = 1 #здесь мы учитываем, что во второй раз было введено слово, заканчивающееся на "-ing"
    slovo = input("Type a word: ")
    dop = input("Type a word that ends with '-ing': ")
    for end in slovo:
        p = end[-3:]
        if p == "ing":
            k += 1
        
        
 

print("Слов в тексте, заканчивающихся на '-ing': ",d)
print("Введённых слов, которые заканчиваются на '-ing': ",k)
