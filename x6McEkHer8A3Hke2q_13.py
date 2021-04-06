
from functools import lru_cache as lru
​
@lru(maxsize=None)
def factorial(n):
  if n == 1:
    return n
  return n * factorial(n-1)

