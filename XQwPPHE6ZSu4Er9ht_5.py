
from math import sqrt
def factors(n):
    pfs = []
    while n%2 == 0:
        pfs.append(2)
        n //= 2
    lim = int(sqrt(n)) + 1
    for i in range(3, lim, 2):
        while n%i == 0:
            pfs.append(i)
            n //= i
    return pfs + [n] if n > 2 else pfs
​
​
def is_economical(n):
    numlen = lambda n: len(str(n))
    pfs = factors(n)
    eco = 0
    for d in set(pfs):
        exp = pfs.count(d)
        eco += numlen(d) + (numlen(exp) if exp > 1 else 0)
    return 'Frugal' if eco < numlen(n) else 'Equidigital' if eco == numlen(n) else 'Wasteful'

