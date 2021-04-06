
def number_groups(*g):
  a, b, c = [set(i) for i in g]
  return sorted(set.union(a.intersection(b),a.intersection(c),b.intersection(c)))

