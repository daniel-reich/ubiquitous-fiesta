
def iso_group(lst,maxs=[-10000000]):
  if len(lst) == 0:
    return maxs[0] if len(maxs) == 1 else maxs
  elif lst[0] > maxs[0]:
    maxs=[lst[0]]
  elif lst[0] == maxs[0]:
    maxs.append(lst[0])
  return iso_group(lst[1:],maxs)

