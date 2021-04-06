
import math
def sum_primes(series):
  if not series:
    return None
  primes = primes_upto(max(series))
  return sum(element for element in series if element in primes)
​
def primes_upto(n):
  if n <= 1:
    return list() 
  return [number for number in range(2, n+1) if is_prime(number)]
​
​
def is_prime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
​
  for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True

