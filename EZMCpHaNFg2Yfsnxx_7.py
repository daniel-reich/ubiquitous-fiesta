
def unique_sort(lst):
  lst.sort()
  newlist = []
  for item in lst:
    if item not in newlist:
      newlist.append(item)
  return newlist

