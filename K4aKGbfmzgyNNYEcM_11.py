
def is_shape_possible(n, angles):
  return (n-2)*180==sum(angles) and all(x<180 for x in angles)

