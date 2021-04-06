
def special_reverse_string(txt):
    r = ""
    key = txt
    txt = iter([x.lower() for x in txt[::-1] if x != " "])
    for y in key:
        if y == " ":
            r += " " 
        elif y.isupper():
            r += next(txt).upper()
        elif y.islower():
            r += next(txt).lower()
        else:
            r += next(txt)
    return r

