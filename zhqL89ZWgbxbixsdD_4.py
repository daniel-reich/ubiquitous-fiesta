
def is_exact(N, n=0, i=2):
  if not n:
    n = N
    
  n /= i
  if n%1:
    return 'Not exact!'
  elif n == 1:
    return [N, i]
  else:
    return is_exact(N, n, i+1)

