
import math
def era(er, ip):
  x = math.floor(er * 9 / ip * 100)  / 100
  return '{:.2f}'.format(x)

