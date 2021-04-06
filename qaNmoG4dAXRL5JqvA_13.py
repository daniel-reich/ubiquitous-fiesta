
def sum_fractions(lst):
  import math
  sum = 0
  for x in lst:
      sum += round(x[0] / x[1],1)
  return int(sum)

