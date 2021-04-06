
def is_shape_possible(n, angles):
  return n>2 and all(a<180 for a in angles) and (n-2)*180 == sum(angles)

