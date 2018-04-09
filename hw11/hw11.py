
import re
o = open('/Users/ekaterinazenkova/Desktop/text.txt','w', encoding='utf-8')
data = open('/Users/ekaterinazenkova/Desktop/Комар.htm', encoding='utf-8').read()


def switch(Word1,Word2,text2change):
    return re.sub(Word1, Word2, text2change)
     

newdata = switch('Комар', 'Слон', data)
newdata2 = switch('комар', 'слон', newdata)

o.write(newdata2)
o.close()
