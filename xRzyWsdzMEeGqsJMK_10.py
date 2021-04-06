
def maskify(txt):
    mystr = ""
    txt = txt[::-1]
    for i in range (len(txt)):
        if (i<4):
            mystr = mystr + txt[i]
        else:
            mystr = mystr + '#'
    return mystr[::-1]

