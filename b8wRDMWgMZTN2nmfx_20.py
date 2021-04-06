
def equal(a, b, c):
  d=set()
  d.update({a,b,c})
  if len(d)==3: return 0
  if len(d)==2: return 2
  return 3

