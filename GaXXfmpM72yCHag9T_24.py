
def unique(lst):
  for i in lst:
    n = lst.count(i)
    if n == 1:
      return i

