
def encryption(txt):
    txt = txt.replace(' ', '')
    a = int(len(txt)**0.5) + 1
    if a ** 2 != len(txt):
        txt += (' ' * (a ** 2 - len(txt)))
    b = [txt[x:x+a] for x in range(0,len(txt),a)]
    return ' '.join([''.join(x).strip() for x in zip(*b)])

