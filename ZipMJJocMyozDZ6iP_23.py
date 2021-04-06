
from math import ceil
def group(lst, size):
  r=ceil(len(lst)/min(len(lst)/2,size))
  return [lst[i::r] for i in range(r)]

