
from math import factorial
def eval_factorial(lst):
  return sum(factorial(int(i[:-1])) for i in lst)

