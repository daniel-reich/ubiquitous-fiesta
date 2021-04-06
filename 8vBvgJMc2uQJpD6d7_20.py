
def factorization(x):
    for i in range (2, int(x) + 1, 1):
        if x % i == 0:
            return i
    return 1
​
def prime_factors(x):
    factors = []
    factor = factorization(x)
    while factor != 1:
        factors.append(factor)
        x = x / factor
        factor = factorization(x)
    return factors

