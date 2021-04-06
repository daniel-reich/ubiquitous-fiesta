
def sorting_steps(lst):
  swaps = []
  for i in range(len(lst)):
    i2 = lst[i:].index(min(lst[i:])) + i
    lst[i], lst[i2] = lst[i2], lst[i]
    swaps.append((i, i2))
  return swaps

