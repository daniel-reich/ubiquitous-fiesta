
def get_subsets(lst, n):
    x = len(lst)
    y=[];a=[]
    for i in range(1,2**x,1):
        p=sorted([lst[j] for j in range(x) if (i & (2**j))])
        if sum(p)==n:
            if len(p)>1:
                y.append(p)
            else:
                a=p
    y.sort(key=lambda y:(len(y),y[0],y[1]))
    if a!=[]:
        return [a]+y
    return y

