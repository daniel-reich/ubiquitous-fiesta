
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
from itertools import combinations_with_replacement
​
def check_sum(n, lst):
    c = 1
    while min(lst) * c <= n:
        if any([sum(x)==n for x in combinations_with_replacement(lst, c)]):
            return True
        c += 1
    return False    
    
def c_fuge(n, k):
  if n == 1 or k == 1:
    return False
  if n == k:
    return True
  nf = set(prime_factors(n))
  return check_sum(k,nf) and check_sum(n-k,nf)

