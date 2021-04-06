
def compound_interest(p, t, r, n):
  total = p
  for _ in range (t * n): total += total * r / n
  return round (total, 2)

