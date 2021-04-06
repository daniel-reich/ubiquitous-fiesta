
def search(arr, item):
  try:
    return arr.index(item)
  except ValueError:
    return -1

