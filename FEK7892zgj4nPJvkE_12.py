
from math import sqrt
def prime_gaps(gap, start, end):
    primes = []
    if (start + gap) > end:
        return None
    for i in range(start, end+1):
        if is_prime(i):
            primes.append(i)
    for i in range(1,len(primes)):
        if primes[i] - primes[i-1] == gap:
            return [primes[i-1], primes[i]]
    return None
​
def is_prime(n):
    if n < 2:
        return False
    end = int(sqrt(n)) + 1
    for i in range(2, end):
        if n % i == 0:
            return False
    return True

