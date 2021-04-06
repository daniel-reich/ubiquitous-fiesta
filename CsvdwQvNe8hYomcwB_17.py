
def remap(value, low1, high1, low2, high2):
  try:
    a = abs(value-low1) / abs(high1-low1)
    return round(abs(low2 + a*(high2-low2)),1)
  except:
    return 0

