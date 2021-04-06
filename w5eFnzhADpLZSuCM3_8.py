
def multiplicity(a):
  return [[x, a.count(x)] for x in sorted(set(a), key=a.index)]

