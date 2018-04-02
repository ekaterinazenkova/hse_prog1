import re
with open ('Лихтенштейн.htm', 'r', encoding='utf-8') as f:
    text = f.read()
    result=""
    text1 = re.search('"P36".*', text) ## id поля Столица в WiKi
#    print(text1.group(0))
    text2 = re.search('title=.*', text1.group(0))
#    print(text2.group(0))
    text3 = re.search('[А-Я][а-я]+', text2.group(0))
    result = text3.group(0)

with open ('text.txt', 'w', encoding='utf-8') as n:
    n.write(result)
    
