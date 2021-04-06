
def perrin(n):
  a, b, c = 3, 0, 2
  for i in range(n):
    a, b, c = b, c, a + b
  return a

