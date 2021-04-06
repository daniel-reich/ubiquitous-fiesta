
def trailing_zeros(n):
  if n<5: return 0
  return n//5+trailing_zeros(n//5)

