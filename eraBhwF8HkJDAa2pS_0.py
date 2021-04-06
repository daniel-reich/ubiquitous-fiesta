
def pirates_killed(gold, tolerance):
  x = list(zip([max(gold) - x for x in gold], tolerance))
  return any([e[0] > e[1] for e in x])

