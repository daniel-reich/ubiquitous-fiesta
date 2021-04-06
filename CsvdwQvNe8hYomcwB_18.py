
def remap(value, low1, high1, low2, high2):
  if (low1==high1): return 0
  return low2 + (value-low1)/(high1-low1)*(high2-low2)

