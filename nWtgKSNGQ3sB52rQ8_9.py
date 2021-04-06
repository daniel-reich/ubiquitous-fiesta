
def evenly_divisible(a, b, c):
  return sum([x for x in range(a, b+1) if x%c==0])

