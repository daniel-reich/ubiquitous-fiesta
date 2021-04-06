
def sieve_eratos(start, num):
    if num < 2:
        return 0
    
    sieve = [True] * (num + 1)
    sieve[0], sieve[1] = False, False
    
    for i in range(2, int(num**0.5) + 1):
        p = i * 2
        while p < num:
            sieve[p] = False
            p += i
    return [i for i in range(start, num + 1) if sieve[i]]
​
def prime_gaps(g, a, b):
    primes = sieve_eratos(a, b)
    for i in range(1, len(primes)):
        if primes[i] - primes[i-1] == g:
            return [primes[i-1], primes[i]]

