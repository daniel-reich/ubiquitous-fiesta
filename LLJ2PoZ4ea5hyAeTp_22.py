
import math
def DECIMATOR(txt):
  choplen = int(math.ceil(len(txt)/10))
  return txt[:(-1)*choplen]

