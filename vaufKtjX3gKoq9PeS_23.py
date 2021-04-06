
def ohms_law(v, r, i):
  if len([i for i in [v,r,i] if not i])>=2 or len([i for i in [v,r,i] if not i])==0:
    return 'Invalid'
  return round(r*i,2) if not v else round(v/r,2) if not i else round(v/i,2)

