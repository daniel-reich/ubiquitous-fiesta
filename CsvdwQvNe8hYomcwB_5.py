
def remap(value, low1, high1, low2, high2):
  range1 = high1 - low1 
  if range1 == 0: return 0
  range2 = high2 - low2
  aux1 = (value - low1)/range1*range2 + low2
  return aux1

