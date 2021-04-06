
def is_shape_possible(n, angles):
  return False if n <3 else sum(angles) == (n-2)*180 \
                        and all(x<=180 for x in angles)

