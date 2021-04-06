
def multiplicity(lst):
  keys = []
  for k in lst:
    if k not in keys: keys.append(k)
  return [[k,lst.count(k)] for k in keys]

