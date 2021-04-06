
def super_reduced_string(txt):
    if not txt:
        return "Empty String"
    for i in range(0,len(txt)):
        if i < len(txt)-1:
            if txt[i] == txt[i+1]:
                return super_reduced_string(txt[:i]+txt[i+2:])
    return txt

