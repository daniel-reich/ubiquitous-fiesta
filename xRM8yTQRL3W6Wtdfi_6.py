
from math import sqrt
def quartic_equation(a, b, c):
  if (b ** 2) - (4 * a * c) < 0:
    return 0
  elif c == 0 and b < 0:
    return 3
  elif c == 0 and b > 0:
    return 1
  else:
    sol1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a)
    sol2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a)
    if sol1 > 0 and sol2 > 0:
      return 4
    elif sol1 < 0 and sol2 < 0:
      return 0
    elif sol1 < 0 or sol2 < 0:
      return 2

