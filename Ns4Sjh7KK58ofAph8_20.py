
def is_triplet(n1, n2, n3):
  s = sorted([n1, n2, n3])
  return s[0]**2 + s[1]**2 == s[2]**2

