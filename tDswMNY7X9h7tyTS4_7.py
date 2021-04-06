
from math import factorial as fact
​
def pascals_triangle(n):
  return [
    fact(i) // (fact(j) * fact(i - j))
    for i in range(n)
    for j in range(i + 1)
  ]

