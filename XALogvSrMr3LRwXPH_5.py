
def is_shuffled_well(lst):
  return not any(abs(x-y) == 1 and abs(y-z) == 1 and abs(x-z) == 2 for x, y, z in zip(lst[:-2], lst[1:-1], lst[2:]))

