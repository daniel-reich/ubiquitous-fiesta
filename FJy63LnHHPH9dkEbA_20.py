
from math import cosh
​
def how_close_to_c(rapidity):
  r = '{:.2e}'.format(1 / cosh(2 * rapidity))
  return r[:r.find('e') + 2] + r[r.find('e') + 2:].strip('0')

