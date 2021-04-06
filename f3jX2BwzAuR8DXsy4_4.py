
from math import factorial
def fact_of_fact(n):
  a = 1
  for i in range(1, n+1):
    a *= factorial(i)
  return a

