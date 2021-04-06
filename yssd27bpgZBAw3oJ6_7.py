
def probability(u):
  denom = 1.
  for i in range(1, u):
    denom *= 1. - i / 365.
  return round(1. - denom, 2)

