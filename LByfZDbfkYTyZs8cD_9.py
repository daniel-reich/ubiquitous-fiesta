
def areaofhexagon(x):
  if(x >= 0):
    if(round((3 * 3 ** 0.5 * x ** 2) / 2, 1) != 0.0):
      return round((3 * 3 ** 0.5 * x ** 2) / 2, 1)
    else:
      return None
  else:
    return None

