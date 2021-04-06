
def deNest(lst):
  if type(lst[0])!=list: return lst[0]
  return deNest(lst[0])

