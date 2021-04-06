
def sum_and_product(s, p):
  n = (s * s - 4 * p)
  if n < 0: return None
  sr = (n)**0.5
  x1, x2 = round((s + sr) / 2, 3), round((s - sr) / 2, 3)
  y1, y2 = round(s - x1, 3), round(s - x2, 3)
  return min((x1, y1), (x2, y2))

