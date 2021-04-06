
def remap(value, low1, high1, low2, high2):
  return (value-low1)/(high1-low1)*(high2-low2)+low2 if (high1-low1)!=0 else 0

