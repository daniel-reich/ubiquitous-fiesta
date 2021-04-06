
def reversible_inclusive_list(s, e, desc=None, arr=None):
    if desc==None:
        desc = s>e
        s,e = sorted([s,e])
        return reversible_inclusive_list(s, e, desc, [s])
    if len(arr) ==  e-s+1:
        return sorted(arr, reverse=desc)
    return reversible_inclusive_list(s, e, desc, arr + [arr[-1]+1])

