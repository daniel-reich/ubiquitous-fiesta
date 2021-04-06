
def flatten(r):
  if type(r)!= list: return [r]
  return sum((flatten(e) for e in r),[])

