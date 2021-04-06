
def modulo(x, y):
  if x - y == 0:
    return 0
  elif abs(x) < abs(y):
    return x
  is_x_negative = x < 0
  is_y_negative = y < 0
  if ((is_x_negative and not is_y_negative)
    or (not is_x_negative and is_y_negative)
  ):
    return modulo(x + y, y)
  return modulo(x - y, y)

