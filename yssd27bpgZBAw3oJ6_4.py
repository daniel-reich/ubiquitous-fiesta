
def probability(u, rounding=True):
  if u > 365:
    return 1
  if u == 2:
    return 1 / 365
  out = 1 - (1 - probability(u - 1, False)) * (366 - u) / 365
  if rounding:
    return round(out, 2)
  return out

