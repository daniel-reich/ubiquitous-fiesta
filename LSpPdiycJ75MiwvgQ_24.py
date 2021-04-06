
from math import factorial as fact
def grid_pos(lst):
  a,b = lst
  return (fact(a+b)/fact(a))/fact(b)

