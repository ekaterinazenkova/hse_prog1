#with open("/Users/ekaterinazenkova/Desktop/control_languages.txt", 'r', encoding="utf-8") as f: (этот путь был на моём компьютере)
with open("control_languages.txt", 'r', encoding="utf-8") as f:
    print("Задание2")
    line = f.readline()
    status = "Critically endangered"
    count = 0
    while line:
        line = line.split(" ")
        word = line[2]
        if status in word:
            count = count + 1
        line = f.resdline()
    print("В списке", count,"языков сo статусом Critically endangered.")
        
