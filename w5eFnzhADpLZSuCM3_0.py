
def multiplicity(lst):
  return [[i, lst.count(i)] for i in sorted(set(lst), key=lst.index)]

