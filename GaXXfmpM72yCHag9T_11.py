
def unique(lst):
  a = set(lst)
  a0 = list(a)[0]
  a1 = list(a)[1]
  return [a0,a1][lst.count(a0)!=1]

