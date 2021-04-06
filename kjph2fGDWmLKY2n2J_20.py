
def valid_color (color):
  res = False 
  code, color = color.split("(")
  color, _ = color.split(")")
  components = color.split(",")
  channels = [num(c) for c in components[:3]]
  if code == "rgb" and len(components)== 3 and validate(channels):
    res = True
  elif code == "rgba" and validate(channels):
    if len(components) == 4 and validateAlpha(float(components[-1])):
      res = True
  return res
    
def num(s):
    try:
        return int(s)
    except ValueError:
        return s
    
def validate(components):
  for c in components:
    if isinstance(c, int) and (c<0 or c>255):
      return False
    elif isinstance(c, str):
      c = c.split("%")
      c = num(c[0])
      if not isinstance(c, int) or c<0 or c>100:
        return False
  return True
      
def validateAlpha(a):
  if isinstance(a, float) and a >=0.0 and a <= 1.0:
    return True
  else:
    return False

