
def setify(lst):
  #sort list and remove all items that occur twice
  newlist = []
  for item in lst:
    if item not in newlist:
      newlist.append(item)
  
  return newlist

