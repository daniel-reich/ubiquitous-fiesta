
from math import factorial
​
s = set([ factorial(x) for x in range(200)])
​
def filter_factorials(numbers):
  return [ x for x in numbers if x in s ]

