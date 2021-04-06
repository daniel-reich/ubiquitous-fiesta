
from math import exp
​
def how_close_to_c(rapidity):
  ret = "{:.2e}".format(2*exp(-2*rapidity)/(1+exp(-4*rapidity)))
  a, b = ret.split("e")
  return "{}e{}".format(a, int(b))

