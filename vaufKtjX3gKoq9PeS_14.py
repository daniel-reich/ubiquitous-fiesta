
def ohms_law(v, r, i):
  
  Parameters = []
  Parameters.append(v)
  Parameters.append(r)
  Parameters.append(i)
  
  if (Parameters.count(None) >= 2):
    return "Invalid"
  elif (v == None):
    return round(r * i, 2)
  elif (r == None):
    return round(v / i, 2)
  elif (i == None):
    return round(v / r, 2)
  else:
    return "Invalid"

