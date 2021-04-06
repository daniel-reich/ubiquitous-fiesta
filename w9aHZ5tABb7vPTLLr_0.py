
def weak_compositions(maxi, dig):
    n = maxi * dig + 1; zeros = [0 for _ in range(n)]
    pas = [zeros[:] for _ in range(dig)]
    for i in range(maxi+1): pas[0][i] = 1
    for j in range(1, dig):
        for p in range(n):
            for back in range(p, p-maxi-1, -1):
                if back >= 0: pas[j][p] += pas[j-1][back]
    return pas[-1]
​
def lucky_ticket(dig):
    lst = weak_compositions(9, dig//2); cp, s = len(lst), 0
    for i in range(cp//2): s+= 2*lst[i]**2
    if cp%2 == 1: s += lst[cp//2]**2
    return s

