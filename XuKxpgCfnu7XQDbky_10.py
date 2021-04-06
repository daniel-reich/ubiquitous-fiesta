
def sum_and_product(x, y):
  delta = x ** 2 - 4 * y
  if delta < 0:
    return None
  return round((x - delta ** 0.5) / 2, 3), round((x + delta ** 0.5) / 2, 3)

