
def remap(value, low1, high1, low2, high2):
  if (high1-low1)==0: return 0
  a = -(low2 - high2)/(high1-low1)
  b = low2 - a * low1
  return value*a+b

