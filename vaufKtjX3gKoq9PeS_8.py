
def ohms_law(v, r, i):
  l = [i for i in (v,r,i)]
  if l.count(None) == 1:
    if i == None:
      return round(v/r,2)
    elif r == None:
      return v/i
    elif v == None:
      return r*i
  else:
    return "Invalid"

