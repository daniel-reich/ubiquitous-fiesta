
def ohms_law(*args):
  if args.count(None) != 1: return 'Invalid'
  
  v,r,i = args
  if v == None: return round(r*i,2)
  if r == None: return round(v/i,2)
  return round(v/r,2)

