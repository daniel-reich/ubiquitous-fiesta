
def find_factors(n):
  return [x for x in range(1, n+1) if n%x==0] if n else []

