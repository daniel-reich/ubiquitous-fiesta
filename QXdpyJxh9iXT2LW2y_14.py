
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
    return res
​
​
def semiprimes(n):
    if n < 4:
        return [], []
    all_semi_primes = []
    not_square = []
    for k in range(4, n):
        factors = prime_factors(k)
        if len(factors) == 2:
            all_semi_primes.append(k)
            if len(set(factors)) == 2:
                not_square.append(k)
    return all_semi_primes, not_square

