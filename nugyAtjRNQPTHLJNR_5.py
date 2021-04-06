
from math import sqrt
def pages_in_book(total):
  r=sqrt(1+8*total)
  if int(r)==r:
    return True
  return False

