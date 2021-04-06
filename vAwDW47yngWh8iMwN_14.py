
def capLast(txt):
    txt = list(txt.split(' '))
    for i in range(len(txt)):
        txt[i] = txt[i][:-1]+txt[i][-1].upper()
    txt = ' '.join(txt)
    return txt

