
def find_factors(n):
  r = []
  for i in range(1, n+1):
    if n%i == 0:
      r.append(i)
      
  return r

