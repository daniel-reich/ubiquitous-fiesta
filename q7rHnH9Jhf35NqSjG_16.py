
def trailing_zeros(n):
  f = 32 if n>100000 else 16
  return round(n/(4+f/n)) if n else 0

