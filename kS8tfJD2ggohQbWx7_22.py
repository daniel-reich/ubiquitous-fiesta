
def last_name_lensort(names):
  return sorted(sorted(names, key = lambda x:x.split()[1]), key = lambda y: len(y.split()[1]))

