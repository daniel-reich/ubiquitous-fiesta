
import math
from decimal import Decimal
def how_close_to_c(rapidity):
  return '{:.2e}'.format(Decimal(1/math.cosh(2*rapidity)))

