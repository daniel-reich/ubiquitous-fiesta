
def flatten(r):
    lists = False
    e = type([])
    x = []
    for i in r:
        if type(i) == e:
            for z in i:
                x.append(z)
                lists = True
        else: x.append(i)
    if lists: return flatten(x)
    else: return x

