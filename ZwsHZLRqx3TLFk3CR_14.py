
from math import factorial
​
def eval_factorial(lst):
  return sum(factorial(int(i.replace('!',''))) for i in lst)

