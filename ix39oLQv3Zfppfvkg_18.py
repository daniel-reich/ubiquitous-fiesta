
def multiply_matrix(m1, m2):
  if m2 and len(m1) == len(m2[0]):
    return [[sum(a*b for a,b in zip(r,c)) 
      for c in [list(r) for r in zip(*m2)]] 
      for r in m1]
  return "ERROR"

