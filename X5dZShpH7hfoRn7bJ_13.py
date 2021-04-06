
from itertools import combinations_with_replacement
def c_fuge(n, k):
  if n == 1 or k == 1: return False
  pn = prime_divisors(n)
  cs = [sum(comb) for i in range(n) for comb in combinations_with_replacement(pn, i) ]
  return k in cs and n-k in cs
​
def prime_divisors(n):
  ret = []
  while n % 2 == 0:
    ret.append(2)
    n = n//2
  
  for i in range(3, n//2, 2):
    if n % i == 0:
      ret.append(i)
      n = n//i
  if n > 2:
    ret.append(n)
​
  return ret

