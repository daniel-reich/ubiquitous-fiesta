
def rep_set(n):
    d = {}
    d[0] = []
    for x in range(1, n+1):
        d[x] = [d[i] for i in range(x)]
    return d[n]

