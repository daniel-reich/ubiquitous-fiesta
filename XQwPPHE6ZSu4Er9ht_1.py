
def prime_factors(n):
    i, factors = 2, []
    
    while i**2 <= n:
        if n%i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
​
def is_economical(n):
    factors = prime_factors(n)
    groups = []
    num_size = len(str(n))
    
    for f in set(factors):
        if factors.count(f) > 1:
            groups += [f, factors.count(f)]
        else:
            groups.append(f)
    size = len(''.join(str(i) for i in groups))
​
    if size < num_size:
        return 'Frugal'
    if size > num_size:
        return 'Wasteful'
    return 'Equidigital'

