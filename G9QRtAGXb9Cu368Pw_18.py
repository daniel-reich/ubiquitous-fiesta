
import math
def combinations(*args):
  out = 1
  for _int in args :
    if _int != 0:
      out *= _int
  return out

