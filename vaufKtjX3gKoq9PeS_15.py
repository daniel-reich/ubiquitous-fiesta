
def ohms_law(v, r, i):
  x = [v, r, i] 
  if x.count(None) >= 2: return "Invalid"
  elif x.count(None) == 0: return "Invalid"
  elif v is None: return round(r*i,2)
  elif r is None: return round(v/i,2)
  elif i is None: return round(v/r,2)

