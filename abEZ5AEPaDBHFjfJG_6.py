
def calc(txt):
    if txt == 'a':
        return 4
    
    try:
        return int(txt)
    
    except ValueError:
        tokens = txt.split("*")
        if len(tokens) > 1:
            mult = 1
            for elem in tokens:
                mult *= calc(elem)
            return mult
        
        tokens = txt.split("/")
        if len(tokens) > 1:
            return calc(tokens[0]) / calc(tokens[1])
        
        tokens = txt.split("+")
        if len(tokens) > 1:
            add = 0
            for elem in tokens:
                add += calc(elem)
            return add
        
        tokens = txt.split("-")
        if len(tokens) > 1:
            return calc(tokens[0]) - calc(tokens[1])
        
        return 0
​
def formula(txt):
    if txt == "":
        return None
​
    newTxt = ""
    for elem in txt:
        if elem.isdigit() or (elem in ("a*/+-=")):
            newTxt += elem
    newTxt = newTxt.split("=")
​
    i = 0
    while (i + 1) < len(newTxt):
        if calc(newTxt[i]) != calc(newTxt[i + 1]):
            return False
        i += 1
    
    return True

