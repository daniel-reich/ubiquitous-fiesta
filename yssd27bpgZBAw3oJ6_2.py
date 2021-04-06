
def probability(u):
  pnot = 1
  for i in range(u-1):
    pnot*= (364-i)/365
  return round(1 - pnot,2)

