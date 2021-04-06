
from gmpy2 import next_prime
def primorial(n):
    p = prev = 1
    for _ in range(n):
        prev = next_prime(prev)
        p *= prev
    return p

