
def find_broken_keys(a,b):
  return sorted(set(v for i,v in enumerate(a) if v!=b[i]), key = a.index)

