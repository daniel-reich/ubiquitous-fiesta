
def eval_factorial(lst):
  import math
  a = 0
  for i in lst:
    a += math.factorial(int(i[:len(i) - 1]))
  return a

