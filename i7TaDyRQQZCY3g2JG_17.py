
from collections import Counter
​
​
def primes(n):
  factors = Counter()
  i = 2
  while i <= n:
    if not n % i:
      n /= i
      factors[i] += 1
    else:
      i += 1
  return factors
  
​
def lcm(nums):
  c = Counter()
  for i in nums:
    c.__ior__(primes(i))
  i = 1   # annoying that python doesnt have prod(items) until 3.8
  for x in c.elements():
    i *= x
  return i

