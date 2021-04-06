
from itertools import combinations_with_replacement
​
def primes(n):
  primes = [2]
  for c in range(3, n+1):
    if all(c % p != 0 for p in primes):
      primes.append(c)
  return primes
  
def semiprimes(n):
  sp, ns = [], []
  pList = primes(n//2)
  for u, v in combinations_with_replacement(pList, 2):
    val = u * v
    if val < n:
      sp.append(val)
      if u != v:
        ns.append(val)
  return sorted(sp), sorted(ns)

