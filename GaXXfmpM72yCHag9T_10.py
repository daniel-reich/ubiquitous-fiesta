
def unique(lst):
  lst.sort()
  return lst[0] if lst.count(lst[0])==1 else lst[len(lst)-1]

