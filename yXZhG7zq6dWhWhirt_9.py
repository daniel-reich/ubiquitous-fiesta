
from functools import reduce
​
def filter_primes(num):
  return list(filter(isPrime, num))
​
​
def isPrime(n):
  return len(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) == 2

