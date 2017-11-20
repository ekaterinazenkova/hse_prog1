with open("/Users/ekaterinazenkova/Desktop/text1.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff","")

lines = text.splitlines()

al = 0
st = 0
for x in lines:
    st += 1
    dlina = len(x.split())
    al += dlina
    
print("Средняя длина строки: ", int(al/st))

