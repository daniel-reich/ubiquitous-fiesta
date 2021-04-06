
def factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
​
def is_economical(n):
    from collections import Counter
    fact = ''.join([str(x)+str(y) if y>1 else str(x) for x,y in Counter(factorization(n)).items()])
    if len(fact) == len(str(n)): return "Equidigital"
    elif len(fact) < len(str(n)): return "Frugal"
    else: return "Wasteful"

