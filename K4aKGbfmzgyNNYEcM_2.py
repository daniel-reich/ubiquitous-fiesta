
def is_shape_possible(n, a):
  if n <=2 or any(i > 180 for i in a):
    return False
  return (180 - (360 / n)) * n == sum(a)

