
def complete_factorization(num):
    p = 2
    primes = []
    while num > 1:
        if num % p == 0:
            primes.append(p)
            num = num // p
        else:
            p += 1
    return primes

