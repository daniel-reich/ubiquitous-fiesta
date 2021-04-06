
import math
def DECIMATOR(txt):
  num = math.ceil(len(txt) / 10)
  new = txt[:-num]
  return new

