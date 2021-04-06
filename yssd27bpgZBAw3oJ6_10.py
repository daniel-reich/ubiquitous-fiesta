
def probability(u):
  p=1
  for i in range(1, u):
    p*=(365-i)/365
  return round(1-p,2)

