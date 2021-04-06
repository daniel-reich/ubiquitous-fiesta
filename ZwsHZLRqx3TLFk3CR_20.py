
import math
def eval_factorial(lst):
  sum_num = 0
  for num in lst:
    x = int(num.split("!")[0])
    sum_num += math.factorial(x)
  return sum_num

