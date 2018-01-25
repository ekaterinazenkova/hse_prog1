import string
import random
with open ("/Users/ekaterinazenkova/Desktop/text.txt", "r", encoding="utf-8") as f:                
    text =""
    line = f.readline()
    while line:
        line = line.strip() #удаляю пробелы в начале и конце строки
        text += line # это так покороче записывают: text = text + line
        line = f.readline()
        
#    table_punct = str.maketrans({key: None for key in string.punctuation})
#    text = text.translate(table_punct)
# ниже то же что и две строчки выше, только как первоклассник бы сделал
    for c in string.punctuation:
        text = text.replace(c,"")

        
    text = text.lower()
    words = text.split(' ')
        
##    print (words)  это для отладки было


    for i, word in enumerate(map(list, words)):
##        print(''.join(word)
#)  это для отладки было
        random.shuffle(word)

        words[i] += ' ' + ''.join(word)

        random.shuffle(word)

        words[i] += ' ' + ''.join(word)

        random.shuffle(word)

        words[i] += ' ' + ''.join(word)

        print(words[i])
import csv



with open('list_to_csv.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow([item])



        
