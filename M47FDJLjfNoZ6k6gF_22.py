
def cup_swapping(swaps):
  pos = "B"
  for swap in swaps:
    if not pos in swap:
      continue
    for p in swap:
      if p != pos:
        pos = p
        break
  return pos

