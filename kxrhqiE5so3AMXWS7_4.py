
import math
def get_number_of_apples(n, p):
  num = int(p.replace("%",""))/100
  if n - math.ceil(n*num)==0:
    return "The children didn't get any apples"
  else:
    return n - math.ceil(n*num)

