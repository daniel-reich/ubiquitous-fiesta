
def delete_occurrences(lst, num):
  newlst = []
  for x in lst:
    if newlst.count(x) != num or x not in newlst:
      newlst.append(x)
  return newlst

