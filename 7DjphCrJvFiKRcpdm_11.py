
def covered_integers(lst):
    m=[]
    [m.extend([i for i in range(x[0],x[1]+1)]) for x in lst]
    return len(set(m))

