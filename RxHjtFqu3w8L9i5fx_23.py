
def bell(n):
    lp, lc = [1], [0]*n
    for i in range(1, n):
        lc[0] = lp[i-1]
        for j in range(1, i+1):
            lc[j] = lp[j-1] + lc[j-1]
        lp = [Z for Z in lc if Z != 0]
    return lc[-1] if n>1 else 1

