
def complete_factorization(n):
    pfs = []
    while n%2 == 0:
        pfs.append(2)
        n /= 2
    lim = int(n**0.5) + 1
    for i in range(3, lim, 2):
        while n%i == 0:
            pfs.append(i)
            n /= i
    return pfs + [int(n)] if n > 2 else pfs

