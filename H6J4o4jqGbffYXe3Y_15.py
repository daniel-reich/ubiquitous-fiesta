
def relation_lst(lst):
    l=[]
    for i in lst:
        for j in lst:
            if i<=j:
                l.append((i,j))
    return sorted(set(l))

