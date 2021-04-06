
def is_triplet(n1, n2, n3):
  lst = sorted([n1,n2,n3])
  return lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2

