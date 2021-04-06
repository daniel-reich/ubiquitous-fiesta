
def search(lst, item):
  lst.sort()
  if item in lst:
    return lst.index(item)
  else:
    return -1

