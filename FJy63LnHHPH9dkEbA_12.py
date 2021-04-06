
from math import cosh
​
def how_close_to_c(rapidity):
  return '{:.2e}'.format(1/cosh(2*rapidity)).replace('-0', '-')

