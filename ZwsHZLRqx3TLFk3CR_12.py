
def eval_factorial(lst):
  from math import factorial
  return sum([factorial(int(x.strip('!'))) for x in lst])

