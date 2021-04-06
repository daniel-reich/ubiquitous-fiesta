
def largest_gap(r):
  return max(y-x for x, y in zip(sorted(r), sorted(r)[1:]))

