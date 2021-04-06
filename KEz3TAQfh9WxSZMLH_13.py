
def count_all(string):
    
    alphacount = 0
    digicount = 0
    
    for char in string:
        if char.isdigit():
            digicount += 1
        elif char != " ":
            alphacount += 1            
    
    return {"LETTERS": alphacount, "DIGITS": digicount}

