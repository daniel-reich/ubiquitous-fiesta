
def group(lst, size):
  groups = [[] for _ in range(round(len(lst) / size))]
  
  while lst:
    for i in groups:
      if lst:
        i.append(lst.pop(0))
  return groups

