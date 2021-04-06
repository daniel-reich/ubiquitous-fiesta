
def combinations(k, n):
    nfact, kfact, diffact = 1, 1, 1
    for i in range(1, n+1):
        nfact *= i
    for i in range(1, k+1):
        kfact *= i
    for i in range(1, (n-k)+1):
        diffact *= i
    return int(nfact/(kfact*diffact))

