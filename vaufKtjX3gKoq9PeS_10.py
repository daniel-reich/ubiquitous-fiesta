
def ohms_law(v, r, i):
  lst=[v,r,i]
  if lst.count(None)>1or lst.count(None)==0:
    return "Invalid"
  if v==None:
    return i*r
  if r==None:
    return round(v/i,2)
  return round(v/r,2)

