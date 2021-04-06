
from math import sqrt
def quad(a, b, c):
  return (-b + sqrt(b**2 - 4 * a * c))/(2*a)
  
​
def f(A, c):
  #a * b  = 2*A - > a**2*b**2 = 4A**2
  #a^2 + b^2 = c^2 -> a^4 + a^2*b^2 = a^2*c^2 -> a^4 - c^2a^2 + 4A^2 = 0
  try:
    a = sqrt(quad(1, -c**2, 4 * A**2))
  except ValueError:
    return "Does not exist"
  b = (2 * A)/a
  return list(sorted([round(s, 3) for s in (a, b)]))

