
def ohms_law(u, r, i):
  if u==None and [u,r,i].count(None)==1:
    return r*i
  elif r==None and [u,r,i].count(None)==1:
    return round(u/i,2)
  elif i==None and [u,r,i].count(None)==1:
    return round(u/r,2)
  else:
    return "Invalid"

