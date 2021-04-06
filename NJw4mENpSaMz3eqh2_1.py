
def is_undulating(n):
  n=str(n)
  if len(n)<3: return False
  if len(set(n))!=2: return False
  return all(a!=b for a,b in zip(n,n[1:]))

