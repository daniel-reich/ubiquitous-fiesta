
import math
def eval_factorial(lst):
  s = 0
  for el in lst: s += math.factorial(int(el.split('!')[0]))
  return s

