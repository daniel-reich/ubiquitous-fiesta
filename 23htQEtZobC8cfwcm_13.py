
from functools import reduce
def canConcatenate(lst, target):
  lst = sorted(list(reduce(lambda x,y: x+y,lst)))
  target.sort()
  return lst == target

