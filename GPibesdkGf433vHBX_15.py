
from math import sqrt
​
def goldbach_conjecture(n):
    primes = []
​
    if (n > 2) and (n % 2 == 0):
        for p in range(2, n):
            if is_prime(p):
                primes.append(p)
    
    for a in primes:
        for b in range(len(primes)-1,-1,-1):
            if (n == (a + primes[b])):
                return [a,primes[b]]
​
    return []
​
def is_prime(n):
    end = int(sqrt(n)) + 1
​
    for i in range(2, end):
        if n % i == 0:
            return False
​
    return True

