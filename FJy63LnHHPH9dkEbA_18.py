
import decimal
import math
import numpy as np
def how_close_to_c(rapidity):
  res = 1 - math.tanh(rapidity)
  sech = decimal.Decimal(1 / np.cosh(2 * rapidity))
  return ('{:.2e}'.format(sech))

