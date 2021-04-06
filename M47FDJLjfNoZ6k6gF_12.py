
from functools import reduce
def cup_swapping(swaps):
  return reduce(lambda a, b: b.replace(a, "") if a in b else a, swaps, "B")

