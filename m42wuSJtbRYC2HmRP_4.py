
from math import log10
def largest_exponential(lst):
  ml10, mxi = 0, 0
  for i in range(len(lst)):
    logexp = lst[i][1] * log10(lst[i][0])
    if logexp > ml10:
      ml10 = logexp
      mxi = i
  return mxi + 1

