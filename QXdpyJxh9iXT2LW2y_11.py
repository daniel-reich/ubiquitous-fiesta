
def sieve_eratos(limit):
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False
​
    for i in range(2, int(limit**0.5) + 1):
        p = i * 2
        while p < limit:
            sieve[p] = False
            p += i
    return [i for i in range(limit) if sieve[i]]
​
def semiprimes(n):
    if n < 2:
        return ([], [])
    primes = sieve_eratos(n)
    primes_semi = sorted([i*j for i in primes for j in primes if i*j <= n and i <= j])
    primes_squareless = [i for i in primes_semi if i**0.5 != int(i**0.5)]
    return (primes_semi, primes_squareless)

