
def convert(deg):
  if deg[-1] == "F":
    C = (int(deg[:-2])-32)*5/9
    return "{:.0f}*C".format(C)
  if deg[-1] == "C":
    F = int(deg[:-2])*9/5 + 32
    return "{:.0f}*F".format(F)
  return 'Error'

