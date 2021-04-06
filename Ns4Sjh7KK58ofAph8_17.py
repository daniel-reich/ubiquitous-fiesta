
def is_triplet(n1, n2, n3):
  order = [n1,n2,n3]
  order.sort()
  x = (order[0]**2) + (order[1]**2)
  y = order[2]**2
  return x == y

