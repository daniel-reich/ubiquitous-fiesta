
def intersection(h1, h2):
  d1 = {}
  d2 = {}
  for k in h1:
    if k in h2:
      d1[k] = h1[k]
      d2[k] = h2[k]
    
  return [d1,d2]

