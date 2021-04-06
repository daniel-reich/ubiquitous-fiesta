
def is_positive_dominant(lst):
  posnums = []
  negnums = []
  st = set(lst)
  lst = list(st)
  if 0 in lst:
    lst.remove(0)
  for i in range(len(lst)):
    if lst[i] > 0:
      posnums.append(lst[i])
    else:
      negnums.append(lst[i])
  if len(posnums) > len(negnums):
    return True
  else:
    return False

