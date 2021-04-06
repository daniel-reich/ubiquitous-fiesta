
def block(lst):
  return sum([len(x) - 1 - x.index(2) for x in [list(x) for x in zip(*lst)] if 2 in x])

