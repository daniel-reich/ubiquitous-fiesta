
def search(lst, item):
  try:
    return lst.index(item)
  except ValueError:
    return -1

