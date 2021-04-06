
def classify_rug(l):
    print(l)
    rows = len(l)
    cols = len(l[0])
    if cols ==1 and rows==1:
        return "perfect"
    c = [list(x) for x in zip(*l)]
    ver, hor = True, True
    for i in range(int(rows // 2)):
        if l[0 + i] != l[-1 - i]:
            hor = False
            break
    print()
    for i in range(int(cols // 2)):
        if c[0 + i] != c[-1 - i]:
            ver = False
            break
    if ver and hor:
        out = "perfect"
    elif not ver and not hor:
        out = "imperfect"
    elif ver and not hor:
        out = "vertically symmetric"
    elif hor and not ver:
        out = "horizontally symmetric"
    return out

