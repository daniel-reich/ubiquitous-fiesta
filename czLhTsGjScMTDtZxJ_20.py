
from math import sqrt
def is_prime(num):
  return num > 1 and all([num % i for i in range(2, int(sqrt(num)) + 1)])
​
from functools import reduce
def primorial(num):
  res = []
  cnt = 2
  while len(res) < num:
    if is_prime(cnt):
      res.append(cnt)
    cnt += 1
  return reduce(lambda a, b: a * b, res)

