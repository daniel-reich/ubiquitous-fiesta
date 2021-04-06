
def measure_the_depth(lst):
  if not lst:
    return 1
  else:
    return measure_the_depth(lst[0]) + 1

