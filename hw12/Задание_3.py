import re
with open("Corpus.xml","r", encoding="utf-8") as f:
    text = f.read()
    
    result = ""
    word = re.search('type="f.l', text)
    word2 = re.search('>[A-Z][a-z]<', word.group(0))
    result = word2.group(0)



with open("text1.txt","w", encoding="utf-8") as o:
    o.write(result)
    
