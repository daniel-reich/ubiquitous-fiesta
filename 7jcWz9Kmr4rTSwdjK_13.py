
from math import sqrt; from itertools import count, islice; import numpy
​
def check_prime(lst):
  return [n for n in lst if all(n % i for i in islice(count(2), int(sqrt(n)-1)))]
​
def prime_factorize(num):
  factors = [i for i in range(2, num+1) if num % i == 0]
  prime_factors = check_prime(factors)
  while num//numpy.prod(prime_factors) != 1:
    prime_factors.append(prime_factors[0])
  return sorted(prime_factors)

