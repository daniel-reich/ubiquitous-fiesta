
def mystery_func(lst, n):
  newlst = []
  for i in lst:
    newlst.append(i%n)
  return newlst

