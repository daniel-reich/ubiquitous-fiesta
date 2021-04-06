
def unique(lst):
  for i in lst:
    count = lst.count(i)
    if count == 1:
      return i

