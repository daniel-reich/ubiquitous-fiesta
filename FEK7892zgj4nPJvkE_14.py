
from math import sqrt
​
def prime_sieve(a, n):
  nums = {i: True for i in range(2, n)}
  for i in range(2, int(sqrt(n)) + 1):
    if nums[i]:
      for j in range(i * i, n, i):
        nums[j] = False
  return [num for num in nums if nums[num] and num >= a]
​
def prime_gaps(g, a, b):
  primes = prime_sieve(a, b + 1)
  for i in range(len(primes) - 1):
    a, b = primes[i], primes[i + 1]
    if b - a == g: return [a, b]
  return None

