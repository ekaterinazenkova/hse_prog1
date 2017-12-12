with open("control_languages.txt", 'r', encoding="utf-8") as f:
    print("Задание1")
    line = f.readline()
    while line:
        if len(line) > 35:
            print(line)
        line=f.readline()
    
