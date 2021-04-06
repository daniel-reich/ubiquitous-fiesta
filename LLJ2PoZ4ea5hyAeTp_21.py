
def DECIMATOR(txt):
  a = len(txt)/10
  return txt[0:-(int(a) + ((int(a) - a) != 0))]

