
def DECIMATOR(txt):
  import math
  l=len(txt)
  n=math.ceil(l/10)
  return txt[:l-n]

