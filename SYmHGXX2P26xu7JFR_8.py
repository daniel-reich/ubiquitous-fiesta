
def number_groups(group1, group2, group3):
  a = (set(group1) & set(group2) )
  b = (set(group3) & set(group1))
  c = (set(group2) & set(group3))
  d = a.union(b, c)
  return sorted(list(d))

