
def ohms_law(v, r, i):
  count =(v is None)+(i is None)+(r is None)
  if count != 1: return "Invalid"
  if v is None: ans= round((i*r),2)
  if i is None: ans= round(( v/r),2)
  if r is None: ans= round((v/i),2)
  return (ans)

