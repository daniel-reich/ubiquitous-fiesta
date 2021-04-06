
def golomb_s(n):
    L = [1, 2,2]
    for i in range(3, n + 1, 1):
        while L.count(i) != L[i - 1] and len(L)<=n:
            L.append(i)
    return L
    
def golomb(n):
    return(golomb_s(n)[:n])

