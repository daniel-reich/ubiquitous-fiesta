
import math
​
def eval_factorial(lst):
  return sum(math.factorial(int(x[:-1])) for x in lst)

