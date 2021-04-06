
from functools import reduce
def gen_primes(n):
    primes, k = {2}, 3
    while len(primes) < n:
        if all(k % p > 0 for p in primes):
            primes.add(k)
        k += 2
    return sorted(primes)
​
lst_primes = gen_primes(10)
​
def primorial(n):
    return reduce(lambda a, b: a * b, lst_primes[:n])

