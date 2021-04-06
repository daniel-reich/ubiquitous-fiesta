
def validate_swaps(lst, txt):
  would_swap = []
  for item in lst:
    if len(item) != len(txt):
      would_swap.append(False)
      continue
    swaps_needed = sum(
      element != required
      for element, required in zip(item, txt)
    )
    would_swap.append(swaps_needed == 2)
  return would_swap

