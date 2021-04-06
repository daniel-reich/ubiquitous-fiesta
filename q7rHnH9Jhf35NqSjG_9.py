
def trailing_zeros(n):
  cur = 0
  while n>=5:
    n = n//5
    cur+=n
  return cur

