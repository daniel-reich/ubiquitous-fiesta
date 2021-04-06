
def max_separator(txt):
    lst = []
    for i, x in enumerate(txt):
        idx = txt[i+1:].find(x)
        if idx >= 0:
            lst.append((idx,x))
    if not lst:
        return lst
    x, y = max(lst)
    return sorted([b for a,b in lst if a == x])

