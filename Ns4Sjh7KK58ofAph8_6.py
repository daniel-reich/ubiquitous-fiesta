
def is_triplet(n1, n2, n3):
  pyth = sorted([n1, n2, n3])
  return pyth[2] * pyth[2] == pyth[0] * pyth[0] + (pyth[1] * pyth[1])

