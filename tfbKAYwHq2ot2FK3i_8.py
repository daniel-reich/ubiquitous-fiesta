
from math import factorial
def nPr(n, r):
  return factorial(n) / factorial(n - r)
​
def non_repeats(radix):
  return sum(nPr(radix, i) * (radix - 1) / radix for i in range(1, radix + 1))

