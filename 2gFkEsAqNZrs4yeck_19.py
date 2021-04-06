
def mini_peaks(lst):
  return [y for x, y, z in zip(lst[:-2], lst[1:-1], lst[2:]) if y > x and y > z]

