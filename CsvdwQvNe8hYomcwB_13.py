
def remap(value, low1, high1, low2, high2):
  r1,r2 = high1-low1,high2-low2
  if r1==0: return 0
  return round(((value-low1)*r2/r1+low2),1)

