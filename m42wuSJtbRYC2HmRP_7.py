
import math
def largest_exponential(lst):
  exp_lst = [pair[1]*math.log10(pair[0]) for pair in lst]
  return 1 + exp_lst.index(max(exp_lst))

