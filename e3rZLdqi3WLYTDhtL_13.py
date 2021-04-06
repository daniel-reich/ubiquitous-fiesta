
def search(lst, item):
  count = 0
  length = len(lst)
  check = len(lst)
  while length > 0:
    if lst[count] == item:
      return count
    count += 1
    length -= 1
  if count == check:
    return -1
  return count

