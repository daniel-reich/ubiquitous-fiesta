
def make_sandwich(i, f):
    a=[]
    for k,j in enumerate(i):
        if k+1 in range(len(i)):
            if i[k]==f and i[k+1]==f:
                a=list(i[:k])+['bread']+[i[k]]+['bread']+['bread']+[i[k+1]]+['bread']+list(i[k+2:])
            elif j==f:
                a=list(i[:k])+['bread']+[i[k]]+['bread']+list(i[k+1:])
        else:
            break
    return a

