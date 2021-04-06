
import math
def get_number_of_apples(n, p):
  p = int(p.replace("%", "")) / 100
  r = math.ceil(int(n) * p)
  if (n - r) > 0:
    return n - r
  else:
    return "The children didn't get any apples"

