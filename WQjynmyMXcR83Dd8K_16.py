
def number_of_swaps(lst): 
  swaps = 0
  while lst != sorted(lst):
    for i in range(len(lst) - 1):
      current = lst[i]
      nxt = lst[i + 1]
      if current > nxt:
        lst[i] = nxt
        lst[i + 1] = current
        swaps += 1
  return swaps

