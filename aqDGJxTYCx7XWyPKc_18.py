
def squares_sum(n):
  squares = 0
  for x in range(n+1):
    squares = x**2 + squares
  return squares

