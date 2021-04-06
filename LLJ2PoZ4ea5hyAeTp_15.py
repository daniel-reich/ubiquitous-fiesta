
def DECIMATOR(txt):
  import math
  i = math.ceil(len(txt)/10)
  return txt[0:len(txt)-i]

