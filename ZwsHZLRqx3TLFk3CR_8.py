
import math
def eval_factorial(lst):
  return sum(math.factorial(int(i[:-1])) for i in lst)

