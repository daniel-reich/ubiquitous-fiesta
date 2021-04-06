
def areaofhexagon(x):
  if x <= 0:
    return None
  else:
    return round(3 * pow(3,1/2) * pow(x,2) / 2,1)

