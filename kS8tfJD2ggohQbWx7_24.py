
def last_name_lensort(names):
  return [' '.join(n) for n in sorted(sorted([n.split() for n in names], key=lambda x: x[1]), key=lambda x: len(x[1]))]

