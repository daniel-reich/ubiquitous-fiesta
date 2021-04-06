
def product(l):
  m=max(l)
  a=[x for x in l if x!=m]
  return m*max(a) if a else m*m

