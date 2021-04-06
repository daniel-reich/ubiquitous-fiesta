
def complete_bracelet(lst):
  # Going over all possible slicings of the list - from slices of length 2 to half the list.
  for k in range(2, len(lst) // 2 + 1):
    # Length of the list must be divisible by k.
    if len(lst) % k != 0:
      continue
    complete = True
    for l in range(2, len(lst) // k + 1):
      if lst[:k] != lst[(l-1)*k:l*k]:
        complete = False
        break
    if complete:
      return True
  return False

