
def evenly_divisible(a, b, c):
  x = 0
  for i in range(a, b + 1):
    if i % c == 0:
      x += i
  return x

