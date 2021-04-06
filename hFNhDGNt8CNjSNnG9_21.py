
def setify(lst):
  lst2 = []
  for itm in lst:
    if itm not in lst2:
      lst2.append(itm)
  return lst2

