
def is_isomorphic(s, t):
    d1={}
    d2={}
    for i,v in enumerate(s):
        if v in d1:
            if t[i] != d1[v]:
                return False
        else:
            d1[v] = t[i]
        if t[i] in d2:
            if v!= d2[t[i]]:
                return False
        else:
            d2[t[i]] = v    
    return True

