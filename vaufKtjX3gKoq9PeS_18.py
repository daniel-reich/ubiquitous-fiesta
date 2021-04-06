
def ohms_law(v, r, i):
  if (v==None and r!=None and i!= None):
    return round(r*i, 2)
  elif (v!=None and r==None and i!= None):
    return round(v/i, 2)
  elif (v!=None and r!=None and i== None):
    return round(v/r, 2)
  else: return "Invalid"

