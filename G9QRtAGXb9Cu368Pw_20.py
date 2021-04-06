
def combinations(items,*args):
    lst=[items]
    for arg in args:
        lst.append(arg)
    l=len(lst)
    arr=None
    for i in range(l):
        if lst[i]!=0:
            if arr==None:arr=lst[i]
            else:arr*=lst[i]
    return arr

