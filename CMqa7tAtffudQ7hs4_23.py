
def sorting_steps(lst):
  lst = lst[:]
  swaps = []
  target = sorted(lst)
  for i in range(len(lst)):
    j = lst.index(target[i])
    lst[i], lst[j] = lst[j], lst[i]
    swaps.append((i,j))
  return swaps

