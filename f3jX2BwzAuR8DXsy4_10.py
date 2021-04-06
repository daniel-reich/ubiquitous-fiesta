
import math
def facts(n):
  return math.factorial(n)
​
def fact_of_fact(n):
  total = 1
  for i in range(n, 1,-1):
    total = total*facts(i)
  return total

