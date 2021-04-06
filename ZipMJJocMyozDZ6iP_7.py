
from math import *
def group(lst, size):
  length = ceil(len(lst) / size)
  subs = [[] for _ in range(length)]
  for i,n in enumerate(lst):
    subs[i%length].append(n)
  return subs

