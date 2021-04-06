
def number_groups(g1, g2, g3):
  A, B, C = set(g1), set(g2), set(g3)
  return sorted(list((A & B) | (B & C) | (A & C)))

