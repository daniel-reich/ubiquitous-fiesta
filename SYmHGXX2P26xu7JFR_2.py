
def number_groups(g1, g2, g3):
  return [n for n in set(g1+g2+g3) if sum(n in g for g in [g1,g2,g3])>1]

