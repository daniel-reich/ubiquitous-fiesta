
def mystery_func(txt):
    retstr = ""
    while txt != '':
        num = ""
        i = 1
        np = 1
        bu = txt[0]
        while i < len(txt) and ord(txt[i]) >= 48 and ord(txt[i]) < 58:
            num += txt[i]
            i += 1
            np += 1
        num = int(num)
        for x in range(num):
            retstr += bu
        txt = txt[np::]
    return retstr

