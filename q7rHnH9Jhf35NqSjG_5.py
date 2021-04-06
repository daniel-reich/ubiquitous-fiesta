
def trailing_zeros(n):
  c=0
  while n:
    n//=5
    c+=n
  return c

