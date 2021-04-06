
import math
def is_prime(num):
  if num == 1:
    return False
  for n in range(2, int(math.sqrt(num))+1):
    if num % n == 0:
      return False
    else:
      continue
  return True
​
def filter_primes(num):
  return [n for n in num if is_prime(n)]

