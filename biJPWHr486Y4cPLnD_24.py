
def chunkify(lst,size):
    j = 0
    b = []
    if len(lst) < size:
        return [lst]
    while j < len(lst) - (len(lst)%size):
        a = []
        
        for i in range(size):
            a.append(lst[i+j])
        j += size 
        b.append(a)
    if len(lst)%size == 0:
        return b 
    else:
        c = []
        for i in range(len(lst)%size):
            c.append(lst[-(i+1)])
        b.append(c)
        return b

