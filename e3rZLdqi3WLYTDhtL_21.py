
def search(lst, item):
  for i in lst:
    if i == item:
      return lst.index(item)
  else:
      return -1

