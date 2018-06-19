import csv
import re

with open ("_rbk2.xhtml", "r", encoding="utf-8") as f:
    line = f.read()
with open ("_rbk3.xhtml", "r", encoding="utf-8") as g:
    line = g.read()
with open ("_rbk4.xhtml", "r", encoding="utf-8") as h:
    line = h.read()
with open ("_rbk7.xhtml", "r", encoding="utf-8") as j:
    line = j.read()
with open ("_rian1.xhtml", "r", encoding="utf-8") as k:
    line = k.read()
with open ("_rian2.xhtml", "r", encoding="utf-8") as l:
    line = l.read()
with open ("_rian3.xhtml", "r", encoding="utf-8") as z:
    line = z.read()
with open ("_rian5.xhtml", "r", encoding="utf-8") as x:
    line = x.read()
with open ("_itartass1.xhtml", "r", encoding="utf-8") as c:
    line = c.read()
with open ("_itartass2.xhtml", "r", encoding="utf-8") as v:
    line = v.read()
with open ("_itartass3.xhtml", "r", encoding="utf-8") as b:
    line = b.read()
with open ("_itartass4.xhtml", "r", encoding="utf-8") as m:
    line = m.read()
with open ("_itartass5.xhtml", "r", encoding="utf-8") as t:
    line = t.read()
with open ("_rbk6.xhtml", "r", encoding="utf-8") as u:
    line = u.read()
    itog =''

# def get_word(filename):
#   word=""
#    with open (""+filename, "r", encoding="utf-8") as f:
#        return(word)
# а вообще так будет проще,но я вспомнила об этом слишком поздно


    def search(slovo, text):
        return len(re.search(teg, file))
    result = search('"S,', line)
    result1 = search('gen"', result.group(0))
    itog = result.group(0)
    print(itog)

with open ('news/_itartass1.html', 'w', encoding='utf-8') as o:
    o.write(itog)
    o.close()

    def search(slovo, text):
        return len(re.search(teg, line))
    abbr = search('"/>[А-Я][А-Я]', line)

    def count_slovo(teg, file):
        return len(re.findall(teg, line)
    
with open ('news/_itartass1.html', 'w', encoding='utf-8') as n:
    n.write(abbr+    +str(search('lex="[A-Z][A-Z]', line)))
    n.close()


FILENAME = "users.csv"

 
users = [
    ["doc_id", _rbk2.xhtml, _rbk3.xhtml, _rbk4.xhtml, _rbk6.xhtml, _rbk7.xhtml, _rian1.xhtml, _rian2.xhtml, _rian3.xhtml, _rian5.xhtml, _itartass1.html, _itartass2.html, _itartass3.html, _itartass4.html, _itartass5.html],
    ["title", -],
    ["author", rbk, rbk, rbk, rbk, rbk, rian, rian, rian, rian, itartass, itartass, itartass, itartass, itartass]
    ["created", yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday, yesterday],
    ["topic", news, news, news, news, news, news, news, news, news, news, news, news, news, news],
    ["tagging", -]
]
 
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
     
 
with open(FILENAME, "a", newline="") as file:
    user = ["doc_id", _rbk2.xhtml, _rbk3.xhtml, _rbk4.xhtml, _rbk6.xhtml, _rbk7.xhtml, _rian1.xhtml, _rian2.xhtml, _rian3.xhtml, _rian5.xhtml, _itartass1.html, _itartass2.html, _itartass3.html, _itartass4.html, _itartass5.html]
    writer = csv.writer(file)
    writer.writerow(user)
    
