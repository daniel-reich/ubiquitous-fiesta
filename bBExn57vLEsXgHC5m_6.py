
from functools import reduce
def same_line(lst):
  b = [reduce(lambda x,y: x-y, z) for z in zip(*lst)]
  return b[0]-1 != b[1]

