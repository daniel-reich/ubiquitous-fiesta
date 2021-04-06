
def is_exact(n, f=1, n2=None):
  if n2 is None:
    n2 = n
  if n2%f != 0:
    return 'Not exact!'
  if n2 == f:
    return [n, f]
  return is_exact(n, f+1, n2//f)

