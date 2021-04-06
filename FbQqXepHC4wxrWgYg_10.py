
from math import sqrt
def prime_divisors(num):
  for i in range(2,int(sqrt(num)) + 1):
    if num % i == 0:
      return sorted(list(set([i] + prime_divisors(num // i))))
  return [num]

