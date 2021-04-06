
import math
def how_close_to_c(rapidity):
  return "{:.2e}".format(1/math.cosh(2*rapidity)).replace("-0","-")

