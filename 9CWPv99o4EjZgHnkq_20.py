
def divide(lst, n):
    r, add = [], []
    i = 0
    for x in lst:
        if i + x <= n:
            add.append(x)
            i += x
        else:
            r.append(add)
            add = []
            add.append(x)
            i = x
    r.append(add)
    return r

