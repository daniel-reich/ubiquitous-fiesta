
def remove_dups(lst):
  newList = []
  for item in lst:
    if not item in newList:
      newList.append(item)
  return newList

