
# function that takes two numbers as argument, the set length n (2 for
# pairs, 3 for triplets), and the limit. Return a list of sorted tuples of
# sexy primes up to (but excluding) the limit.
def sexy_primes(n, limit):
    primes, result = [], []
    def isPrime(a):
        return all(a % i for i in range(2, a)) if a not in [0,1] else False
    for i in range(limit):
        if isPrime(i): primes.append(i)
    if n == 2:
        for p in primes:
            if p + 6 in primes:
                result.append((p,p+6))
    if n == 3:
        for p in primes:
            if p + 6 in primes and p + 12 in primes:
                result.append((p, p+6, p+12))
​
    return result

