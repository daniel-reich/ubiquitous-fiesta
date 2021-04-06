
from functools import reduce
def volume_of_box(sizes):
  return reduce(lambda a, b: a * b, sizes.values())

