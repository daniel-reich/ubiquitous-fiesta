
from math import factorial as f
def eval_factorial(lst):
  return sum(f(int(x[:-1])) for x in lst)

