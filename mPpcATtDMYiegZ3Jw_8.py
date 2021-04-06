
def right_triangle(x, y, z):
  if x <= 0 or y <= 0 or z <= 0:
    return False
  max0 = max(x, y, z)
  sum = 0
  if x != max0:
    sum += x**2
  if y != max0:
    sum += y**2
  if z != max0:
    sum += z**2
  return sum == max0**2

