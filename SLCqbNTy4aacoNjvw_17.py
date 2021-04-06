
def removeDups(lst):
  u = []
  for i in lst:
    if i not in u:
      u.append(i)
  return u

