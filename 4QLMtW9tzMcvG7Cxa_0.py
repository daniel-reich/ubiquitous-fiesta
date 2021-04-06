
from functools import reduce
def resistance_calculator(resistors):
  if any(r == 0 for r in resistors):
    return [0, round(sum(resistors), 2)]
  tot = reduce(lambda a,r: [a[0] + 1/r, a[1] + r], resistors, [0, 0])
  return [round(1/tot[0], 2), round(tot[1], 2)]

