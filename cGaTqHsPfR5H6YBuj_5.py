
def make_sandwich(i,f):
  o = []
  for l in i:
    if l == f:
      o.append('bread')
      o.append(l)
      o.append('bread')
    else:
      o.append(l)
      
  return o

