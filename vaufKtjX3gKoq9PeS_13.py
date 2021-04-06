
def ohms_law(v, r, i):
  a = [v, r, i]
  if a.count(None)!=1: return "Invalid"
  if v==None: return round(r*i,2)
  elif r==None: return round(v/i,2)
  else: return round(v/r,2)

