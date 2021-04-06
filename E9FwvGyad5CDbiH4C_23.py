
def block(lst):
    x=[]
    for i in lst:
        for j in i:
            if j==2:
                if lst.index(i)!=len(lst)-1:
                    x.append((lst.index(i)))
    return sum([abs(i-len(lst))-1 for i in x])

