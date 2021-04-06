
def DECIMATOR(txt):
  dec = len(txt)*.1
  if dec == int(dec):
    return txt[:-(int(dec))]
  return txt[:-(int(dec)+1)]

