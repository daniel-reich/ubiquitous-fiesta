
def unravel(txt):
    idx1 = txt.find('[')
    if idx1  < 0:
        return [txt]
    L = [txt[:idx1]]
    while len(txt) > 0:
        idx1 = txt.find('[')
        if idx1 < 0:
            L2 = [el + txt for el in L]
            break
        idx2 = txt.find(']')
        possibilities = txt[idx1+1:idx2].split('|')
        txt = txt[idx2+1:]
        L2 = []
        for el in L:
            for poss in possibilities:
                L2.append(el + poss)
        L = L2[:]
        if len(txt) == 0:
            break
        idx1 = txt.find('[')
        if idx1 < 0:
            L2 = [el + txt for el in L]
            break
        elif idx1 > 0:
            chunk = txt[:idx1]
            L2 = [el + chunk for el in L]
            txt = txt[idx1:]
        L = L2[:]
    return sorted(L2)

