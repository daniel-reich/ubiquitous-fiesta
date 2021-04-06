
def is_exact(n,x=1,f=1):
  if f > n:
    return 'Not exact!'
  elif f == n:
    return [f,x]
  x += 1
  return is_exact(n,x,f*x)

