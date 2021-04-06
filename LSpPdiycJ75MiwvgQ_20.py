
from math import factorial as f
def grid_pos(lst):
  return (f(lst[0] + lst[1]) / f(lst[0])) / f(lst[1])

