
from decimal import Decimal, getcontext
def square_root(n):
  getcontext().prec = 40
  return round(Decimal(Decimal(n)**Decimal(.5)))

