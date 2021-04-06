
def last_name_lensort(names):
  return [' '.join(a) for a in sorted([x.split() for x in names],key=lambda x: (len(x[1]), x[1]))]

