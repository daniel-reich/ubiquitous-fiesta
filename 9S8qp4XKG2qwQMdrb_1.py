
def ways_to_climb(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return b

