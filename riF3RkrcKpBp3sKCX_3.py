
def cap_space(txt):
    b=""
    for i in txt:
        if i.isupper():
            b=b+" "+i.lower()
        else:
            b=b+i
    return b

