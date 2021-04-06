
import math
def DECIMATOR(txt):
  n = len(txt)/10
  n = int(math.ceil(n))
  txt = txt[:-n]
  return txt

