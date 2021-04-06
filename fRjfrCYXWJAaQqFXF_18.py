
from operator import mul
from functools import reduce
​
is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
def first_n_primes(n):
    '''
    Returns each of the first n prime numbers one at a time
    '''
    p = 2
    for _ in range(n):
        yield p
        p += 1
        while not is_prime(p):
            p += 1
​
PRIMES = list(first_n_primes(10))
​
primorial = lambda n: reduce(mul,PRIMES[:n])

