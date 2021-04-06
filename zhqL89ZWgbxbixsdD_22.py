
def is_exact(n, m=None,i=1):
  if m is None: m=n
  if n == 1: return [m,i-1]
  if n%i: return "Not exact!"
  return is_exact(n//i,m,i+1)

