
import operator
from functools import reduce
​
def primorial(n):
  primes = generate_primes()
  return reduce(operator.mul, (next(primes) for _ in range(n)))
  
def generate_primes():
    D = {}
    q = 2
    
    while q:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

