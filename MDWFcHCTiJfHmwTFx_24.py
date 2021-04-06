
import math
def quadratic_equation(a, b, c):
  D = math.sqrt(b**2 - 4*a*c)
  x1 = (-b + D)/(2*a)
  x2 = (-b - D)/(2*a)
  return max(x1,x2)

