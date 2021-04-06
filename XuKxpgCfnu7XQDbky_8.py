
def sum_and_product(s, p):
  a = 1
  b = -1 * s
  c = p
  d = b ** 2 - 4 * a * c
  try:
    x = round((-1 * b + d ** (0.5)) / (2 * a), 3)
    y = round(s - x, 3)
    return y, x
  except:
    return None

