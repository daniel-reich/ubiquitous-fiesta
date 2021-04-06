
def multiplicity(lst):
  return [[i, lst.count(i)] for i in sorted(list(set(lst)), key=lambda x: lst.index(x))]

