
def multiplicity(lst):
  return [[x, lst.count(x)] for x in sorted(set(lst), key=lst.index)]

