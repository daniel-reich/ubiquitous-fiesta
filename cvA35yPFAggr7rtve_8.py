
def last_ancestor(folders,X,Y):
    lst = sorted([[k,v] for k,v in folders.items()],key=lambda x:x[1])
    for k,v in lst[::-1]:
        if (X in v and Y in v) or (X == k and Y in v) or (X in v and Y == k) or (X == Y == k): return k
        if X in v: return last_ancestor(folders,k,Y)
        if Y in v: return last_ancestor(folders,X,k)

