
def number_of_swaps(lst):
  total_swaps = 0
  swaps = None
  while swaps != 0:
    swaps = 0
    for n in range(len(lst) - 1):
      if lst[n] > lst[n + 1]:
        lst[n], lst[n + 1] = lst[n + 1], lst[n]
        total_swaps += 1
        swaps += 1
  return total_swaps

