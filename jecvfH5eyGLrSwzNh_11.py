
def fauna_number(txt):
    splited = txt.split(" ")
    splited = sum([j.split('.') for j in sum([i.split(',') for i in splited], [])], [])
​
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
    result  = []
​
    for word in range(len(splited)):
        if splited[word] in animals:
            if splited[word-1].isnumeric():
                result.append((splited[word], splited[word-1]))
​
            else: result.append((splited[word], splited[word+1]))
        
            
​
    return result

