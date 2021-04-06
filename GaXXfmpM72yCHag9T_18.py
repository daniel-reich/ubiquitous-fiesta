
def unique(lst):
  new = set(lst)
  for i in new:
    if lst.count(i) == 1:
      return i

