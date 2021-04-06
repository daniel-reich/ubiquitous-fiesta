
def sorting_steps(lst):
  exp = sorted(lst)
  swaps = []
  for i in range(len(lst)):
    if lst[i] != exp[i]:
      j = lst.index(exp[i])
      swaps.append((i, j))
      lst[i], lst[j] = lst[j], lst[i]
  return swaps

