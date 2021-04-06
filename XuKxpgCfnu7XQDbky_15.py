
from math import sqrt
def sum_and_product(s, p):
  discriminant = pow(s,2) - (4*p)
  try:
    return (round((s- sqrt(discriminant))/2,3), round((s + sqrt(discriminant)) / 2,3))
  except ValueError:
    return None

