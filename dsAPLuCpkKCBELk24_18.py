
def get_products(l):
    p = 1
    r = [] 
    for i in range(0,len(l)): 
        for n in l: 
            if n != l[i]:
                p *= n 
        r.append(p) 
        p = 1 
    return r

