
def high_low(txt):
  txt = sorted(txt.split(), key=int)
  return txt[-1] + " " + txt[0]

