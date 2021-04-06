
def removeDups(lst):
  L = []
  for i in range(len(lst)):
    if lst[i] not in L:
      L.append(lst[i])
  return L

