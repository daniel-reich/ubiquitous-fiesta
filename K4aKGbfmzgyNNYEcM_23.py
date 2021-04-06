
def is_shape_possible(n, angles):
​
  sum_of_interior = (n - 2) * 180
  sum_angles = sum(angles)
  all_below_180 = all([angle < 180 for angle in angles])
​
  if sum_of_interior == sum_angles and all_below_180:
    return True
​
  return False

