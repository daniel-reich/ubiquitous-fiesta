
from math import sqrt, ceil
from fractions import gcd
​
def is_prime(n):
  if n < 2: return False
  if n < 4: return True
  if n%2 == 0 or n%3 == 0: return False
  return all(n % i > 0 for i in range(3, ceil(sqrt(n)) + 1, 2))
​
def sim_prop_frac(max_den):
  count_distinct = 0
  for den in range(2, max_den + 1):
    if is_prime(den):
      count_distinct += den - 1
    else:
      for n in range(1, den):
        if gcd(n, den) == 1:
          count_distinct += 1
  return count_distinct

