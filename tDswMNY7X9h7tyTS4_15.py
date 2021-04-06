
from math import factorial
def pascals_triangle(n):
  res = []
  for i in range(n):
    for j in range(i+1):
      res.append(factorial(i)/(factorial(j)*factorial(i-j)))
  return res

