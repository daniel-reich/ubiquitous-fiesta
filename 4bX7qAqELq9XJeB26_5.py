
def to_camel_case(txt):
    txt = [i for i in txt]
    for i in range(len(txt)):
        if txt[i-1] == "-" or txt[i-1] == "_":
            txt[i] = txt[i].upper()
    txt = "".join(txt)
    if "_" in txt:
        txt = txt.replace("_","")
    if "-" in txt:
        txt = txt.replace("-","")
    return txt

