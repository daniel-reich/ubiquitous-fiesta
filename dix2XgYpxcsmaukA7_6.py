
from collections import Counter
​
def express_factors(num):
  factors = factorization(num)
  print (factors)
  cnt = Counter(factors)
  pairs = sorted([[k,v] for k,v in cnt.items()], key= lambda x: x[0])
  print(pairs)
  res = []
  for pair in pairs:
    k,v = pair
    if v > 1:
      res.append(str(k) + "^" + str(v))
    else:
      res.append(str(k))
  return " x ".join(res)
​
def primes (num):
    primes = [2]
    number = 3
    while number <= num :
        if not any([number % p == 0 for p in primes]):
            primes.append(number)
        number += 2
    return primes
​
def factorization(num):
    prim = primes(num)
    factors = []
    for p in prim:
        while num % p == 0:
            factors.append(p)
            num = num // p
    return factors

