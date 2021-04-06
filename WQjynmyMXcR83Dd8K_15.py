
def number_of_swaps(lst):
  swaps = 0
  while sorted(lst) != lst:
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        swaps += 1
  return swaps

