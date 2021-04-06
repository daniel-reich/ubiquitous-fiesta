
import math
def get_number_of_apples(n, p):
  p = int(p[:-1])/100
  return math.floor(n - p*n) if math.floor(n - p*n)!=0 else "The children didn't get any apples"

