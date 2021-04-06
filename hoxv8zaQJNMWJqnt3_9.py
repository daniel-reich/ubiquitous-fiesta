
def is_heteromecic(n, x=0):
  if x*(x+1) < n:
    return is_heteromecic(n, x+1)
  else:
    return x*(x+1) == n

