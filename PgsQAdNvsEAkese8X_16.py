
def to_list(dct):
    t=dct.items()
    l=[]
    for i,j in t:
        a=[i,j]
        l.append(a)
    return sorted(l)

