
def is_shape_possible(n, ang):
  return sum(ang)==(n-2)*180 and all(a<=180 for a in ang)

