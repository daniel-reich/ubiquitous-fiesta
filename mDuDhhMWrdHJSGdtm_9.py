
from functools import reduce
​
def divisible(n):
  factors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
  return len(factors) == 3

