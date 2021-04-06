
# The Centrifuge Problem
import itertools
import math
def prime(num):
    if num == 2:
        return True
    max_trial = math.ceil(num ** (1/2))
    for number in range(2, max_trial + 1):
        if num % number == 0:
            return False
    return True
def prime_factors(num):
    prime_numbers = []
    for i in range(2, num + 1):
        if num % i == 0 and prime(i):
            prime_numbers.append(i)
    return prime_numbers
​
def c_fuge(holes, tubes):
    primes = prime_factors(holes)
    
    possibilities = set()
    for level in range(0, holes + 1):
        primes = prime_factors(holes) * level
        for items in [sum(item) for item in list(itertools.combinations(primes, level)) if sum(item) <= holes]:
            possibilities.add(items)
    return tubes in possibilities and (holes - tubes) in possibilities

