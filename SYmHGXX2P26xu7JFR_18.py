
def number_groups(a, b, c):
  x, y, z = set(a) & set(b), set(a) & set(c), set(b) & set(c)
  return sorted(set(k for v in map(list, (x, y, z)) for k in v))

