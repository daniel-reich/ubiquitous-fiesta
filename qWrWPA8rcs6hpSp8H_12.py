
def determinant_s(L,s,G,f):
    f+=1
    try:
        if len(L) == 2:
            return (L[0][0] * L[1][1] - L[1][0] * L[0][1])
        else:
            for i in range(0, len(L), 1):
                L = []
                for o in G:
                    L.append(o[:])
                a = L[i][0]
                L.pop(i)
                for p in range(0, len(L), 1):
                    L[p].pop(0)
                s += ((-1) ** i) * a * determinant_s(L, s, G, f)
    except RuntimeError:
        import sys
        sys.setrecursionlimit(2*f)
        pass
    return(s)
​
​
​
def determinant(L):
    G = []
    s = 0
    f=0
    if len(L) == 1:
        return (L[0][0])
    else:
        for i in L:
            G.append(i[:])
        return (determinant_s(L, s, G, f))

