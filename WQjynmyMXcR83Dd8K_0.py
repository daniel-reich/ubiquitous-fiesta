
def number_of_swaps(lst):
  swaps, target = 0, sorted(lst)
  while lst != target:
    for i in range(len(lst) - 1):
      if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        swaps += 1
  return swaps

