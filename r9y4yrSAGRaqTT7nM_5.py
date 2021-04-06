
def find_missing(x):
    w=[]
    if(x==[] or x==[[]] or x==None):
        return False
    else:
        for i in x:
            w.append(len(i))
        w.sort()
        if(0 in w): return False
        for i in range(w[0], w[len(w)-1]):
            if (i)!=w[i-w[0]]:
                return i

