
def number_groups(*groups):
  g1, g2, g3 = map(set, groups)
  I12 = set(g1) & set(g2) 
  I13 = set(g1) & set(g3)
  I23 = set(g2) & set(g3)
  I = I12 | I13 | I23
  return sorted(I)

