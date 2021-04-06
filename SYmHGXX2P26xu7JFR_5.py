
def number_groups(group1, group2, group3):
  g1 = set(group1)
  g2 = set(group2)
  g3 = set(group3)
  return sorted(g1 & g2 | g3 & g2 | g3 & g1)

