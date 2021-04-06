
import math
def how_close_to_c(rap):
  return '{:.2e}'.format(1/math.cosh(2*rap)).replace('-0','-')

