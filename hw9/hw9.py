
import re
with open("Глагол.txt", "r", encoding="utf-8") as f:
    text =""
    line = f.readline()
    while line:
        line = line.strip() 
        text += line 
        line = f.readline()   
    text = text.lower()
 
 
    
    for word in text:
        slovo  = re.findall(r'открыва.?.?', text)
        slovo1 = re.findall(r'откры[л][оаи]', text)
        slovo2 = re.findall(r'откры[в][ш][аеи][йея]', text)
        slovo3 = re.findall(r'откро[юешьетемете]', text)
        slovo4 = re.findall(r'открыть', text) 
        
 

    
    print (slovo)
    print (slovo1)
    print (slovo2)
    print (slovo3)
    print (slovo4)
  
    
           
