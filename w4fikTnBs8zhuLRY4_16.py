
def rep_set(n):
  if n==0: return []
  elif n==1: return [[]]
  return [rep_set(n-i) for i in range(n,0,-1)]

