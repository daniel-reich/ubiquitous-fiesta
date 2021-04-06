
def remap(value, low1, high1, low2, high2):
  try:
    return ((value - low1) / (high1 - low1))* (high2 - low2)+low2 
  except:
    return 0

