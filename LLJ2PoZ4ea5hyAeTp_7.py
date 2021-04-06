
def DECIMATOR(txt):
  import math
  n = math.ceil(len(txt)/10)
  return txt[0:-n]

