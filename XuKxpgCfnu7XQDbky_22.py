
def sum_and_product(s, p):
  discriminant = s**2 - (4 * p)
  if discriminant < 0:
    return None
  ys = [
    (-s + (discriminant)**0.5) / (-2),
    (-s - (discriminant)**0.5) / (-2)
  ]
  results = []
  for y in ys:
    results.append((round(s - y, 3), round(y, 3)))
  return sorted(results)[0]

