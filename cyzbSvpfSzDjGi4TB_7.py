
def harmonic(n):
  i = 1
  s = 0.0
  for i in range(1, n+1):
    s = s + 1/i
  return round(s,3)

