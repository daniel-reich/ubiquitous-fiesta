
def numbers_to_ranges(lst):
    o=[]
    p=[]
    if len (lst)==1:
        return list(str(lst[0]))
    if len (lst)==0:
        return []
    if sorted(lst) == list(range(min(lst), max(lst)+1)):
        u=("{}-{}".format(lst[0],lst[-1]))
        p.append(u)
        return p
        
    for i in range(0,len(lst)-1):
        o.append(lst[i])
        if lst[i]!=lst[i+1]-1:
            break
    r=o,lst[len(o):]
    if len(o)==1:
        u=str(lst[0])
        l=("{}-{}".format(r[1][0],r[1][-1]))
        p.append(u)
        p.append(l)
        return p
    else:
        
        u=("{}-{}".format(r[0][0],r[0][-1]))
        l=("{}-{}".format(r[1][0],r[1][-1]))
        p.append(u)
        p.append(l)
        return p

