
def truncate(txt, length):
    strn = ''
    c = 0
    for i in range(length):
        try:
            strn += txt[c]
            c += 1
        except IndexError:
            return txt
    if txt[c].isalpha():
        for l in strn[::-1]:
            if l == ' ':
                strn = strn[:-1]
                break
            elif l.isalpha():
                strn = strn[:-1]
    return strn

