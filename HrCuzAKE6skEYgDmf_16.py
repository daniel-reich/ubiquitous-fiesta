
from math import ceil
def pairs(lst):
  return [[lst[z], lst[-z-1]] for z in range(ceil(len(lst)/2))]

