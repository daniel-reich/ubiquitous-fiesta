
def has_factors(n):
    if abs(n) < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return True
    return False
​
def prime_factorize(n):
    if n < 2:
        return []
    factors = []
    if not has_factors(n):
        factors.append(n)
    while has_factors(n):
        for i in range(2, n):
            if n % i == 0:
                if not has_factors(i):
                    factors.append(i)
                    n = n // i
        if n != 1 and not has_factors(n):
            factors.append(n)
    factors.sort()
    return factors

