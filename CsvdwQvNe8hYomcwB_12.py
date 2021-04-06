
def remap(value, low1, high1, low2, high2):
  try: ratio = (value - low1) / (high1 - low1)
  except: return 0
  return low2 + (high2 - low2) * ratio

