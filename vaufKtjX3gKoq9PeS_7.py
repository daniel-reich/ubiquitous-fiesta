
def ohms_law(v, r, i):
  try:
    if v != None and r != None and i != None:
      raise Invalid
    if v == None:
      return round(r * i,2)
    if r == None:
      return round(v / i,2)
    return round(v / r,2)
  except:
    return 'Invalid'

