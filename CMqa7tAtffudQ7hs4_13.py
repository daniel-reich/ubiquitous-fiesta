
def sorting_steps(lst): # Insertion sort
  swaps = []
  for i in range(1, len(lst)):
    while lst[i] < lst[i - 1] and i > 0:
      swaps.append((i - 1, i))
      lst[i], lst[i - 1] = lst[i - 1], lst[i]
      i -= 1
  return swaps

