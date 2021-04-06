
import math
def sum_and_product(s, p):
  det = s*s - 4*p
  if det >= 0:
    sol = (s - math.sqrt(det)) / 2
    return (round(sol, 3), round(s - sol, 3))

