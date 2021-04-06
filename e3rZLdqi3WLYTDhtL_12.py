
def search(lst, item):
  try:
    return sorted(lst).index(item)
  except:
    return -1

