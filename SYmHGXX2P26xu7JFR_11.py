
def number_groups(g1, g2, g3):
  return sorted(set(list(set(g1).intersection(set(g2))) + list(set(g1).intersection(set(g3))) + list(set(g2).intersection(set(g3)))))

