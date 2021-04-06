
def search(lst, item):
  for x in range(len(lst)):
    if lst[x]==item:
      return x
  return -1

