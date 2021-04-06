
def setify(lst):
  newlst = []
  for i in lst:
    if not(i in newlst):
      newlst.append(i)
  return newlst

