
def evenly_divisible(a, b, c):
  return sum([i for i in range(a, b+1) if i % c == 0])

