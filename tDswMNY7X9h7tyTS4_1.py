
from math import factorial as fact
​
def pascals_triangle(n):
  res = []
  for i in range(n):
    res += [pascal_value(i, j) for j in range(i+1)]
  return res
    
def pascal_value(n, k):
  return int(fact(n) / (fact(k) * fact(n-k)))

