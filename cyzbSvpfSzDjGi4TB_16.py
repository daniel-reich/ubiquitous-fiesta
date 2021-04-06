
def harmonic(n):
  harm = 0
  for i in range(1,n+1):
    harm = harm + 1/i
  return round(harm,3)

