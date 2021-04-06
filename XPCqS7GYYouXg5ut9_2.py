
from collections import Counter
​
def prime_factors(num):
    p = 2
    lst = []
    while num >= p*p:
        if num % p == 0:
            lst.append(p)
            num /= p
        else:
            p += 1
    lst.append(num)
    return lst
​
def product(lst):
    prod = 1
    for x in lst:
        prod *= x
    return prod
​
def simplify_sqrt(n):
    c = Counter(prime_factors(n))
    outer = []
    inner = []
    for k, v in c.items():
        o = k ** (v // 2)
        outer.append(o if o else 1)
        i = k * (v % 2)
        inner.append(i if i else 1)
    return product(outer), product(inner)

