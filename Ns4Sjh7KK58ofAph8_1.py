
def is_triplet(n1, n2, n3):
  a, b, h = sorted((n1, n2, n3))
  return a**2 + b**2 == h**2

