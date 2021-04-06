
from math import floor
​
def is_prime(primes, num, left=0, right=None):
    n = len(primes)
    L = 0
    R = n-1
    while L <= R:
      mid = floor((L+R)/2)
      if primes[mid] < num:
        L = mid + 1
      elif primes[mid] > num:
        R = mid - 1
      else:
        return 'yes'
    return 'no'

