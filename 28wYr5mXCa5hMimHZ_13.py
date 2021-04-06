
def valid_name(name):
    if name.count(" ") not in range(1, 3, 1):
        return False
    
    word_count = name.count(" ") + 1
    parts = []
    temp = []
    
    for x in range(len(name)):
        if name[x] == " ":
            parts.append(temp)
            temp = []
            continue
        temp.append(name[x])
    parts.append(temp)   
​
    if name.count(".") == 2:
        if word_count != 3:
            return False
        if parts[0][1] != "." or parts[1][1] != ".":
            return False
        
    if name.count(".") == 1:
        if word_count == 2:
            if not parts[0][1] == ".":
                return False
        else:    
            if not parts[1][1] == ".":
                return False
    
    if name.count(".") == 0:
        for x in range(word_count):
            if len(parts[x]) <2:
                return False
        
    for x in range(word_count):
        if not parts[x][0].isupper():
            return False
    
    return True

