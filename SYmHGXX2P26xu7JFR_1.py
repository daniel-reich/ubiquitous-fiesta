
def number_groups(*L):
  A, B, C = map(set, L)
  return sorted(A & B | B & C | C & A)

