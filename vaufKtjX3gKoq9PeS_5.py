
def ohms_law(u, r, i):
  if [u,r,i].count(None)>1 or [u,r,i].count(None)<1:
    return 'Invalid'
  if not u:
    return round(r*i,2)
  if not r:
    return round(u/i,2)
  if not i:
    return round(u/r,2)

