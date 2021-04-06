
from math import exp
​
def how_close_to_c(r):
  return '{:.2e}'.format(2*exp(-2*r)/(1+exp(-4*r))).replace('e-0','e-')

