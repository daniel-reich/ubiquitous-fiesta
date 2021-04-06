
def alternating_caps(txt):
    string = ""
    s = True
    for i in txt:
        string += i.upper() if s else i.lower()
        if i.isalpha():
            s = not s
    return string

