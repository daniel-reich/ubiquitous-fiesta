
def find_none(lst):
  try:
    return lst.index(None)
  except ValueError:
    return -1

