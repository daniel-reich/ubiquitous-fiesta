
def setify(lst):
  newlist = []
  for i in lst:
    if i not in newlist:
      newlist.append(i)
  return sorted(newlist)

