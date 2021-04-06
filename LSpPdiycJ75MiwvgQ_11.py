
from math import factorial as f
def grid_pos(lst):
  a, b = sorted(lst)
  return f(b+a)/(f(a)*f(b))

