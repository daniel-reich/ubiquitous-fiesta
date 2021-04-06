
from math import cosh
from decimal import Decimal
def how_close_to_c(rapidity):
  return "{:.2e}".format(Decimal(1/ cosh(2*rapidity)))

