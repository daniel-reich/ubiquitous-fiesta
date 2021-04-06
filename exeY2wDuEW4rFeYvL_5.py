
def ordered_matrix(a, b):
    r=[]
    i=1
    for c in range(a):
        r.append(list(range(i,i+b)))
        i=i+b
    return r

