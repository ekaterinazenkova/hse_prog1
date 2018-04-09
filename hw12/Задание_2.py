
with open("/Users/ekaterinazenkova/Desktop/Corpus.xml","r", encoding="utf-8") as f:
    line = f.readline()
    a = 0
    poisk = "<w lemma="
    while line:
        if poisk in line:
            a += 1
            line = f.readline()

    listok = {line: a}  
    empty_dict = {}  
    empty_dict2 = dict()  


with open("/Users/ekaterinazenkova/Desktop/text1.txt","w", encoding="utf-8") as o:
    o.write(empty_dict2)
    


 
