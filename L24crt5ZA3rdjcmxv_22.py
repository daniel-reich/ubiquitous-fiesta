
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
vowels="aeiou"
def get_vowels(x):
    return [n for n in x if n in vowels]
def get_consonants(x):
    return [n for n in x if n not in vowels]
def fiscal_code(person):
    code=""
    name=person["surname"].lower()
    v=get_vowels(name)
    c=get_consonants(name)
    if len(c)>=3:
        code+="".join(c[:3])
    elif len(name)>2:
        code+="".join(c)+"".join(v[:3-len(c)])
    else:
        code+="".join(c)+"".join(v)+"X"
    name=person["name"].lower()
    v=get_vowels(name)
    c=get_consonants(name)    
    if len(c)==3:
        code+="".join(c)
    elif len(c)>3:
        code+=c[0]+c[2]+c[3]
    elif len(name)>2:
        code+="".join(c)+"".join(v[:3-len(c)])
    else:
        code+="".join(c)+"".join(v)+"X"
    
    dob=person["dob"]
    code+=dob[-2:]
    dobs=dob.split("/")
    code+=months[dobs[1]]
    if person["gender"]=="M":
        if len(dobs[0])==1:
            code+="0"+dobs[0] 
        else: code+=dobs[0]
    else: 
        code+=str(int(dobs[0])+40)
    
    
    return code.upper()

