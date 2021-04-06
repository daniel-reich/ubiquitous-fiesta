
def junction_or_self(n):
  junction = [k for k in range(n,-1,-1) if k + sum(map(int,str(k))) == n]
  return junction or 'Self'

