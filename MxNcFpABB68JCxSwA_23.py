
def legendre(p, n):
    if p > n:
        return 0
    sol = 0
    e = 1
    while n >= p ** e:
        sol = sol + n // p ** e
        e += 1
    return sol

