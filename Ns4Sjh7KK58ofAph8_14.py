
def is_triplet(n1, n2, n3):
  x = [n1,n2,n3]
  return max(x) ** 2 == sum([i**2 for i in x if i != max(x)])

