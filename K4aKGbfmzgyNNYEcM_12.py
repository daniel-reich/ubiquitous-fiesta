
def is_shape_possible(n, angles):
  return sum(angles)==(n-2)*180 and n>2 and all(i<=180 for i in angles)

