
def find_factors(n):
  if n >= 1:
    return [i for i in range(1,n+1) if n % i == 0]
  else:
    return []

