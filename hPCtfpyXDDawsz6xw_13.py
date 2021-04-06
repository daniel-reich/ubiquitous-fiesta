
def verbify(txt):
    txt = txt.split()
    if txt[0].endswith("e"):
        txt[0] = txt[0] + "d"
    elif not txt[0].endswith("ed"):
        txt[0] = txt[0] + "ed"
    return " ".join(txt)

