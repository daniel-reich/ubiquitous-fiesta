
def deepest(lst):
  if type(lst)!= list: return 0
  return 1 + max(deepest(e) for e in lst)

