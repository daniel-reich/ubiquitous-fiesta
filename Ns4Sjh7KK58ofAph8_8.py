
def is_triplet(n1, n2, n3):
  l = [n1, n2, n3]
  pb = 0
  h = max(l)
  for i in l:
    if i != h:
      pb = pb + i**2
  if pb == h**2:
    return True
  return False

