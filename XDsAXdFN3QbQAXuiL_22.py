
def search(lst, item):
  index = 0
  for num in lst:
    if num == item:
      return index
    index += 1
  return -1

