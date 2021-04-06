
def num_split(num):
    l = list(str(abs(num)))
    for i,v in enumerate(l):
        if num>0:l[i]=eval(str(v) + "0"*(len(l)-i-1))
        else: l[i]=eval(str(v) + "0"*(len(l)-i-1))*(-1)
    return l

