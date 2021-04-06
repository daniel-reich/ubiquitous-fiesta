
def make_sandwich(l, f):
    res=[]
    for i in l:
        if i == f:
            res.append('bread')
            res.append(i)
            res.append('bread')
        else:res.append(i)
    return res

