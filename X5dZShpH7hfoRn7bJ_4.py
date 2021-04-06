
def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return list(set(res))
​
​
def c_fuge(n, k):
    if n == 1 or k == 1:
        return False
    elif n == k:
        return True
    n_factors = prime_factors(n)
    if len(n_factors) > 1:
        n_factors.append(n_factors[0] + n_factors[1])
        n_factors.append(n_factors[0] + n_factors[2])
    k_factors = prime_factors(k)
    nk_factors = prime_factors(n - k)
    return (any(f in k_factors for f in n_factors)
            and any(f in nk_factors for f in n_factors))

